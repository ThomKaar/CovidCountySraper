import requests
from string import Template
from bs4 import BeautifulSoup
from helper import urls, parseInt
import datetime
import csv

def main():
    county_data_list = []
    for county in urls:
        # Making a GET request
        r = requests.get(county['url'])

        # print request object
        if r.status_code != 200:
            t = Template('request to $url failed')
            print(t.substitute({'url': county['url']}))
            return 1

        t = Template('Pull data for $county...')
        print(t.substitute({'county': county['countyName']}))
        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')
        countyDiv = soup.find('div', class_='zRzGke EA71Tc pym81b')
        casesDiv = countyDiv.find('div', class_='fNm5wd qs41qe')
        caseCount = parseInt(casesDiv.find('div', class_='UvMayb').text)
        newCases = parseInt(casesDiv.find('strong').text)

        deathsDiv = countyDiv.find('div', class_='fNm5wd ckqIZ')
        deathCount = parseInt(deathsDiv.find('div', class_='UvMayb').text)
        newDeaths = parseInt(deathsDiv.find('strong').text)

        date = datetime.datetime.now()


        d = {}
        d['County'] = county['countyName']
        d['Date'] = date
        d['Total Cases'] = caseCount
        d['New Cases'] = newCases
        d['Total Deaths'] = deathCount
        d['New Deaths'] = newDeaths
        county_data_list.append(d)
        # totalCases = casesDiv[0].find('div', class_='UvMayb')
    filename = 'CACountyCovidData.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['County', 'Date', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths'])
        w.writeheader()

        w.writerows(county_data_list)
    return 0
# Using the special variable
# __name__
if __name__=="__main__":
    main()