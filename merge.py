# Very simple script to merge all separate data csv's into one big one

import pandas as pd
import gc

str_adv = 'data/{year}_advanced.csv'
str_reg = 'data/{year}_per_game.csv'

adv_list = []
reg_list = []
for year in range(1990,2020):
    data_adv = str_adv.format(year=year)
    data_reg = str_reg.format(year=year)
    a_df = pd.read_csv(data_adv)
    r_df = pd.read_csv(data_reg)

    # Add season to DF
    a_df['Season'] = year
    r_df['Season'] = year
    adv_list.append(a_df)
    reg_list.append(r_df)

    del(a_df)
    del(r_df)
    gc.collect()

# Clean up advanced df's
df = pd.concat(adv_list)
df = df.drop('Rk', axis=1)
df.reset_index(drop=True)
df = df.dropna(how='all', axis='columns')
df.to_csv("data/advanced.csv", index=False)
print("advanced merge done")

# Clean up regular df's
df = pd.concat(reg_list)
df = df.drop('Rk', axis=1)
df.reset_index(drop=True)
df.to_csv("data/per_game.csv", index=False)
print("per_game merge done")


