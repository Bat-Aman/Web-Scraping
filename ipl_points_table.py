import requests
from bs4 import BeautifulSoup
import os
from prettytable import PrettyTable


def get_webpage(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    return soup

def points_table(soup):
    x = PrettyTable()
    x.field_names = ['Team', 'Played', 'Won', 'Lost', 'Tied', 'Points', 'NRR']
    title = soup.find(
        'h3', {'class': 'cb-mat-mnu-wrp cb-min-pad'}).text.replace(',', '')
    os.system('cls||clear')
    print("\n\t\t", "-" * 35, " | ", title, " | ", "-" * 35, "\n")
    table = soup.find('table', {'class': 'table cb-srs-pnts'})

    for rows in table.select('tbody tr'):
        if(rows.find_all('td', {'class': 'cb-srs-pnts-dwn'})):
            continue
        elif(rows.find_all('td', {'class': 'cb-srs-pnts-td'})):
            cells = rows.find_all('td')
            team = cells[0].text.strip()
            match = cells[1].text.strip()
            won = cells[2].text.strip()
            lost = cells[3].text.strip()
            tied = cells[4].text.strip()
            points = cells[6].text.strip()
            nrr = cells[7].text.strip()

            x.add_row([team, match, won, lost, tied, points, nrr])
        else:
            continue
    print(x)

def main():
    os.system('cls||clear')
    url = 'http://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/points-table'
    soup = get_webpage(url)
    points_table(soup)

if __name__ == "__main__":
  main()
