
import requests
from flask import jsonify

Base_URL = "https://world.openfoodfacts.org"


def fetch_barcode(barcode):
    url = f"{Base_URL}/api/v2/product/{barcode}.json"
    response= requests.get(url,timeout=10)
    data= response.json()

    if data.get('status') !=1:
        return jsonify('Product not found'),404
    
    product = data['product']
    return {
        'name': product.get('product_name') or 'unknown',
        'brand' : product.get('brands') or 'unknown',
        'barcode' :barcode
     }

def fetch_name(name,limit =5):
    url = f"{Base_URL}/cgi/search.pl"
    params = {
        "search_terms": name,
        "search_simple": 1,
        "json": 1,
        "page_size":limit,
    }
    response = requests.get(url, params=params, timeout=10)
    data = response.json()
 
    results = []
    for product in data.get("products", []):
        results.append({
            "name": product.get("product_name") or "Unknown product",
            "brand": product.get("brands") or "Unknown brand",
            "barcode": product.get("code") or "",
        })
    return results
 