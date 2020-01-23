library(tidycensus)
library(tidyverse)

nm <- get_acs(geography = "county", 
              variables = c(hhincome = "DP03_0062", 
                            pctba = "DP02_0067P", 
                            medage = "DP05_0017"), 
              state = "NM", 
              output = "wide") %>%
  select(county = NAME, hhincome = hhincomeE, 
         pct_college = pctbaE, 
         median_age = medageE) %>%
  mutate(county = str_replace(county, " County, New Mexico", ""))


write_csv(nm, "data/new_mexico.csv")


texas <- get_acs(geography = "county", 
        variables = c(pct_internet = "DP02_0152P", 
                      pct_poverty = "DP03_0128P"), 
        survey = "acs1", 
        year = 2017, 
        state = "TX") %>%
  select(county = NAME, variable, estimate) %>%
  spread(key = variable, value = estimate) %>%
  mutate(county = str_replace(county, " County, Texas", ""))


write_csv(texas, "data/texas.csv")
