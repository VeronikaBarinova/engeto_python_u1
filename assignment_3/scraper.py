"""
scraper_3.py: treti projekt do Engeto Online Python Akademie
author: Veronika Barinova
email: veronika.barina@gmail.com
discord: veronikabarinova_30716 (not use too much)
"""
import requests
from bs4 import BeautifulSoup
import csv
import sys
from typing import List

def get_town_data(url: str) -> List[dict]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    town_data = []

    print (f"STAHUJI DATA Z VYBRANEHO URL: {url}")
    for row in soup.find_all('td', class_='cislo'):
        link = row.find('a')
        if link and 'xvyber=' in link['href']:
            town = { 'code': list(link)[0], 'url': link['href'] }
            town_data.append(town)
    return town_data

def scrape_town_data(town:List[dict]) -> dict:
    response = requests.get(f"https://volby.cz/pls/ps2017nss/{town['url']}")
    
    soup = BeautifulSoup(response.content, 'html.parser')    

    obec_tag = soup.find('h3', string=lambda x: x and 'Obec:' in x)
    voters = soup.find_all('td', headers='sa2')[0].text.strip()
    envelopes = soup.find_all('td', headers='sa3')[0].text.strip()
    valid_votes = soup.find_all('td', headers='sa6')[0].text.strip()

    if obec_tag:
        town_name = obec_tag.text.split(': ')[1].strip()

    results = {
        'code': town['code'],
        'location': town_name,
        'registered': voters,
        'envelopes': envelopes,
        'valid': valid_votes,
    }

    rows = soup.find_all('tr')

    for row in rows:
        party_name_td = row.find('td', class_='overflow_name')
        if party_name_td:
            next_td = party_name_td.find_next_sibling('td')
            if next_td:
                party_name = party_name_td.text.strip()
                votes = next_td.text.strip()
                results[party_name] = votes

    return results

def save_to_csv(data, filename: str) -> None:
    if data:
        headers = list(data[0].keys())
        print(f"UKLADAM DATA DO SOUBORU: {filename}")
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

def dump_csv(filename:str , rows:int) -> None:
    with open(filename, 'r', encoding='utf-8') as file:        
        for _ in range(rows):
            print(file.readline().strip())

def main():
    if len(sys.argv) != 3:
        print("Usage: python scraper.py '<url>' <output_file.csv>")
        return
    else:
        url = sys.argv[1]
        output_file = sys.argv[2]
    
    town_data = get_town_data(url)
    all_data = []
    
    for town_url in town_data:
        town_data = scrape_town_data(town_url)
        
        all_data.append(town_data)
    
    save_to_csv(all_data, output_file)
    #nebylo soucasti zadani, tak pripadne staci zakomentovat tento radek
    dump_csv(output_file, 3)
    print(f"UKONCUJI {sys.argv[0]}")

if __name__ == "__main__":
    main()
