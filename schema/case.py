from pydantic import BaseModel
from typing import List, Optional
from .documents import DocumentModel, SummaryModel

class CaseBase(BaseModel):
    casename: str
    document_path: str
    documnet_name: str

class CaseResponse(BaseModel):
    caseid: str
    casename: str

    class Config:
        from_attributes = True

class CaseModel(CaseBase):
    caseid: str
    documents: List[DocumentModel] = []
    summaries: List[SummaryModel] = []

    class Config:
        from_attributes = True


