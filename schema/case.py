from pydantic import BaseModel
from typing import List, Optional
from .documents import DocumentModel, SummaryModel

class CaseBase(BaseModel):
    casename: str

class CaseModel(CaseBase):
    caseid: str
    documents: List[DocumentModel] = []
    summaries: List[SummaryModel] = []

    class Config:
        from_attributes = True
