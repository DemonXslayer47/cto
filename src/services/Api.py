from flask import Flask, request, jsonify
from Database import register_db, login_db, data_db
from flask_cors import CORS

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


@app.route('/update', methods=['POST'])
def update():
    req = request.get_json()
    print(req)
    # Call the function for update
    # res = update_db(req)
    # return jsonify(res)
    return jsonify({"message": "Update endpoint called"})

@app.route('/track', methods=['GET'])  # Change to GET method
def track():
    try:
        # Call the function to fetch data
        data = data_db()  # Implement this function in Database.py
        return jsonify(data)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "An error occurred"})

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
