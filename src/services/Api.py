from flask import Flask
from flask import request,jsonify,render_template
from traitlets import This
from Database import register_db,login_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login',methods = ['POST'])
def login():
    req = request.get_json()
    print(req)
    res = login_db(req)
    return jsonify(res)

@app.route('/register', methods=['POST'])
def register_user():
    req = request.get_json()
    print(req)
    res = register_db(req)
    return jsonify(res)

