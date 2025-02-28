import requests
from bs4 import BeautifulSoup

# Base URL for the Toyota listings (pagination will be handled with page numbers)
base_url = 'https://www.autotrader.com/cars-for-sale/All-Cars/Honda'

# Loop through the first three pages
for page_num in range(1, 4):  # Loop for pages 1, 2, and 3
    print(f"\nScraping page {page_num}...\n")
    
    # Construct the URL for the current page
    url = f"{base_url}?page={page_num}"
    
    # Send a request to the current page URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all car listings (look for <h2> tags with the specific class for car names)
        listings = soup.find_all('h2', class_='text-bold text-size-400 link-unstyled')
        
        # Loop through each listing and extract car title and price
        if listings:
            print(f"Found {len(listings)} listings on page {page_num}:\n")
            for listing in listings:
                # Get the car title
                title = listing.get_text(strip=True)
                
                # Find the price associated with the car (inside the <div> tag with the price class)
                price = listing.find_next('div', class_='text-size-500 text-ultra-bold first-price')
                if price:
                    price = price.get_text(strip=True)  # Get the price text
                else:
                    price = 'Price not listed'  # If no price is found, use a fallback text
                
                # Print the car title and price
                print(f"Car: {title} - Price: {price}")
        else:
            print(f"No listings found on page {page_num}.")
    else:
        print(f"Failed to retrieve page {page_num}. Status code: {response.status_code}")