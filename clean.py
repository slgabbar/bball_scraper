# Very simple script to clean the player names in our data:
#
# Ex. 'LeBron James\jamesle01' -> 'Lebron James'
# Ex. 'Lebron James F'         -> 'Lebron James'

import pandas as pd
import gc


# Clean the names from advanced and per game data
def clean_stats(name):
    if '*' in name:
        # Account for older years where some players had '*"
        # 'Larry Bird*\birdla01'
        sep = '*'
    else:
        sep = '\\'
    name = name.split(sep, 1)[0]
    return name


for year in range (1990, 2020):
    print("Cleaning stats from " + str(year) + "...")
    adv_csv = str(year) + "_advanced.csv"
    pgm_csv = str(year) + "_per_game.csv"

    adv_df = pd.read_csv('data/' + adv_csv)
    pgm_df = pd.read_csv('data/' + pgm_csv)

    adv_df['Player'] = adv_df['Player'].apply(clean_stats)
    pgm_df['Player'] = pgm_df['Player'].apply(clean_stats)

    # Ovverwrite back to disk
    adv_df.to_csv('data/' + adv_csv, index=False)
    pgm_df.to_csv('data/' + pgm_csv, index=False)

    # Delete and Garbage Collect
    del(adv_df)
    del(pgm_df)
    gc.collect()

# Clean all_nba_teams as well
print("Cleaning all nba teams...")

df = pd.read_csv("data/all_nba_teams.csv")

# 177 because after that row the players dont have positions and dont need to be cleane
for i in range(0, 177):
    df.iloc[i][3] = df.iloc[i][3][:-2]
    df.iloc[i][4] = df.iloc[i][4][:-2]
    df.iloc[i][5] = df.iloc[i][5][:-2]
    df.iloc[i][6] = df.iloc[i][6][:-2]
    df.iloc[i][7] = df.iloc[i][7][:-2]

df.to_csv('data/all_nba_teams.csv', index=False)


print("Done")






