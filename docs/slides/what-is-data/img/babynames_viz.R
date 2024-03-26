library(babynames)
library(tidyverse)
library(plotly)

tx_names <- babynames::babynames %>%
  filter(name %in% c("Mary", "Gertrude", "Sophia", "Emma"), 
         sex == "F") %>%
  mutate(per1000 = prop * 1000)

gg <- ggplot(tx_names, aes(x = year, y = per1000, color = name)) + 
  geom_line() + 
  theme_minimal(base_size = 18) + 
  labs(x = "Year",
       y = "Names per 1000",
       color = "") + 
  scale_color_brewer(palette = "Dark2")

ggp <- ggplotly(gg)

htmlwidgets::saveWidget(ggp, "slides/what-is-data/img/babynames.html")
