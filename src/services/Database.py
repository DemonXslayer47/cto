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
                    "Orig. Submit Date": getattr(result, 'OrigSubmitDate', None),
                    "IRB Submit Date": getattr(result, 'IRBSubmitDate', None),
                    "Pause Date": getattr(result, 'PauseDate', None),
                    "Restart Date": getattr(result, 'RestartDate', None),
                    "Est. Start Date": getattr(result, 'EstStartDate', None),
                    "eRS/WD": getattr(result, 'eRSWD', None),
                    "IRB": getattr(result, 'IRB', None),
                    "PI": getattr(result, 'PI', None),
                    "SC": getattr(result, 'SC', None),
                    "Dept": getattr(result, 'Dept', None),
                    "Study Feasibility": getattr(result, 'StudyFeasibility', None),
                    "Sponsor / Protocol": getattr(result, 'SponsorProtocol', None),
                    "ICF": getattr(result, 'ICF', None),
                    "IDE IND": getattr(result, 'IDEIND', None),
                    "CTA": getattr(result, 'CTA', None),
                    "SSM Fac": getattr(result, 'SSMFac', None),
                    "SSM Pharm": getattr(result, 'SSMPharm', None),
                    "SSM RBR Approval": getattr(result, 'SSMRBRApproval', None),
                    "CTO CA": getattr(result, 'CTOCA', None),
                    "CTO Budget": getattr(result, 'CTOBudget', None),
                    "CTO IRB Check List": getattr(result, 'CTOIRBCheckList', None),
                    "CTO CTMS": getattr(result, 'CTOCTMS', None),
                    "CTO/EPIC": getattr(result, 'CTOEPIC', None),
                    "CTO WD Grant": getattr(result, 'CTOWDGrant', None),
                    "IRB Approval": getattr(result, 'IRBApproval', None),
                    "Status": getattr(result, 'Status', None),
                    "Type": getattr(result, 'Type', None),
                    "FY": getattr(result, 'FY', None),
                    "FQ": getattr(result, 'FQ', None),
                    "CTO DO": getattr(result, 'CTODO', None),
                    "IRB DO": getattr(result, 'IRBDO', None),
                    "Goal": getattr(result, 'Goal', None),
                    "Rate": getattr(result, 'Rate', None),
                    "Complete Date": getattr(result, 'CompleteDate', None),
                    "Project CTO TA": getattr(result, 'ProjectCTOTA', None),
                    "Project IRB TA": getattr(result, 'ProjectIRBTA', None),
                    "Which IRB": getattr(result, 'WhichIRB', None),
                    "Protocol Version & Date": getattr(result, 'ProtocolVersionDate', None),
                    "CTO Notes": getattr(result, 'CTONotes', None),
                    "CTPI Notes": getattr(result, 'CTPINotes', None),
                    "CA Develop Start Date": getattr(result, 'CADevelopStartDate', None),
                    "CA SSM Appr. / Final Date": getattr(result, 'CASSMApprFinalDate', None),
                    "CA Dev / Final TA": getattr(result, 'CADevFinalTA', None),
                    "CA Submit / Start Dev TA": getattr(result, 'CASubmitStartDevTA', None),
                    "CA Submit / Final TA": getattr(result, 'CASubmitFinalTA', None),
                    "Budget Neg Start Date": getattr(result, 'BudgetNegStartDate', None),
                    "Budget Final Date": getattr(result, 'BudgetFinalDate', None),
                    "Budget Neg / Final TA": getattr(result, 'BudgetNegFinalTA', None),
                    "Budget Submit / Final TA": getattr(result, 'BudgetSubmitFinalTA', None),
                    "CTA Final Date": getattr(result, 'CTAFinalDate', None),
                    "CTA Submit / Final TA": getattr(result, 'CTASubmitFinalTA', None),
                    "CTA FE Date": getattr(result, 'CTAFEDate', None),
                    "CTA Final / FE TA": getattr(result, 'CTAFinalFETA', None),
                    "Local IRB Review Complete": getattr(result, 'LocalIRBReviewComplete', None),
                    "CTO Checklist Rec'd": getattr(result, 'CTOChecklistRecd', None),
                    "IRB Ancillary Reviews Rec'd": getattr(result, 'IRBAncillaryReviewsRecd', None),
                    "IRB Comments Sent": getattr(result, 'IRBCommentsSent', None),
                    "IRB SAF Signed": getattr(result, 'IRBSAFSigned', None),
                    "Final IRB Approval Date": getattr(result, 'FinalIRBApprovalDate', None),
                    "Local IRB Review Complete TA": getattr(result, 'LocalIRBReviewCompleteTA', None),
                    "CTO Checklist Rec'd TA": getattr(result, 'CTOChecklistRecdTA', None),
                    "IRB Ancillary Reviews Rec'd TA": getattr(result, 'IRBAncillaryReviewsRecdTA', None),
                    "IRB Comment Sent TA": getattr(result, 'IRBCommentSentTA', None),
                    "SIRB Approval TA": getattr(result, 'SIRBApprovalTA', None)
                }
                return response
            else:
                return {"error": "No matching records"}
    except Exception as e:
        print("Error:", e)
        return {"error": "An error occurred"}


if __name__ == "__main__":
    app_db.run(debug=True)
