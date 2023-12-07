from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

app_db = Flask(__name__)
CORS(app_db)

#engine = create_engine('mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=.&database=Data_5710')
engine = create_engine('mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=HP&database=CTO') #update the string with your sql server and db details.

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

def data_db(req):
    try:
        with Session(engine) as session:
            sql_statement = text("SELECT * FROM CTO WHERE " + " AND ".join(f"{field} = :{field}" for field in req.keys()))
            query_params = req
            print("Executing SQL statement:", sql_statement)
            print("Query Parameters:", query_params)
            
            query = session.execute(sql_statement, query_params)
            result = query.first()

            if result:
                response = {
                    "Orig. Submit Date": getattr(result, 'Orig. Submit Date', None),
                    "IRB Submit Date": getattr(result, 'IRB Submit Date', None),
                    "Pause Date": getattr(result, 'Pause Date', None),
                    "Restart Date": getattr(result, 'Restart Date', None),
                    "Est. Start Date": getattr(result, 'Est. Start Date', None),
                    "eRS/WD": getattr(result, 'eRS/WD', None),
                    "IRB": getattr(result, 'IRB', None),
                    "PI": getattr(result, 'PI', None),
                    "SC": getattr(result, 'SC', None),
                    "Dept": getattr(result, 'Dept', None),
                    "Study Feasibility": getattr(result, 'Study Feasibility', None),
                    "Sponsor / Protocol": getattr(result, 'Sponsor / Protocol', None),
                    "ICF": getattr(result, 'ICF', None),
                    "IDE IND": getattr(result, 'IDE IND', None),
                    "CTA": getattr(result, 'CTA', None),
                    "SSM Fac": getattr(result, 'SSM Fac', None),
                    "SSM Pharm": getattr(result, 'SSM Pharm', None),
                    "SSM RBR Approval": getattr(result, 'SSM RBR Approval', None),
                    "CTO CA": getattr(result, 'CTO CA', None),
                    "CTO Budget": getattr(result, 'CTO Budget', None),
                    "CTO IRB Check List": getattr(result, 'CTO IRB Check List', None),
                    "CTO CTMS": getattr(result, 'CTO CTMS', None),
                    "CTO/EPIC": getattr(result, 'CTO/EPIC', None),
                    "CTO WD Grant": getattr(result, 'CTO WD Grant', None),
                    "IRB Approval": getattr(result, 'IRB Approval', None),
                    "Status": getattr(result, 'Status', None),
                    "Type": getattr(result, 'Type', None),
                    "FY": getattr(result, 'FY', None),
                    "FQ": getattr(result, 'FQ', None),
                    "CTO DO": getattr(result, 'CTO DO', None),
                    "IRB DO": getattr(result, 'IRB DO', None),
                    "Goal": getattr(result, 'Goal', None),
                    "Rate": getattr(result, 'Rate', None),
                    "Complete Date": getattr(result, 'Complete Date', None),
                    "Project CTO TA": getattr(result, 'Project CTO TA', None),
                    "Project IRB TA": getattr(result, 'Project IRB TA', None),
                    "Which IRB": getattr(result, 'Which IRB', None),
                    "Protocol Version & Date": getattr(result, 'Protocol Version & Date', None),
                    "CTO Notes": getattr(result, 'CTO Notes', None),
                    "CTPI Notes": getattr(result, 'CTPI Notes', None),
                    "CA Develop Start Date": getattr(result, 'CA Develop Start Date', None),
                    "CA SSM Appr. / Final Date": getattr(result, 'CASSM Appr. / Final Date', None),
                    "CA Dev / Final TA": getattr(result, 'CA Dev / Final TA', None),
                    "CA Submit / Start Dev TA": getattr(result, 'CA Submit / Start Dev TA', None),
                    "CA Submit / Final TA": getattr(result, 'CA Submit / Final TA', None),
                    "Budget Neg Start Date": getattr(result, 'Budget Neg Start Date', None),
                    "Budget Final Date": getattr(result, 'Budget Final Date', None),
                    "Budget Neg / Final TA": getattr(result, 'Budget Neg / Final TA', None),
                    "Budget Submit / Final TA": getattr(result, 'Budget Submit / Final TA', None),
                    "CTA Final Date": getattr(result, 'CTA Final Date', None),
                    "CTA Submit / Final TA": getattr(result, 'CTA Submit / Final TA', None),
                    "CTA FE Date": getattr(result, 'CTA FE Date', None),
                    "CTA Final / FE TA": getattr(result, 'CTA Final / FE TA', None),
                    "Local IRB Review Complete": getattr(result, 'Local IRB Review Complete', None),
                    "CTO Checklist Rec'd": getattr(result, 'CTO Checklist Recd ', None),
                    "IRB Ancillary Reviews Rec'd": getattr(result, 'IRBAncillaryReviewsRecd', None),
                    "IRB Comments Sent": getattr(result, 'IRB Comments Sent', None),
                    "IRB SAF Signed": getattr(result, 'IRB SAF Signed', None),
                    "Final IRB Approval Date": getattr(result, 'Final IRB Approval Date', None),
                    "Local IRB Review Complete TA": getattr(result, 'Local IRB Review Complete TA', None),
                    "CTO Checklist Rec'd TA": getattr(result, 'CTO Checklist Recd TA', None),
                    "IRB Ancillary Reviews Rec'd TA": getattr(result, 'IRB Ancillary Reviews Recd TA', None),
                    "IRB Comment Sent TA": getattr(result, 'IRB Comment Sent TA', None),
                    "SIRB Approval TA": getattr(result, 'SIRB Approval TA', None)
                }
                return response
            else:
                return {"error": "No matching records"}
    except Exception as e:
        print("Error:", e)
        return {"error": "An error occurred"}



if __name__ == "__main__":
    app_db.run(debug=True)