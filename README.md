# PropertyPalScanner
A web scraper designed to fetch property listings from the PropertyPal website, specifically targeting properties to rent in Belfast. It extracts details such as property addresses and prices and prepares the information to be sent to your personal email.


# Features
- Scrapes Property Listings: Fetches property listings from the PropertyPal website.
- Extracts Property Details: Obtains property links, addresses from image alt tags, and prices from property detail pages.
- Logs Information: Provides detailed logging for monitoring and debugging.
- Handles HTTP Restrictions: Mimics browser requests to bypass potential HTTP 403 restrictions.
  
# Prerequisites
- Python 3.x
- requests library
- beautifulsoup4 library

# Installation
1. Clone the repo
git clone https://github.com/AndrewH537/PropertyPalScanner.git

2. Install required libraries
pip install requests beautifulsoup4

Note: if you get any import errors, specifcally for requests and bs4 in scraper.py,
ensure pip is installed and up to date
pip install --upgrade pip

Make sure the correct Python interpreter is selected
Windows: Ctrl + Shift + P
Select required interpreter

To run the script run main.py
To run just the scraper run scraper.py


If you still get import errors for requests and bs4 you may need to run the following;
py -m pip install requests
py -m pip install bs4

# Schedule the program
For task schedule on windows:
1. Open Task manager
2. Create a new task
3. Set the trigger to repeat at the desired interval
4. Set the action to start a program and point it to your interpreter and main.py

For schedule on cron run:
crontab -e
0 * * * * /usr/bin/python3 /path/to/your/main.py

# Customisation
1. Change the targeted URL
Modify the url variable in scraper.py to target different locations or property types.

2. Modify Headers
You can adjust the headers dictionary in scraper.py if you need to mimic different browser requests or add additional headers.

3. Modify the HTML parsing code
   This code is set up specifically to parse through the code for PropertyPal as of 18/07/24. The html elements may be subject to change. If the code changes or you want to use this project to scrape similar websites with a different codebase then you can do so in the scrape_properties function in scraper.py.
You will need to visit that specific site, right-click on a property listing and select "Inspect" to open the Developer Tools. From there you can view the html elements of the site and search by class tag to find the contents you want to scrape.



