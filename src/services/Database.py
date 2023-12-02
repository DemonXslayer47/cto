from flask import jsonify
from numpy import insert
from sqlalchemy import Enum, LargeBinary, and_, create_engine, update
from sqlalchemy import select
import base64

import sqlalchemy

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declared_attr

#engine = create_engine('mssql+pyodbc://@' + '.' + '/' + 'Mechazone' + '?trusted_connection=yes & driver=ODBC Driver 17 for SQL Server')

connection_string = 'mssql+pyodbc://@' + '.' + '/' + 'Data_5710' + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string)



from datetime import datetime
from sqlalchemy import ForeignKey,DateTime,Boolean
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Integer,Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import insert
from sqlalchemy import text
from flask import session 


class Base:
    pass
    
#Base = declarative_base(cls=Base)
Base = sqlalchemy.orm.declarative_base(cls=Base)

class Users(Base):
    __tablename__ = "Users"

    UserId: int = Column(Integer, primary_key=True)
    Name: str = Column(String(255), nullable=False)
    ContactId: int = Column(Integer, nullable=False)
    Email: str = Column(String, nullable=False)
    Address: str = Column(String, nullable=False)
    ZipCode: str = Column(String, nullable=False)
    UserName: str = Column(String, nullable=False)
    Password: str = Column(String, nullable=False)


def register_db(req):

    from sqlalchemy import insert
    stmt = insert(Users).values(Name=req['Name'], ContactId=req['ContactId'],Email=req['Email'],Address=req['Address'],ZipCode=req['ZipCode'],UserName=req['UserName'],Password=req['Password'])
    compiled = stmt.compile()
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
    return {"issuccess": True} 



def login_db(req):
    try:
        from sqlalchemy import text
        with Session(engine) as session:
            
            sql_statement = text("SELECT * FROM Users WHERE UserName = :userName and Password = :password" )
            query = session.query(Users).from_statement(sql_statement)
            query = query.params(userName=req['UserName'],password = req['Password'])

           
            result = query.first()
            response = {
                "userId": result.UserId,
                "name" : result.Name,
                "contactId": result.ContactId,
                "email": result.Email,
                "userName": result.UserName,
                "address": result.Address,
                "zipCode": result.ZipCode
            }
           
            return response
    except Exception as e:
        print(e)
        return {}        


 
     


