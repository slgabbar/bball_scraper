# Imports
import os, errno
from selenium import webdriver

# Specify Driver and load URL
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.basketball-reference.com/leagues/NBA_2018_per_game.html')

# Create the directory to put data
PATH = 'data/'
try:
    os.makedirs(path)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# Gets the raw csv content from bballref and stores in raw_csv as a string
raw_csv = driver.execute_script('''var x = document.getElementsByClassName("tooltip");
       x[3].click();
       var content = document.getElementById("csv_per_game_stats");
       return content.textContent;
       ''')

# Write CSV todisk
outfile = "2018_pergame.csv"
f = open(PATH+outfile, "w")
f.write(raw_csv)

print("Done.")