# Inventory Management System — Flask REST API

A Flask REST API for a retail inventory management admin portal, built for
the *Python REST API with Flask* summative lab. Supports full CRUD on
inventory items and pulls product details (name, brand, ingredients, image)
from the **OpenFoodFacts API** by barcode or name search.

## Project overview (Task 1: The Problem)

Employees need to add, view, edit, and delete inventory items without
manually typing in every product detail. Since OpenFoodFacts already has
product data for millions of barcodes, the app lets an employee type/scan a
barcode and auto-fills the product name, brand, and ingredients — they only
need to add store-specific info (quantity, price).

## Design (Task 2)

**Mock database:** an in-memory Python list of dicts (`data_store.py`), as
specified in the lab. Each item gets an auto-incrementing `id`. Data resets
when the server restarts — there's no persistence layer, matching the "mock
database in an array" requirement.

**Routes:**

| Route | Method | Input | Output | Effect |
|---|---|---|---|---|
| `/inventory` | GET | — | list of items | none (read) |
| `/inventory/<id>` | GET | — | one item | none (read) |
| `/inventory` | POST | `product_name` + fields, **or** `barcode` + `quantity`/`price` | created item | adds to array |
| `/inventory/<id>` | PATCH | any subset of fields | updated item | mutates array |
| `/inventory/<id>` | DELETE | — | 204 No Content | removes from array |
| `/products/lookup/<barcode>` | GET | — | product preview | none (external API only) |
| `/products/search?q=` | GET | search term | list of product previews | none (external API only) |

The two `/products/...` routes never touch the inventory array — they're
previews. `POST /inventory` is the route that's triggered from the CLI's
"Add item by barcode" option, and is what actually saves an external lookup
into the mock database.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API (Task 3)

```bash
python app.py
```

Server runs at **http://127.0.0.1:5000**.

## Using the CLI

In a second terminal (server must be running):

```bash
python cli.py
```

Menu-driven interface: list inventory, view an item, add an item manually,
add an item by barcode (fetches from OpenFoodFacts), search OpenFoodFacts by
name, update an item, delete an item.

## Example requests

Add an item by barcode:
```bash
curl -X POST http://127.0.0.1:5000/inventory \
  -H "Content-Type: application/json" \
  -d '{"barcode": "3017620422003", "quantity": 10, "price": 3.49}'
```

Update quantity:
```bash
curl -X PATCH http://127.0.0.1:5000/inventory/1 \
  -H "Content-Type: application/json" \
  -d '{"quantity": 8}'
```

Delete an item:
```bash
curl -X DELETE http://127.0.0.1:5000/inventory/1
```

## Testing (Task 4)

```bash
pytest -v
```

17 tests covering:
- Every CRUD route (`tests/test_inventory_crud.py`) — create, read, update,
  delete, plus 404/400 error cases.
- External API integration (`tests/test_external_api.py`) — barcode lookup,
  name search, and "create by barcode" flow, all with OpenFoodFacts calls
  **mocked** (via `pytest-mock`) so tests run offline and don't depend on the
  real API being up.

## Project structure

```
inventory-lab/
├── app.py                    # Flask app: CRUD + external API routes
├── data_store.py              # Mock database (in-memory array)
├── off_client.py               # OpenFoodFacts API wrapper
├── cli.py                       # CLI that talks to the running API
├── requirements.txt
├── tests/
│   ├── conftest.py            # Test client + mock fixtures
│   ├── test_inventory_crud.py # CRUD route tests
│   └── test_external_api.py   # External API integration tests
└── README.md
```

## Git workflow (Task 5 / submission)

Suggested branching for the "Excelled" git-management rubric row:

```bash
git init
git checkout -b feature/crud-routes        # build app.py CRUD + data_store.py
# commit, then merge back to main via PR

git checkout -b feature/external-api       # build off_client.py + /products routes
# commit, then merge back to main via PR

git checkout -b feature/cli                # build cli.py
# commit, then merge back to main via PR

git checkout -b feature/tests              # build tests/
# commit, then merge back to main via PR
```

Delete each feature branch after merging. Push `main` to GitHub and submit
that repo URL.

## Notes / possible extensions

- **Persistence**: swap `data_store.py`'s in-memory list for SQLite/SQLAlchemy
  if you want data to survive restarts — the route logic in `app.py` wouldn't
  need to change much.
- **Auth**: currently open, no login — fine for a lab/admin-only tool, but
  add auth before deploying anywhere real.
- **Validation**: request bodies are checked minimally; consider
  `marshmallow` schemas for stricter validation as a stretch goal.