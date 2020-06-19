# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set url you want to scrape
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the url
response = requests.get(url) 
print(response) #200 means it went through

#Parse HTML through the url and save it as BS object
soup = BeautifulSoup(response.text, "html.parser")

#Locate all 'a' tags
soup.find_all('a')

#Take a look to the first data file
one_a_tag = soup.find_all('a')[37]

link = one_a_tag['href']

#download all files

line_count = 1

for one_a_tag in soup.find_all('a'):
    if line_count >= 37:
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/' + link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
        time.sleep(1)
    line_count +=1