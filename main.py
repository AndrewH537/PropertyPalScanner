from scraper import scrape_properties
from storage import load_previous_listings, save_listings, get_new_listings
from notifier import send_email
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levellevelname)s - %(message)s')

def main():
    logging.info("Starting property scraper.")
    
    current_listings = scrape_properties()
    logging.info(f"Scraped {len(current_listings)} properties: {current_listings}")
    
    previous_listings = load_previous_listings()
    logging.info(f"Loaded {len(previous_listings)} previous listings.")
    
    new_listings = get_new_listings(current_listings, previous_listings)
    logging.info(f"Found {len(new_listings)} new listings: {new_listings}")
    
    if new_listings:
        send_email(new_listings)
        save_listings(current_listings)
        logging.info("Email sent and current listings saved.")
    else:
        logging.info("No new listings found.")

if __name__ == "__main__":
    main()
