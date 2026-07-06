# Stock Catalog System
 
A small Flask REST API for managing retail stock items, with real
product data pulled in from the **OpenFoodFacts API**. 
 
No database is used - all data is stored in memory in a Python list
while the server is running (this also means data resets every time
you restart `app.py`, which is expected).
 
## What it does
 
- Full CRUD (Create, Read, Update, Delete) for stock items
- Pulls real product info (name, brand) from OpenFoodFacts by
  barcode or by name search
- A command-line app (`cli.py`) that talks to the API like a real client
- A full automated test suite (`pytest`)

## API Endpoints
 
| Method | Endpoint                     | Description                              |
|--------|-------------------------------|-------------------------------------------|
| GET    | `/items`                       | List all items                           |
| GET    | `/items/<items_ID>`                  | Get one item                             |
| POST   | `/items`                       | Create a new item                        |
| PATCH  | `/items/<items_ID>`                  | Update fields on an item                 |
| DELETE | `/items/<items_ID>`                  | Delete an item                           |
| GET    | `/external/search?name=milk`   | Search OpenFoodFacts by name (preview)   |
| GET    | `/external/barcode/<code>`     | Look up one product by barcode (preview) |
| POST   | `/items/import/<barcode>`      | Fetch from OpenFoodFacts AND save it     |