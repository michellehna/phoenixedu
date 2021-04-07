# This file controls the webscraping to get the ranking data from the ranking website

from bs4 import BeautifulSoup
import requests

url = "https://www.webometrics.info/en/asia/singapore%20"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

listofschools = []

toRanking = soup.find('tbody')
toRow     = toRanking.find('tr')

while toRow != None:
    school = {}
    school['LocalRanking']   = toRow.td.center.text
    school['WorldRanking']   = toRow.td.next_sibling.center.text
    school['Name']           = toRow.td.next_sibling.next_sibling.a.text
    school['Website']        = toRow.td.next_sibling.next_sibling.a['href']
    school['ImpactRank']     = toRow.td.next_sibling.next_sibling.next_sibling.next_sibling.center.text
    school['OpennessRank']   = toRow.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.center.text
    school['ExcellenceRank'] = toRow.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.center.text
    listofschools.append(school)
    toRow = toRow.find_next('tr')