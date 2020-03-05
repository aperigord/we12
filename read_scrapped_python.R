library(jsonlite)
library(dplyr)
library(tidyr)
library(stringr)

scrap_file <- fromJSON("eurosai.json", flatten = T) %>%
  unnest(subject) %>%
  unnest(country) %>%
  unnest(link) %>%
  mutate(link = paste0("https://www.eurosai.org", link))

links_data <- scrap_file %>%
  group_by(title, country) %>%
  summarise(link = first(link)) %>%
  ungroup()

subjects_data <- scrap_file %>%
  group_by(title, country, subject) %>%
  summarise(link = first(link)) %>%
  ungroup()

openxlsx::write.xlsx(list(links_complete = scrap_file,
                          links_by_country = links_data,
                          links_by_subject = subjects_data), 
                     "links.xlsx")
