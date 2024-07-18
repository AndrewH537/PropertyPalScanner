import logging
import os
import json

def load_previous_listings(filepath='listings.json'):
    logging.info(f"Loading previous listings from {filepath}.")
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    return []

def save_listings(listings, filepath='listings.json'):
    logging.info(f"Saving current listings to {filepath}.")
    
    with open(filepath, 'w') as file:
        json.dump(listings, file)

def get_new_listings(current_listings, previous_listings):
    logging.info("Comparing current listings with previous listings.")
    return [listing for listing in current_listings if listing not in previous_listings]
