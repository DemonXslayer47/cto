from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

app_db = Flask(__name__)
CORS(app_db)

engine = create_engine('mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=.&database=Data_5710')

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
    app_db.run(debug=True)
