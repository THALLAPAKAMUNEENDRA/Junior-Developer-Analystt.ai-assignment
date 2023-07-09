#program :- for part-1

import requests
from bs4 import BeautifulSoup

def scrape_product_details(url):
    # Send GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_details = []
    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:
        product_url_element = product.find('a', {'class': 'a-link-normal a-text-normal'})
        product_url = product_url_element['href'] if product_url_element else 'Not available'

        product_name_element = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        product_name = product_name_element.text.strip() if product_name_element else 'Not available'

        price_element = product.find('span', {'class': 'a-offscreen'})
        product_price = price_element.text.strip() if price_element else 'Not available'

        rating_element = product.find('span', {'class': 'a-icon-alt'})
        rating = rating_element.text.strip() if rating_element else 'Not available'

        review_element = product.find('span', {'class': 'a-size-base'})
        review_count = review_element.text.strip() if review_element else '0'

        product_details.append({
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': rating,
            'Number of reviews': review_count
        })

    return product_details

# Scrape 20 pages of product listings
base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'
total_pages = 20

all_product_details = []
for page in range(1, total_pages+1):
    url = base_url.format(page)
    product_details = scrape_product_details(url)
    all_product_details.extend(product_details)

# Print the scraped product details
for product in all_product_details:
    print(product)

'''
output:-
{'Product URL': 'Not available', 'Product Name': 'Skybags Brat Black 46 Cms Casual Backpack', 'Product Price': '₹599', 'Rating': '4.1 out of 5 stars', 'Number of reviews': '5,013'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister 32 Ltrs Black Casual Backpack (AMT FIZZ SCH BAG 02 - BLACK)', 'Product Price': '₹1,199', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '55,194'}
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L (Blue & black)', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLACK LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,299', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '422'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon 35L Water Resistant 15.6 inch Laptop Bag for Men/Backpack for Men, Navy Blue | Office Bag for Men/Office Bag for Women with Padded Laptop Compartment | Rain Cover & Reflective Strips', 'Product Price': '₹649', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '16,390'} 
{'Product URL': 'Not available', 'Product Name': 'Gear Classic 20L Faux Leather Water Resistant Anti Theft Laptop Bag/Backpack for Men/Women-Brown', 'Product Price': '₹988', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,857'}
{'Product URL': 'Not available', 'Product Name': 'ADISA 15.6 inch Laptop Backpack Office Bag College Travel Back Pack 32 Ltrs (z-Navy Blue)', 'Product Price': '₹499', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '961'}
{'Product URL': 'Not available', 'Product Name': 'Gear Aspire 30L Water Restant Office Laptop Bag/Backpack for Men/Women/(Black)', 'Product Price': '₹1,085', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,780'}   
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'Fur Jaden 55 LTR Rucksack Travel Backpack Bag for Trekking, Hiking with Shoe Compartment', 'Product Price': '₹849', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '5,383'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon Large 37L Laptop Bag Backpack for menं Women Boys aand Girls Luggage Travel Bags with 17.3 inches Laptop Compartment & Rain Cover', 'Product Price': '₹849', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '3,081'}
{'Product URL': 'Not available', 'Product Name': 'SAFARI 15 Ltrs Sea Blue Casual/School/College Backpack (DAYPACKNEO15CBSEB)', 'Product Price': '₹248', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '19,776'}        
{'Product URL': 'Not available', 'Product Name': 'ADISA 32L Large Laptop Backpack Office Bag College Travel Back Pack with rain Cover (Grey)', 'Product Price': '₹599', 'Rating': '3.8 out of 5 stars', 'Number of reviews': '226'}
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLUE LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,399', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '427'}
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L, Charcoal black', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'Skybags Brat Black 46 Cms Casual Backpack', 'Product Price': '₹599', 'Rating': '4.1 out of 5 stars', 'Number of reviews': '5,013'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister 32 Ltrs Black Casual Backpack (AMT FIZZ SCH BAG 02 - BLACK)', 'Product Price': '₹1,199', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '55,194'}  
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L (Blue & black)', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLACK LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,299', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '422'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon 35L Water Resistant 15.6 inch Laptop Bag for Men/Backpack for Men, Navy Blue | Office Bag for Men/Office Bag for Women with Padded Laptop Compartment | Rain Cover & Reflective Strips', 'Product Price': '₹649', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '16,390'} 
{'Product URL': 'Not available', 'Product Name': 'Gear Classic 20L Faux Leather Water Resistant Anti Theft Laptop Bag/Backpack for Men/Women-Brown', 'Product Price': '₹988', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,857'}
{'Product URL': 'Not available', 'Product Name': 'ADISA 15.6 inch Laptop Backpack Office Bag College Travel Back Pack 32 Ltrs (z-Navy Blue)', 'Product Price': '₹499', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '961'}
{'Product URL': 'Not available', 'Product Name': 'Gear Aspire 30L Water Restant Office Laptop Bag/Backpack for Men/Women/(Black)', 'Product Price': '₹1,085', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,780'}   
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'Fur Jaden 55 LTR Rucksack Travel Backpack Bag for Trekking, Hiking with Shoe Compartment', 'Product Price': '₹849', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '5,383'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon Large 37L Laptop Bag Backpack for menं Women Boys aand Girls Luggage Travel Bags with 17.3 inches Laptop Compartment & Rain Cover', 'Product Price': '₹849', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '3,081'}
{'Product URL': 'Not available', 'Product Name': 'SAFARI 15 Ltrs Sea Blue Casual/School/College Backpack (DAYPACKNEO15CBSEB)', 'Product Price': '₹248', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '19,776'}        
{'Product URL': 'Not available', 'Product Name': 'ADISA 32L Large Laptop Backpack Office Bag College Travel Back Pack with rain Cover (Grey)', 'Product Price': '₹599', 'Rating': '3.8 out of 5 stars', 'Number of reviews': '226'}
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLUE LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,399', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '427'}
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L, Charcoal black', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'Skybags Brat Black 46 Cms Casual Backpack', 'Product Price': '₹599', 'Rating': '4.1 out of 5 stars', 'Number of reviews': '5,013'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister 32 Ltrs Black Casual Backpack (AMT FIZZ SCH BAG 02 - BLACK)', 'Product Price': '₹1,199', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '55,194'}  
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L (Blue & black)', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLACK LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,299', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '422'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon 35L Water Resistant 15.6 inch Laptop Bag for Men/Backpack for Men, Navy Blue | Office Bag for Men/Office Bag for Women with Padded Laptop Compartment | Rain Cover & Reflective Strips', 'Product Price': '₹649', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '16,390'} 
{'Product URL': 'Not available', 'Product Name': 'Gear Classic 20L Faux Leather Water Resistant Anti Theft Laptop Bag/Backpack for Men/Women-Brown', 'Product Price': '₹988', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,857'}
{'Product URL': 'Not available', 'Product Name': 'ADISA 15.6 inch Laptop Backpack Office Bag College Travel Back Pack 32 Ltrs (z-Navy Blue)', 'Product Price': '₹499', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '961'}
{'Product URL': 'Not available', 'Product Name': 'Gear Aspire 30L Water Restant Office Laptop Bag/Backpack for Men/Women/(Black)', 'Product Price': '₹1,085', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,780'}   
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'Fur Jaden 55 LTR Rucksack Travel Backpack Bag for Trekking, Hiking with Shoe Compartment', 'Product Price': '₹849', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '5,383'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon Large 37L Laptop Bag Backpack for menं Women Boys aand Girls Luggage Travel Bags with 17.3 inches Laptop Compartment & Rain Cover', 'Product Price': '₹849', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '3,081'}
{'Product URL': 'Not available', 'Product Name': 'SAFARI 15 Ltrs Sea Blue Casual/School/College Backpack (DAYPACKNEO15CBSEB)', 'Product Price': '₹248', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '19,776'}        
{'Product URL': 'Not available', 'Product Name': 'ADISA 32L Large Laptop Backpack Office Bag College Travel Back Pack with rain Cover (Grey)', 'Product Price': '₹599', 'Rating': '3.8 out of 5 stars', 'Number of reviews': '226'}
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLUE LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,399', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '427'}
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L, Charcoal black', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'Skybags Brat Black 46 Cms Casual Backpack', 'Product Price': '₹599', 'Rating': '4.1 out of 5 stars', 'Number of reviews': '5,013'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister 32 Ltrs Black Casual Backpack (AMT FIZZ SCH BAG 02 - BLACK)', 'Product Price': '₹1,199', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '55,194'}  
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L (Blue & black)', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLACK LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,299', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '422'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon 35L Water Resistant 15.6 inch Laptop Bag for Men/Backpack for Men, Navy Blue | Office Bag for Men/Office Bag for Women with Padded Laptop Compartment | Rain Cover & Reflective Strips', 'Product Price': '₹649', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '16,390'} 
{'Product URL': 'Not available', 'Product Name': 'Gear Classic 20L Faux Leather Water Resistant Anti Theft Laptop Bag/Backpack for Men/Women-Brown', 'Product Price': '₹988', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,857'}
{'Product URL': 'Not available', 'Product Name': 'ADISA 15.6 inch Laptop Backpack Office Bag College Travel Back Pack 32 Ltrs (z-Navy Blue)', 'Product Price': '₹499', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '961'}
{'Product URL': 'Not available', 'Product Name': 'Gear Aspire 30L Water Restant Office Laptop Bag/Backpack for Men/Women/(Black)', 'Product Price': '₹1,085', 'Rating': '4.4 out of 5 stars', 'Number of reviews': '5,780'}   
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'Fur Jaden 55 LTR Rucksack Travel Backpack Bag for Trekking, Hiking with Shoe Compartment', 'Product Price': '₹849', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '5,383'}
{'Product URL': 'Not available', 'Product Name': 'Half Moon Large 37L Laptop Bag Backpack for menं Women Boys aand Girls Luggage Travel Bags with 17.3 inches Laptop Compartment & Rain Cover', 'Product Price': '₹849', 'Rating': '3.9 out of 5 stars', 'Number of reviews': '3,081'}
{'Product URL': 'Not available', 'Product Name': 'SAFARI 15 Ltrs Sea Blue Casual/School/College Backpack (DAYPACKNEO15CBSEB)', 'Product Price': '₹248', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '19,776'}        
{'Product URL': 'Not available', 'Product Name': 'ADISA 32L Large Laptop Backpack Office Bag College Travel Back Pack with rain Cover (Grey)', 'Product Price': '₹599', 'Rating': '3.8 out of 5 stars', 'Number of reviews': '226'}
{'Product URL': 'Not available', 'Product Name': 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', 'Product Price': '₹679', 'Rating': '4.0 out of 5 stars', 'Number of reviews': '4,656'}
{'Product URL': 'Not available', 'Product Name': 'American Tourister VALEX BLUE LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', 'Product Price': '₹1,399', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '427'}
{'Product URL': 'Not available', 'Product Name': 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L, Charcoal black', 'Product Price': '₹550', 'Rating': '4.3 out of 5 stars', 'Number of reviews': '11,570'}
'''