# Babynames slide figures for 01-data-literacy (refreshed 2026-08 with SSA data
# through 2025). Run from the repo root. Raw SSA files: names.zip (national) and
# namesbystate.zip from https://www.ssa.gov/oact/babynames/limits.html, unzipped
# to the paths below. All figures use Texas girls' names to match the slide's
# example question; per1000 is computed within the SSA files, whose counts omit
# names with fewer than 5 occurrences in a year.

library(tidyverse)
library(plotly)
library(gt)

ssa_dir <- Sys.getenv("SSA_DIR", "ssa")
out_dir <- "slides/img/01-data-literacy"

# --- Course dataset: rebuild data/babynames.csv (1880-2025) -------------------
# Same schema as the legacy file (year, sex, name, n, prop). Note prop here is
# n / sum(n) within year and sex over the >=5-occurrence names in the SSA file;
# the old R babynames package divided by total applicants instead, so historical
# prop values differ slightly.
national <- list.files(file.path(ssa_dir, "national"),
                       pattern = "^yob\\d{4}\\.txt$", full.names = TRUE) |>
  map(function(f) {
    read_csv(f, col_names = c("name", "sex", "n"), col_types = "cci") |>
      mutate(year = as.integer(str_extract(basename(f), "\\d{4}")))
  }) |>
  list_rbind() |>
  group_by(year, sex) |>
  mutate(prop = n / sum(n)) |>
  ungroup() |>
  select(year, sex, name, n, prop)

write_csv(national, "data/babynames.csv")

# --- Texas girls' names -------------------------------------------------------
tx_f <- read_csv(file.path(ssa_dir, "states", "TX.TXT"),
                 col_names = c("state", "sex", "year", "name", "n"),
                 col_types = "ccici") |>
  filter(sex == "F") |>
  group_by(year) |>
  mutate(per1000 = 1000 * n / sum(n)) |>
  ungroup()

# --- Table: top 10 TX girls' names, 2025 --------------------------------------
top10_2025 <- tx_f |>
  filter(year == 2025) |>
  arrange(desc(n)) |>
  mutate(rank = row_number()) |>
  slice_head(n = 10) |>
  select(state, sex, year, name, count = n, per1000, rank)

gt(top10_2025) |>
  fmt_number(columns = per1000, decimals = 2) |>
  tab_options(table.font.size = px(18)) |>
  gtsave(file.path(out_dir, "names_table.PNG"))

# --- Heatmap: top 25 names of 2025, tracked 1990-2025 -------------------------
top25 <- top10_2025 |> select(name) |> pull() |> union(
  tx_f |> filter(year == 2025) |> slice_max(n, n = 25) |> pull(name)
)

heat_df <- tx_f |>
  filter(name %in% top25, year >= 1990) |>
  complete(name, year = 1990:2025, fill = list(per1000 = 0))

heatmap_gg <- ggplot(heat_df, aes(x = year, y = fct_rev(factor(name)), fill = per1000)) +
  geom_tile(color = "white", linewidth = 0.3) +
  scale_fill_distiller(palette = "RdPu", direction = 1) +
  scale_x_continuous(breaks = seq(1990, 2025, 5), expand = c(0, 0)) +
  theme_minimal(base_size = 16) +
  labs(title = "Female baby names per 1000 in the SSA data (TX)",
       x = "", y = "", fill = "Per 1000") +
  theme(panel.grid = element_blank())

ggsave(file.path(out_dir, "heatmap.png"), heatmap_gg,
       width = 12, height = 8, dpi = 150, bg = "white")

# --- Presenting-data figure: four names across a century of TX data ----------
# Okabe-Ito colors (the CVD-safe palette Wilke's color chapter recommends);
# identity is doubled by direct labels in ink, so color is never load-bearing.
four_names <- tx_f |>
  filter(name %in% c("Mary", "Gertrude", "Sophia", "Emma"))

pal <- c(Mary = "#E69F00", Gertrude = "#56B4E9",
         Sophia = "#009E73", Emma = "#CC79A7")

peak_labels <- four_names |>
  filter(name %in% c("Mary", "Gertrude", "Sophia")) |>
  group_by(name) |>
  slice_max(per1000, n = 1, with_ties = FALSE) |>
  ungroup()
emma_end <- four_names |> filter(name == "Emma") |> slice_max(year, n = 1)

lines_gg <- ggplot(four_names, aes(x = year, y = per1000, color = name)) +
  geom_line(linewidth = 1) +
  geom_text(data = peak_labels,
            aes(label = name), color = "#333333",
            vjust = -0.8, size = 5, fontface = "bold") +
  geom_text(data = emma_end,
            aes(label = name), color = "#333333",
            hjust = -0.15, size = 5, fontface = "bold") +
  annotate("text", x = 1946, y = 5.5,
           label = "Gertrude disappears: fewer than five\nTexas girls a year get the name",
           color = "#777777", size = 3.8, hjust = 0, vjust = 0, lineheight = 1) +
  scale_color_manual(values = pal, guide = "none") +
  scale_x_continuous(breaks = seq(1910, 2010, 20), limits = c(1908, 2036)) +
  theme_minimal(base_size = 16) +
  theme(panel.grid.minor = element_blank()) +
  labs(title = "A century of girls' names in Texas",
       subtitle = "Births per 1,000 girls given each name, 1910–2025",
       x = NULL, y = "Names per 1,000",
       caption = "Source: Social Security Administration state name files, 2025 release.\nNames with fewer than five occurrences in a state-year are not reported.")

ggsave(file.path(out_dir, "babynames_lines.png"), lines_gg,
       width = 12, height = 6.75, dpi = 150, bg = "white")
