from flask import Flask
from flask import request,jsonify,render_template
from traitlets import This
from Database import addBike_item_to_cart, addCar_item_to_cart, get_store_details, getAllBikesFrom_db,getAllSparesForBikes,getAllCarsFrom_db,getAllSparesForCars, getBikeBrands,getBikeModelsByBrand, getBrandModelBikeParts, getBrandModelCarParts, getBrands, getModelsByBrand, prepareShoppingCart,register_db,login_db, update_delivery_type
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login',methods = ['post'])
def login():
    req = request.get_json()
    print(req)
    res = login_db(req)
    return jsonify(res)

@app.route('/data', methods=['POST'])
def register_user():
    req = request.get_json()
    print(req)
    res = register_db(req)
    return jsonify(res)
