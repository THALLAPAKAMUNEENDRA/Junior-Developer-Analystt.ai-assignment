#program:- for part - 2

import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    description = 'Not available'
    asin = 'Not available'
    product_description = 'Not available'
    manufacturer = 'Not available'

    # Scrape the necessary information from the product page
    title_element = soup.find('span', {'id': 'productTitle'})
    if title_element:
        description = title_element.text.strip()

    asin_element = soup.find('th', string='ASIN')
    if asin_element:
        asin = asin_element.find_next('td').text.strip()

    product_description_element = soup.find('div', {'id': 'productDescription'})
    if product_description_element:
        product_description = product_description_element.text.strip()

    manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
    if manufacturer_element:
        manufacturer = manufacturer_element.text.strip()

    product_details = {
        'Description': description,
        'ASIN': asin,
        'Product Description': product_description,
        'Manufacturer': manufacturer
    }

    return product_details

def scrape_product_urls():
    base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'
    total_pages = 10
    product_urls = []

    for page in range(1, total_pages+1):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        for product in products:
            product_link = product.find('a', {'class': 'a-link-normal a-text-normal'})
            if product_link and 'href' in product_link.attrs:
                product_url = 'https://www.amazon.in' + product_link['href']
                product_urls.append(product_url)

    all_product_details = []
    for url in product_urls:
        product_details = scrape_product_details(url)
        all_product_details.append(product_details)

    return all_product_details

def export_to_csv(data, filename):
    if not data:
        print("No product details found.")
        return

    keys = data[0].keys()

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Scrape product details from URLs
all_product_details = scrape_product_urls()

# Export data to CSV file
export_to_csv(all_product_details, 'product_details.csv')



'''
#output:-

No product details found.

'''