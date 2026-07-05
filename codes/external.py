
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

