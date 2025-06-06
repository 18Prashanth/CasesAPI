from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentModel(BaseModel):
    document_id: str
    document_path: str
    document_name: str
    document_status: str = "active"

class SummaryModel(BaseModel):
    summary_id: str
    summary_path: str
    status: str
    created_at: datetime
