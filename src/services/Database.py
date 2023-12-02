from flask import Flask
from flask import request, jsonify, render_template
from flask_cors import CORS
from sqlalchemy import create_engine, select, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

app = Flask(__name__)
CORS(app)

# Define your database connection string
connection_string = 'mssql+pyodbc://@' + '.' + '/' + 'Data_5710' + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string)

# Define your declarative base
Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"

    UserId = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    ContactId = Column(Integer, nullable=False)
    Email = Column(String, nullable=False)
    Address = Column(String, nullable=False)
    ZipCode = Column(String, nullable=False)
    UserName = Column(String, nullable=False)
    Password = Column(String, nullable=False)

# Initialize the database with the app
Base.metadata.create_all(bind=engine)

def register_db(req):
    stmt = Users.__table__.insert().values(
        Name=req['Name'],
        ContactId=req['ContactId'],
        Email=req['Email'],
        Address=req['Address'],
        ZipCode=req['ZipCode'],
        UserName=req['UserName'],
        Password=req['Password']
    )

    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

    return {"issuccess": True}

def login_db(req):
    try:
        with Session(engine) as session:
            sql_statement = text("SELECT * FROM Users WHERE UserName = :userName and Password = :password")
            query = session.execute(sql_statement, {'userName': req['UserName'], 'password': req['Password']})
            result = query.first()

            if result:
                response = {
                    "userId": result.UserId,
                    "name": result.Name,
                    "contactId": result.ContactId,
                    "email": result.Email,
                    "userName": result.UserName,
                    "address": result.Address,
                    "zipCode": result.ZipCode
                }
                return response
            else:
                return {"error": "Invalid credentials"}

    except Exception as e:
        print(e)
        return {}

if __name__ == "__main__":
    app.run(debug=True)
