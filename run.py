#!/usr/bin/env python3
from classified_scraper import ClassifiedScraper
from json_handler import JsonHandler

def main():
    base_url = "https://clasificadosonline.com/UDTransListingADV.asp"
    marca = 0
    tipo_c = 12
    from_year = 1975
    to_year = 2010
    low_price = 999
    high_price = 3000
    key = ""

    # Construct the URL with variables
    url = (
        f"{base_url}?Marca={marca}&"
        f"TipoC={tipo_c}&"
        f"RESPueblos=%25&"
        f"FromYear={from_year}&"
        f"ToYear={to_year}&"
        f"LowPrice={low_price}&"
        f"HighPrice={high_price}&"
        f"Key={key}&"
        f"Submit2=Buscar&"
        f"IncPrecio=1&"
        f"AccessM=0"
    )
    json_handler = JsonHandler('pickup_data.json')
    scraper = ClassifiedScraper(url)

    # Update data in the main script
    json_handler.update_existing_data(scraper.data)

if __name__ == "__main__":
    main()
