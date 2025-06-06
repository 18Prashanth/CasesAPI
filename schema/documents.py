from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentUpload(BaseModel):
    document_path: str
    documnet_name: str
    
class DocumentModel(BaseModel):
    document_id: str
    document_path: str
    document_name: str
    document_status: str = "active"

    class Config:
        from_attributes = True

class SummaryModel(BaseModel):
    summary_id: str
    summary_path: str
    status: str
    created_at: datetime
