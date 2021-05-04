from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

def getwebinfo():
    destination_url = "https://www.worldometers.info/coronavirus/country/us/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    req = Request(url=destination_url, headers=headers)

    uClient = urlopen(req)
    page_html = uClient.read()
    uClient.close()

    # parse html 
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("table", {"class":"usa_table_countries"})
    total = page_soup.findAll("div", {"id":"maincounter-wrap"})

    return containers, total

def getTotal():
    _, total = getwebinfo()

    # main counts 
    total_cases = total[0].span.text.strip()
    total_death = total[1].span.text.strip()
    total_recovered = total[2].span.text.strip()

    return total_cases, total_death, total_recovered

def getData(stateName):
    containers, _ = getwebinfo()

    content = containers[0].tbody.contents
    states = []
    for item in content:
        if item != "\n":
            name = item.td.next_sibling.next_sibling.text.strip()
            cases = item.td.next_sibling.next_sibling.next_sibling.next_sibling.text.strip()
            if item.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.strip() == "":
                newcases = "+0"
            else:
                newcases = item.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.strip()
            deaths = item.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text.strip()

            states.append([name, cases, newcases, deaths])

    for state in states:
        if state[0] == stateName:
            return state[0], state[1], state[2], state[3]

getData("Mississippi")