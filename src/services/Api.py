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
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine('mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=HP&database=CTO') #update the string with your sql server and db details.

@app.route('/cto-data', methods=['POST'])
def cto_data():
    try:
        # Fetch all data from the CTO table
        with Session(engine) as session:
            sql_statement = text("SELECT * FROM CTO")
            query = session.execute(sql_statement)
            results = query.fetchall()

            # Get column names
            columns = query.keys()

            # Convert the results to a list of dictionaries
            data_list = [dict(zip(columns, row)) for row in results]

            if data_list:
                return jsonify(data_list)
            else:
                return jsonify({"error": "No matching records"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "An error occurred"})


if __name__ == "__main__":
    app.run(debug=True)
