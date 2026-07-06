from flask import Flask, jsonify 
import requests

app = Flask(__name__)



############################ GET METHOD #################################


app.route('',methods =['GET'])
def get_inventory():
    pass



################################POST METHOD #####################################

app.route('',methods=['POST'])
def create():
    data = requests.get_json()
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



