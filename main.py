from uuid import uuid4
from fastapi import FastAPI
from database import db
from schema.case import CaseBase
from motor.motor_asyncio import AsyncIOMotorCollection


app = FastAPI()
collection: AsyncIOMotorCollection = db["cases"]

@app.post("/cases/")
async def create_case(case:CaseBase):
    new_case_id = f"CASE_{str(uuid4())[:8]}"

    case_doc = {
        "caseid": new_case_id,
        "casename": case.casename,
        "documents": [],
        "summaries": []
        }
    
    await collection.insert_one(case_doc)
    return {"caseid": new_case_id, "message": "Case created successfully."}