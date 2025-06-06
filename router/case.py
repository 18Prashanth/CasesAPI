from motor.motor_asyncio import AsyncIOMotorCollection
from schema.case import CaseBase
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status
from database import db
from schema.case import CaseResponse
from schema.documents import DocumentUpload


router = APIRouter()
Collection = db["cases"]

# Function to get next case number
async def get_next_case_number():
    counter = await db.counters.find_one_and_update(
        {"_id": "caseid"},
        {"$inc": {"sequence_value": 1}},
        return_document=True,
        upsert=True
    )
    return counter["sequence_value"]

# Function to get next document number
async def get_next_document_number():
    counter = await db.counters.find_one_and_update(
        {"_id": "document_id"},
        {"$inc": {"sequence_value": 1}},
        return_document=True,
        upsert=True
    )
    return counter["sequence_value"]


# Fuction to upload the document
@router.post("/cases/", response_model= CaseResponse, status_code=status.HTTP_200_OK)
async def create_case(case:CaseBase):
    case_number = await get_next_case_number()
    case_id = f"CASE_{case_number}"

    new_case = {
        "caseid": case_id,
        "casename": case.casename,
        "documents": [],
        "summaries": []
        }
    
    result = await Collection.insert_one(new_case)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create case")
        
    return new_case



@router.post("/cases/upload_document")
async def upload_document(caseid: str, request: DocumentUpload):
    document_num = await get_next_document_number()
    document_id = f"DOC_{document_num}"
    
    document_data = {
        "document_id": document_id,
        "document_path": request.document_path,
        "documnet_name": request.documnet_name,
        "document_status": "active"
    }
    
    # Update the case document → push into documents array
    result = await db.cases.update_one(
        {"caseid": caseid},
        {"$push": {"documents": document_data}}
    )
    
    if result.modified_count == 1:
        return {"message": "Document uploaded successfully", "document_id": document_id}
    else:
        raise HTTPException(status_code=404, detail="Case not found or failed to upload document")