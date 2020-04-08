from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

destination_url = "https://www.worldometers.info/coronavirus/country/us/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
req = Request(url=destination_url, headers=headers)

uClient = urlopen(req)
page_html = uClient.read()
uClient.close()

# parse html 
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("table", {"class":"usa_table_countries"})

content = containers[0].tbody.contents

states = []

for item in content:
    if item != "\n":
        name = item.td.text.strip()
        cases = item.td.next_sibling.next_sibling.text.strip()
        deaths = item.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.strip()

        states.append([name, cases, deaths])

def getData(stateName):
    for state in states:
        if state[0] == stateName:
            return state[0], state[1], state[2]

