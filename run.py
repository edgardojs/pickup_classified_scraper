#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

from classified_scraper import ClassifiedScraper
from json_handler import JsonHandler
from mailer import EmailSender


def main():
    # load environment variables from .env file
    load_dotenv()
    GOOGLE_PASSWORD = os.environ.get("GOOGLE_PASSWORD")
    PERSONAL_EMAIL = os.environ.get("PERSONAL_EMAIL")

    # URL Variables

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

    # Run the Scraper
    json_handler = JsonHandler('pickup_data.json')
    scraper = ClassifiedScraper(url)

    # Update data in the main script
    json_handler.update_existing_data(scraper.data)

    # Load the data from pickup_data.json
    all_data = json_handler.load_data()

    # Filter items from the last 24 hours
    yesterday = datetime.now() - timedelta(days=1)
    recent_items = [item for item in all_data if datetime.fromisoformat(item['timestamp']) > yesterday]

    # Send the email
    subject = "Yesterday's Pickup Data"
    body = "Here are the items from yesterday:\n\n"

    for item in recent_items:
        body += f"Title: {item['title']}\nPrice: {item['price']}\nLink: {item['link']}\n\n"

    sender = PERSONAL_EMAIL
    recipients = [PERSONAL_EMAIL]
    password = GOOGLE_PASSWORD
    esender = EmailSender()
    esender.send_email(subject, body, sender, recipients, password)

if __name__ == "__main__":
    main()
