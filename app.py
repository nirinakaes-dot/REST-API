from flask import Flask, jsonify, request

import store
import external_api


def create_app():
    app = Flask(__name__)

    ############################ HEALTH CHECK #################################

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({'message': 'Stock Catalog API is running.'}), 200

    ############################ GET METHOD #################################
    #####GET ALL ITEMS ####

    @app.route('/items', methods=['GET'])
    def get_items():
        return jsonify(store.get_all()), 200

    ###GET SPECIFIC ITEM#######
    @app.route('/items/<int:item_ID>', methods=['GET'])
    def get_item(item_ID):
        item = store.get_by_id(item_ID)
        if not item:
            return jsonify({'error': 'Item not found'}), 404
        return jsonify(item), 200

    ################################POST METHOD #####################################

    @app.route('/items', methods=['POST'])
    def create():
        data = request.get_json()
        if not data.get('name'):
            return jsonify({'error': 'Name is required'}), 400

        item = store.create(
            name=data.get('name'),
            brand=data.get('brand', 'Unknown'),
            price=data.get('price', 0.0),
            barcode=data.get('barcode')
        )

        return jsonify(item), 201

    ########################PATCH METHOD #####################################

    @app.route('/items/<int:item_ID>', methods=['PATCH'])
    def update(item_ID):
        data = request.get_json()

        item = store.get_by_id(item_ID)
        if not item:
            return jsonify({'error': 'Item does not exist'}), 404

        updated = store.update(item_ID, data)
        return jsonify(updated), 200

    ################################DELETE METHOD#############################

    @app.route('/items/<int:item_ID>', methods=['DELETE'])
    def delete(item_ID):
        item = store.get_by_id(item_ID)

        if not item:
            return jsonify({'error': 'The item does not exist'}), 404

        store.delete(item_ID)

        return jsonify({'message': f'item with ID: {item_ID} is successfully deleted'}), 200

    ############################ EXTERNAL API ROUTES #################################
    ##### SEARCH OPENFOODFACTS BY NAME (preview only, doesn't save) ####

    @app.route('/external/search', methods=['GET'])
    def external_search():
        name = request.args.get('name')
        if not name:
            return jsonify({'error': "Provide a '?name=' query parameter"}), 400

        results = external_api.fetch_by_name(name)
        return jsonify(results), 200

    ##### LOOK UP OPENFOODFACTS BY BARCODE (preview only, doesn't save) ####

    @app.route('/external/barcode/<barcode>', methods=['GET'])
    def external_barcode(barcode):
        result = external_api.fetch_by_barcode(barcode)
        if not result:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify(result), 200

    ##### FETCH FROM OPENFOODFACTS AND SAVE INTO OUR LIST ####

    @app.route('/items/import/<barcode>', methods=['POST'])
    def import_item(barcode):
        product = external_api.fetch_by_barcode(barcode)
        if not product:
            return jsonify({'error': 'Product not found on OpenFoodFacts'}), 404

        data = request.get_json(silent=True) or {}

        item = store.create(
            name=product['name'],
            brand=product['brand'],
            barcode=product['barcode'],
            price=data.get('price', 0.0)
        )
        return jsonify(item), 201

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)