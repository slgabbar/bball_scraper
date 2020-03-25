# Imports
import selenium
from selenium import webdriver

# Specify Driver and load URL
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.basketball-reference.com/leagues/NBA_2018_per_game.html')

raw_csv = driver.execute_script('''var x = document.getElementsByClassName("tooltip");
       x[3].click();
       var content = document.getElementById("csv_per_game_stats");
       return content.textContent;
       ''')

print(raw_csv)

