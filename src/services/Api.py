from flask import Flask, request, jsonify
from flask_cors import CORS
from Database import register_db, login_db, data_db

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    print(req)
    res = login_db(req)
    print(res)  
    return jsonify(res)

@app.route('/register', methods=['POST'])
def register_user():
    req = request.get_json()
    print(req)

    # Check if the required keys are present in the request data
    required_keys = ['Name', 'ContactId', 'Email', 'Address', 'ZipCode', 'UserName', 'Password']
    if not all(key in req for key in required_keys):
        return jsonify({"error": "Missing required keys"})

    res = register_db(req)
    return jsonify(res)

@app.route('/cto-data', methods=['POST'])
def cto_data():
    try:
        req_data = request.get_json()

        if not req_data:
            return jsonify({"error": "Invalid JSON data"})

        res = data_db(req_data)
        
        if 'error' in res:
            return jsonify(res), 500  # Internal Server Error
        else:
            return jsonify(res)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == "__main__":
    app.run(debug=True)
