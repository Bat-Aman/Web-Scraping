from bs4 import BeautifulSoup
import requests
import os

choice = {
    '1': 'english',
    '2': 'hindi',
    '3': 'gujarati',
    '4': 'punjabi'
}


def input_choice():
    for sno in choice:
        print(sno, ".", choice[sno])
    ch = input('Enter the choice number(1-4):\n>>>')
    return choice[ch]


def get_songs(lang):
    response = requests.get(
        'https://www.saavn.com/s/featured/' + lang + '/Weekly_Top_Songs')
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find('ol', {'class': 'content-list'})
    all_songs = data.find_all('div', {'class': 'details'})

    return all_songs


def print_songs(all_songs, lang):
    os.system('cls||clear')
    print("\n\t\t", "-" * 35, " | Top 30 ", lang,
          "songs this week | ", "-" * 35, "\n")
    for count, s in enumerate(all_songs, 1):
        song = s.find('p', {'class': 'song-name'}).text
        print(count, song)


def saavn_songs():
    lang = input_choice()
    all_songs = get_songs(lang)
    print_songs(all_songs, lang)


saavn_songs()
