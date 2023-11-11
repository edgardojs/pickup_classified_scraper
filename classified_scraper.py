#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as soup
import json

class ClassifiedScraper:
    def __init__(self, url):
        self.url = url
        self.data = []
        self.scraper()
        print("Script Finished!")

    # Extracting hrefs with AutoNumAnuncio in their content
    def has_autonumanuncio(self, content):
        return content and 'AutoNumAnuncio' in content

    def scraper(self, *args, **kwargs):
        try:
            headers = requests.utils.default_headers()
            headers.update({'User-Agent': 'Mozilla/5.0'})
            response = requests.get(self.url, headers=headers)
            page_soup = soup(response.content, "html.parser")

            # Find all <tr> tags with specified attributes
            tr_tags = page_soup.find_all('tr', align='center', valign='middle')

            for tr_tag in tr_tags:
                # Extract information from the <tr> tag or its children as needed
                item_data = {}
                a_title = tr_tag.find('span', class_='Tahoma15blacknound')
                if a_title:
                    print(a_title.text)
                    item_data['title'] = a_title.text.strip()

                a_price = tr_tag.find('span', class_='Tahoma14BrownNound')
                if a_price:
                    print(a_price.text)
                    item_data['price'] = a_price.text.strip()

                if 'title' in item_data and 'price' in item_data:

                    a_tag = tr_tag.find('a', href=lambda href: self.has_autonumanuncio(href))
                    if a_tag:
                        href = a_tag.get('href')
                        print(f"https://www.clasificadosonline.com{href}")
                        item_data['link'] = f'https://www.clasificadosonline.com{a_tag.get("href")}'

                    print("\n---\n")
                    self.data.append(item_data)


        except Exception as e:
            print("There was an error: ", e)
