#Import all the libraries
import json
from veryfi import Client
import re
import os

#Veryfi Key
client_id = 'vrfrjXmXbzAeT8CTZc9FpAVCukL03MVfRlBz9cL'
client_secret = 'dW5Pul4JTCfhvB0kT7vWVsKlkRiFeEiXEwJUJea62Pojlo8mB9unGcmHMVl4cBtUZglTkogcmooZii8GT4MhEECTpborGfIAY7hwonCMXS7HcXnX4lK2uOM662tsgjDR'
username = 'michell.castrillon15'
api_key = '87c54d3c65d4ac9f34a6daac5c9ca625'

#List of categories for veryfi to choose the right category for this document
categories = ['Grocery', 'Utilities', 'Travel','Job Supplies and materials']

#Function to reuse code for each file
def annotations(file_path):
    #File path used to extract the annotation
    file_path = f'{file_path}'

    # Instantiate the client
    veryfi_client = Client(client_id, client_secret, username, api_key)

    # call the process document API and we pass our categories and filepath
    response = veryfi_client.process_document(file_path, categories=categories)

    # Data to use
    data = str(response)

    # Vendor Information
    # Vendor name
    pattern_vendor_name = r"'vendor':\s*{[^}]*'name':\s*'([^']+)"
    vendor_name = re.findall(pattern_vendor_name, data)

    # vendor address
    pattern_vendor_address = r"'vendor':\s*{[^}]*'address':\s*'([^']+)"
    vendor_address = re.findall(pattern_vendor_address, data)

    # Bill to name
    pattern_bill_to_name = r"'bill_to':\s*{[^}]*'name':\s*'([^']+)"
    bill_to_name = re.findall(pattern_bill_to_name, data)

    # Invoice Number
    pattern_invoice_number = r"'invoice_number':\s'([^']+)"
    invoice_number = re.findall(pattern_invoice_number, data)

    # Date
    pattern_date = r"'date':\s'([^' ]+)"
    date = re.findall(pattern_date, data)

    # For each line item
    # Sku
    pattern_product_sku = r"'sku':\s*([^', ]*)"
    product_sku = re.findall(pattern_product_sku, data)

    # Product description
    pattern_product_description = r"'description':\s*'([^']+)"
    product_description = re.findall(pattern_product_description, data)

    # Product quantity
    pattern_product_quantity = r"'quantity':\s*([^', ]+)"
    product_quantity = re.findall(pattern_product_quantity, data)

    # Product tax rate
    pattern_product_tax_rate = r"'tax_rate':\s*([^', ]*)"
    product_tax_rate = re.findall(pattern_product_tax_rate, data)

    # Product price
    pattern_product_price = r"'price':\s*([^', ]+)"
    product_price = re.findall(pattern_product_price, data)

    # Total
    pattern_product_total = r"'total':\s*([^', ]+)"
    product_total = re.findall(pattern_product_total, data)

    # Adding all the information in a new dictionary
    # Creating a new dictionary under ocr_text
    new_dictionary = {}
    for key in response:
        new_dictionary[key] = response[key]
        if key == 'ocr_text':
            break

    # Adding the new information
    new_dictionary["annotations"] = {
        "vendor_data": {
            "vendor_name": vendor_name,
            "vendor_address": vendor_address,
            "bill_to_name": bill_to_name,
            "invoice_number": invoice_number
        }
    }

    # Create a new dictionary with the product information
    products = {}
    for i in range(len(product_sku)):
        item_key = f"item{i + 1}"
        products[item_key] = {
            "sku": product_sku[i],
            "description": product_description[i],
            "quzntity": product_quantity[i],
            "tax_rate": product_tax_rate[i],
            "price": product_price[i],
            "total": product_total[i]
        }
    # Saving the product dictionary into the new_dictionary
    new_dictionary["annotations"]["products_description"] = products

    # Extracting file name
    file_name = new_string = re.findall(r'([^/]+)\.[^.]+$', file_path)

    # Creating the new JSON file
    json_file = f"processed/{file_name[0]}.json"
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(new_dictionary, file, indent=4, ensure_ascii=False)


#For each file on the folder
folder_path = 'files/'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    annotations(file_path)