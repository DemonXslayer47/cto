from flask import Flask
from flask import request, jsonify
from Database import register_db, login_db, data_db,pidata_db,irbdata_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    print(req)
    res = login_db(req)
    print(res)  # Add this line to check the response
    return jsonify(res)

#hi

@app.route('/register', methods=['POST'])
def register_user():
    req = request.get_json()
    print(req)
    res = register_db(req)
    return jsonify(res)

@app.route('/data', methods=['POST'])
def data():
    req = request.get_json()
    print(req)
    res = data_db(req)
    return jsonify(res)

# @app.route('/pidata', methods=['POST'])
# def pidata():
#     req = request.get_json()
#     print(req)
#     res = pidata_db(req)
#     return jsonify(res)


# @app.route('/irbdata', methods=['POST'])
# def irbdata():
#     req = request.get_json()
#     print(req)
#     res = irbdata_db(req)
#     return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
