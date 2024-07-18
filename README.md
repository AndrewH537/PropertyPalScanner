# PropertyPalScanner
A web scraper designed to fetch property listings from the PropertyPal website, specifically targeting properties to rent in Belfast. It extracts details such as property addresses and prices and prepares the information to be sent to your personal email. The idea is to run it every hour and compare values to email any new properties that are posted.


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
```
git clone https://github.com/AndrewH537/PropertyPalScanner.git
```

2. Install required libraries
```
pip install requests beautifulsoup4
```

Note: if you get any import errors, specifcally for requests and bs4 in scraper.py,

ensure pip is installed and up to date

```
pip install --upgrade pip
```

Make sure the correct Python interpreter is selected

Windows: Ctrl + Shift + P

Select required interpreter

To run the script run main.py

To run just the scraper run scraper.py


If you still get import errors for requests and bs4 you may need to run the following;

```
py -m pip install requests
```

```
py -m pip install bs4
```

# Schedule the program
For task schedule on windows:

1. Create a batch file

Create a batch file that will run your Python script. This batch file will be used by Task Scheduler.

Open a text editor (e.g., Notepad).

Add the following lines, replacing the paths with the actual paths to your Python executable and main.py script:

```
@echo off
cd C:\path\to\your\script
C:\path\to\your\python\python.exe scraper.py
```

2. Open Task Scheduler using `Win + R`, type `taskschd.msc`

3. Create a new task

4. General tab -

Name: Provide a name for your task, such as "Property Scraper".

Description: Optionally, provide a description.

Check "Run whether user is logged on or not".

Check "Run with highest privileges".

5. Triggers Tab

Click on New....

Begin the task: On a schedule.

Settings: Daily.

Repeat task every: 1 hour for a duration of: Indefinitely.

Ensure "Enabled" is checked.

Click OK.

6. Actions Tab

Click on New....

Action: Start a program.

Program/script: Click Browse... and navigate to the batch file you created (run_scanner.bat).

Click OK.

7. Settings Tab:

Ensure "Allow task to be run on demand" and "Run task as soon as possible after a scheduled start is missed" are checked.
Optionally, configure additional settings like stopping the task if it runs longer than a certain duration.
Click OK.

8. Enter Credentials




# Customisation
1. Change the targeted URL
Modify the url variable in scraper.py to target different locations or property types.

2. Modify Headers
You can adjust the headers dictionary in scraper.py if you need to mimic different browser requests or add additional headers.

3. Modify the HTML parsing code
   This code is set up specifically to parse through the code for PropertyPal as of 18/07/24. The html elements may be subject to change. If the code changes or you want to use this project to scrape similar websites with a different codebase then you can do so in the scrape_properties function in scraper.py.
You will need to visit that specific site, right-click on a property listing and select "Inspect" to open the Developer Tools. From there you can view the html elements of the site and search by class tag to find the contents you want to scrape.



