from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

app_db = Flask(__name__)
CORS(app_db)

engine = create_engine('mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=.&database=Data_5710')
#engine = create_engine('mssql+pyodbc:///?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server&server=HP&database=CTO') #update the string with your sql server and db details.

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
        # Remove extra spaces from keys in the payload
        req = {key.strip(): value for key, value in req.items()}

        with Session(engine) as session:
            sql_statement = text("SELECT * FROM CTO WHERE " + " AND ".join(f"{field} = :{field}" for field in req.keys()))
            query_params = req
            print("Executing SQL statement:", sql_statement)
            print("Query Parameters:", query_params)

            query = session.execute(sql_statement, query_params)
            results = query.fetchall()

            if results:
                response = [
                    {
                        "Orig. Submit Date": result['Orig. Submit Date'],
                        "IRB Submit Date": result['IRB Submit Date'],
                        "Pause Date": result['Pause Date'],
                        "Restart Date": result['Restart Date'],
                        "Est. Start Date": result['Est. Start Date'],
                        "eRS/WD": result['eRS/WD'],
                        "IRB": result['IRB'],
                        "PI": result['PI'],
                        "SC": result['SC'],
                        "Dept": result['Dept'],
                        "Study Feasibility": result['Study Feasibility'],
                        "Sponsor / Protocol": result['Sponsor / Protocol'],
                        "ICF": result['ICF'],
                        "IDE IND": result['IDE IND'],
                        "CTA": result['CTA'],
                        "SSM Fac": result['SSM Fac'],
                        "SSM Pharm": result['SSM Pharm'],
                        "SSM RBR Approval": result['SSM RBR Approval'],
                        "CTO CA": result['CTO CA'],
                        "CTO Budget": result['CTO Budget'],
                        "CTO IRB Check List": result['CTO IRB Check List'],
                        "CTO CTMS": result['CTO CTMS'],
                        "CTO/EPIC": result['CTO/EPIC'],
                        "CTO WD Grant": result['CTO WD Grant'],
                        "IRB Approval": result['IRB Approval'],
                        "Status": result['Status'],
                        "Type": result['Type'],
                        "FY": result['FY'],
                        "FQ": result['FQ'],
                        "CTO DO": result['CTO DO'],
                        "IRB DO": result['IRB DO'],
                        "Goal": result['Goal'],
                        "Rate": result['Rate'],
                        "Complete Date": result['Complete Date'],
                        "Project CTO TA": result['Project CTO TA'],
                        "Project IRB TA": result['Project IRB TA'],
                        "Which IRB": result['Which IRB'],
                        "Protocol Version & Date": result['Protocol Version & Date'],
                        "CTO Notes": result['CTO Notes'],
                        "CTPI Notes": result['CTPI Notes'],
                        "CA Develop Start Date": result['CA Develop Start Date'],
                        "CA SSM Appr. / Final Date": result['CA SSM Appr. / Final Date'],
                        "CA Dev / Final TA": result['CA Dev / Final TA'],
                        "CA Submit / Start Dev TA": result['CA Submit / Start Dev TA'],
                        "CA Submit / Final TA": result['CA Submit / Final TA'],
                        "Budget Neg Start Date": result['Budget Neg Start Date'],
                        "Budget Final Date": result['Budget Final Date'],
                        "Budget Neg / Final TA": result['Budget Neg / Final TA'],
                        "Budget Submit / Final TA": result['Budget Submit / Final TA'],
                        "CTA Final Date": result['CTA Final Date'],
                        "CTA Submit / Final TA": result['CTA Submit / Final TA'],
                        "CTA FE Date": result['CTA FE Date'],
                        "CTA Final / FE TA": result['CTA Final / FE TA'],
                        "Local IRB Review Complete": result['Local IRB Review Complete'],
                        "CTO Checklist Rec'd": result['CTO Checklist Recd'],
                        "IRB Ancillary Reviews Rec'd": result['IRBAncillaryReviewsRecd'],
                        "IRB Comments Sent": result['IRB Comments Sent'],
                        "IRB SAF Signed": result['IRB SAF Signed'],
                        "Final IRB Approval Date": result['Final IRB Approval Date'],
                        "Local IRB Review Complete TA": result['Local IRB Review Complete TA'],
                        "CTO Checklist Rec'd TA": result['CTO Checklist Recd TA'],
                        "IRB Ancillary Reviews Rec'd TA": result['IRB Ancillary Reviews Recd TA'],
                        "IRB Comment Sent TA": result['IRB Comment Sent TA'],
                        "SIRB Approval TA": result['SIRB Approval TA']
                    }
                    for result in results
                ]
                return response
            else:
                return {"error": "No matching records"}
    except Exception as e:
        print("Error:", e)
        return {"error": "An error occurred"}



if __name__ == "__main__":
    app_db.run(debug=True)