import sys
from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup

#  Making the url
username = input("Enter the UserName: ")
my_url = 'https://twitter.com/' + username
uClient = uRequest(my_url)
soup = BeautifulSoup(uClient, "html.parser")

s1 = soup.title.text
print("\n\n\t\t\t-----------------------------Twitter Card----------------------------------")
print("\n\t\t\t\t\tUsername: @" + username)
print("\t\t\t\t\tName: " + s1.partition("(")[0])

bio = soup.find('div', {"class": "ProfileHeaderCard"}).find(
    'p', {"class": "ProfileHeaderCard-bio u-dir"}).text
bio = bio.replace('\n', '-')
print("\t\t\t\t\tBio: " + bio)

location = soup.find('div', {"class": "ProfileHeaderCard-location"}).find(
    'span', {"class": "ProfileHeaderCard-locationText u-dir"}).text
location = location.replace('\n', '')
print("\t\t\t\t\tLocation: " + location)

joining_date = soup.find('div', {"class": "ProfileHeaderCard-joinDate"}).find(
    'span', {"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"}).text
print("\t\t\t\t\tJoining Date: " + joining_date)

dob = soup.find('div', {"class": "ProfileHeaderCard-birthdate"}).find(
    'span', {"class": "ProfileHeaderCard-birthdateText u-dir"}).text
dob = dob.replace('\n', '')
print("\t\t\t\t\tDate of Birth: " + dob)

print("\n\n\t\t\t-----------------------------Recent Tweets----------------------------------\n\n")
for tweets in soup.findAll('div', {"class": "content"}):
    tweet = tweets.find('p', {"class": "TweetTextSize--normal"}).text
    tweet = tweet.replace('\n', '    ')
    print("->  " + tweet)
