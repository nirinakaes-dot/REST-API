from flask import Flask, jsonify 
import requests

app = Flask(__name__)



############################ GET METHOD #################################


app.route('',methods =['GET'])
def get_inventory():


    if not name:
       return ('Product not found',404)
    pass



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