




import requests

http = "https://prothomalo.com"
urldata = requests.get(http)

print(urldata.text)


<!----------------------------------------------------------------------------------


import requests
import bs4

http = "http://dotinternetbd.com"

urldata = requests.get(http)
bsoup = bs4.BeautifulSoup(urldata.text, 'lxml')

print(bsoup.prettify())


<!----------------------------------------------------------------------------------

import requests
import bs4

http = "https://www.mycodingzone.net/blog/english"

urldata = requests.get(http)
bsoup = bs4.BeautifulSoup(urldata.text, 'html.parser')

for pgraph in bsoup.find_all('p'):
    print(pgraph.text)

<!----------------------------------------------------------------------------------

import requests, webbrowser
from bs4 import  BeautifulSoup

user_input = input('Enter your text : ')
print('Searching .. . ')

google_url = "https://www.google.com/search?q="
google_search = requests.get(google_url+user_input)

bsoup = BeautifulSoup(google_search.text, 'lxml')
print(bsoup.prettify())


	...continue
	

<!----------------------------------------------------------------------------------