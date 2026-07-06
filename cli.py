import requests
 
BASE_URL = "http://127.0.0.1:5000"
 
 
def list_items():
    response = requests.get(f"{BASE_URL}/items")
    items = response.json()
    if not items:
        print("No items yet.")
    for item in items:
        print(f"  [{item['id']}] {item['name']} | {item['brand']} | "
              f" price: {item['price']}")
 
 
def add_item():
    name = input("Name: ")
    brand = input("Brand: ")
    price = input("Price: ") or 0.0
 
    payload = {
        "name": name,
        "brand": brand,
        "price": float(price),
    }
    response = requests.post(f"{BASE_URL}/items", json=payload)
    print("Created:", response.json())
 
 
def update_item():
    item_id = input("ID of item to update: ")
    field = input("Field to change (name/brand/price): ")
    value = input("New value: ")
 
    if field in ("price"):
       value = float(value)

    payload = {field: value}
    response = requests.patch(f"{BASE_URL}/items/{item_id}", json=payload)
    print("Updated:", response.json())
 
 
def delete_item():
    item_id = input("ID of item to delete: ")
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    print(response.json())
 
 
def search_external():
    name = input("Search OpenFoodFacts for product name: ")
    response = requests.get(f"{BASE_URL}/external/search", params={"name": name})
    results = response.json()
    for i, product in enumerate(results):
        print(f"  {i + 1}. {product['name']} ({product['brand']}) "
              f"barcode: {product['barcode']}")
 
 
def import_by_barcode():
    barcode = input("Barcode to import: ")
    price = input("Price: ") or 0.0
 
    payload = { "price": float(price)}
    response = requests.post(f"{BASE_URL}/items/import/{barcode}", json=payload)
    print("Imported:", response.json())
 
 
MENU = """
==== Stock Catalog CLI ====
1. List all items
2. Add a new item manually
3. Update an item
4. Delete an item
5. Search OpenFoodFacts by name
6. Import an item from OpenFoodFacts by barcode
0. Exit
"""
 
ACTIONS = {
    "1": list_items,
    "2": add_item,
    "3": update_item,
    "4": delete_item,
    "5": search_external,
    "6": import_by_barcode,
}
 
 
def main():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")
 
 
if __name__ == "__main__":
    main()
 