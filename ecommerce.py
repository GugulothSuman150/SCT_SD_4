import requests
from bs4 import BeautifulSoup
import csv

# Function to extract product information from the URL
def extract_product_info(url):
    # Send HTTP request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract product information
    products = []
    for product in soup.find_all('div', class_='product'):
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        rating = product.find('div', class_='product-rating').text.strip()
        
        # Store the extracted information into a dictionary
        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })
    
    return products

# Function to write product information to CSV
def write_to_csv(products):
    with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == '__main__':
    
    url = 'https://www.flipkart.com/tyy/4io/~cs-gcxawvd1ly/pr?sid=tyy%2C4io&collection-tab-name=+vivo+T2+Pro+5G&param=8992&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTIwLDk5OSoiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJ2aXZvIFQyIFBybyA1ZyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdUNFJaTVpGRVdEWTciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19'
    
    # Extract product information
    products = extract_product_info(url)
    
    # Write product information to CSV file
    write_to_csv(products)
    
    print(f'Product information extracted and saved to products.csv')
