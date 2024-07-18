import logging
import requests
from bs4 import BeautifulSoup

def scrape_properties():
    logging.info("Scraping properties from website.")
    
    url = 'https://www.propertypal.com/property-to-rent/belfast/sort-dateHigh'
    
    # Add headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    
    response = requests.get(url, headers=headers)
    logging.info(f"HTTP GET request to {url} returned status code {response.status_code}")
    
    if response.status_code == 403:
        logging.error("Access forbidden: received HTTP 403 status code.")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Try to find the main div containing all properties
    properties_container = soup.find('div', class_='sc-8cd7a62a-0 dNMfIQ')
    
    if not properties_container:
        logging.warning("No properties container found on the page.")
        return []
    
    # Find the list containing property items
    properties_list = properties_container.find('ul', class_='sc-8cd7a62a-1 jlWBWF')
    
    if not properties_list:
        logging.warning("No properties list found within the container.")
        return []
    
    # Find all property list items
    property_items = properties_list.find_all('li', class_='sc-93204c6d-0 kdxPRe pp-property-box')
    
    logging.info(f"Found {len(property_items)} properties in the list.")
    
    property_details = []
    for property in property_items:
        link_tag = property.find('a', class_='sc-93204c6d-2 biKfxj')
        
        if link_tag and 'href' in link_tag.attrs:
            link = f"https://www.propertypal.com{link_tag['href']}"
            address = "No address available"
            price = "No price available"
            
            # Extract the address from the alt attribute of the img tag
            img_tag = property.find('img', class_='sc-e5645386-2 gCEYGU')
            if img_tag and 'alt' in img_tag.attrs:
                address = img_tag['alt'].replace(' photo', '').strip()
            
            # Navigate to the detailed property page to fetch additional information
            property_response = requests.get(link, headers=headers)
            property_soup = BeautifulSoup(property_response.text, 'html.parser')
            
            # Price is located within a span inside a p tag
            price_tag = property_soup.find('p', class_='sc-af42e648-0 dMZym pp-property-price')
            if price_tag:
                price = price_tag.get_text(strip=True)
                
            property_details.append({'address': address, 'price': price, 'link': link})
        else:
            logging.warning("No link found for a property.")
    
    return property_details

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    properties = scrape_properties()
    logging.info(f"Scraped properties: {properties}")
    print(f"Found properties: {properties}")
