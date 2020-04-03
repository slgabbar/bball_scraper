# Imports
import os, errno
from selenium import webdriver

def scrape_bball_stats(type, year_start, year_end, savedir):
    temp_url = "https://www.basketball-reference.com/leagues/NBA_{season}_{type}.html"
    for year in range(year_start, year_end+1):

        # define the url from season and type
        url = temp_url.format(season=year, type=type)

        # Load the url
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get(url)

        # define some variable to help with scraping
        partial_table = '{type}_stats_toggle_partial_table'.format(type=type)
        csv_content = 'csv_{type}_stats'.format(type=type)

        # Hide partial rows so players who have played for multiple teams in one season
        # do not show up twice.
        driver.execute_script('document.getElementById("'+ partial_table +'").click();')

        # Gets the raw csv content from bballref and stores in raw_csv as a string
        raw_csv = driver.execute_script('''var x = document.getElementsByClassName("tooltip");
               x[3].click();
               var content = document.getElementById("'''+csv_content+'''");
               return content.textContent;
               ''')

        # Create dir if not already there
        # PATH = 'data/{season}_season/'.format(season=year)
        PATH = savedir
        try:
            os.makedirs(PATH)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


        # Write CSV todisk
        # filename = "{season}_{type}.csv".format(season=year, type=type)

        filename = str(year) + "_" + type + ".csv"

        f = open(PATH+filename, "w")
        f.write(raw_csv)

        print("Finished {season}_{type}".format(season=year, type=type))

def scrape_all_nba(savedir, filename):
    url = "https://www.basketball-reference.com/awards/all_league.html"

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(url)

    csv_content = "csv_awards_all_league"

    raw_csv = driver.execute_script('''var x = document.getElementsByClassName("tooltip");
                   x[3].click();
                   var content = document.getElementById("''' + csv_content + '''");
                   return content.textContent;
                   ''')

    # Create dir if not already there
    # PATH = 'data/{season}_season/'.format(season=year)
    PATH = savedir
    try:
        os.makedirs(PATH)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # Write CSV todisk
    # filename = "{season}_{type}.csv".format(season=year, type=type)
    f = open(PATH + filename, "w")
    f.write(raw_csv)

    print("Finished scarping All-NBA teams")

# Scrape basketball data statistics over range of years
# Per_game, per_minute, per_poss, advance
scrape_bball_stats('per_game', 1990, 2019, 'data/')
# scrape_bball_stats('per_minute', 1990, 2019, 'data/')
# scrape_bball_stats('per_poss', 1990, 2019, 'data/')
scrape_bball_stats('advanced', 1990, 2019, 'data/')

# Scrape all-nba teams
scrape_all_nba('data/', 'all_nba_teams.csv')
