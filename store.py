

items = []    
next_id = 1     


def reset():
    global items, next_id
    items = []
    next_id = 1


def get_all():
    return items


def get_by_id(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None


def create(name, brand="Unknown", barcode=None, quantity=0, price=0.0):
    global next_id
    item = {
        "id": next_id,
        "name": name,
        "brand": brand,
        "barcode": barcode,
        "price": price,
    }
    items.append(item)
    next_id += 1
    return item


def update(item_id, fields):
    item = get_by_id(item_id)
    if not item:
        return None

    allowed = {"name", "brand", "barcode", "price"}
    for key, value in fields.items():
        if key in allowed:
            item[key] = value
    return item


def delete(item_id):
    item = get_by_id(item_id)
    if item:
        items.remove(item)
        return True
    return False