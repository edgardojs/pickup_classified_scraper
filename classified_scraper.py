import requests
from bs4 import BeautifulSoup as soup

class ClassifiedScraper:
    def __init__(self, url):
        self.url = url
        self.scraper()
        print("Script Finished!")

    def scraper(self, *args, **kwargs):
        try:
            headers = requests.utils.default_headers()
            headers.update({'User-Agent': 'Mozilla/5.0'})

            response = requests.get(self.url, headers=headers)
            page_soup = soup(response.content, "html.parser")
            # You can continue with parsing the page_soup and extracting the data you need here.
            print(page_soup)

        except Exception as e:
            print("There was an error: ", e)

def main():
    url = "https://clasificadosonline.com/UDTransListingADV.asp?Marca=0&TipoC=12&RESPueblos=%25&FromYear=0&ToYear=2024&LowPrice=999&HighPrice=3000&Key=&Submit2=Buscar&IncPrecio=1&AccessM=0"
    scraper = ClassifiedScraper(url)

if __name__ == "__main__":
    main()
