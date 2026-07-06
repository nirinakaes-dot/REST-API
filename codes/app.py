from flask import Flask, jsonify ,request

app = Flask(__name__)



############################ GET METHOD #################################
#####GET ALL ITEMS ####

app.route('/items',methods =['GET'])
def get_items():
    return jsonify(store.get_all()),200


###GET SPECIFIC ITEM#######
app.route('/items/<int:item_ID>', methods=['GET'])
def get_item(item_ID):
    item = store.get_by_ID(item_ID)
    if not item:
        return jsonify({'error':'Item not found'}),404
    return jsonify(item),200
   



################################POST METHOD #####################################

@app.route('/items',methods=['POST'])
def create():
    data = request.get_json()
    if not data.get('name'):
        return jsonify({'error':'Name is required'}),400
    
    item= store.create(
        name = data.get('name'),
        brand = data.get('brand','Unknown'),
        price = data.get('price',0.0),
        barcode= data.get('barcode')

    )

    return jsonify(item),201

########################PATCH METHOD #####################################

@app.route('/items/<int:item_ID>',methods=['PATCH'])

def update(item_ID):
    data = request.get_json()

    item= store.get_by_ID(item_ID)
    if not item:
        return jsonify({'error':'Item does not exist'}),404
    
    updated = store.update(item_ID,data)
    return jsonify(updated),200






################################DELETE METHOD#############################
@app.route('/items/<int:item_ID>',methods=['DELETE'])
def delete(item_ID):
    data = request.get_json()
    item = store.get_by_ID(item_ID)

    if not item:
        return jsonify({'error':'The item does not exist'}),404
    

    deleted = store.delete(item_ID)

    return jsonify(f'item with ID: {item_ID} is successfully deleted'),200






if __name__ == "__main__":
   app.run(debug=True)