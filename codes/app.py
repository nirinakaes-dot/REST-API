from flask import Flask, jsonify 
import requests

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

app.route('',methods=['POST'])
def create():
    data = requests.get_json()
    new = 
    
    pass




########################PATCH METHOD #####################################

app.route('',methods=['PATCH'])

def update():
    data = requests.get_json()

    pass




################################DELETE METHOD#############################
app.route('',methods=['DELETE'])
def delete():
    data = requests.get_json()

    pass



if __name__ == "__main__":
   app.run(debug=True)