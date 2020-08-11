# Simple r script, fill in missing data in advanced and per_game data
# merge togethjer into one data file so we can run feature analysis on all features

# Load the tidyverse library
library(tidyverse)

# Read in two files from disk
adv <- read.csv("/Users/samgabbard/Desktop/bball_scraper/data/advanced.csv")
prg <- read.csv("/Users/samgabbard/Desktop/bball_scraper/data/per_game.csv")


# Fill in all missing values with 0 for both DF's
adv[is.na(adv)] <- 0
prg[is.na(prg)] <- 0

# Merge the advanced data and regular season data together
all_data <- inner_join(adv, prg, by=c("Player"="Player", "Season"="Season", "Tm"="Tm",
                                      "Pos"="Pos", "Age"="Age", "G"="G", "All_NBA"="All_NBA"))

# Clean up the column names of all_data
all_data <- all_data %>% rename(
  TOT_MIN=MP.x, TS_P=TS., ORB_P=ORB., DRB_P=DRB., TRB_P=TRB., AST_P=AST., STL_P=STL., BLK_P=BLK., TOV_P=TOV.,
  USG_P=USG., WS_48=WS.48, MPG=MP.y, FG_P=FG., X3P_P=X3P., X2P_P=X2P., eFG_P=eFG., FT_P=FT.,)
