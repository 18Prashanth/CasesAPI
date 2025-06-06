from pydantic import BaseModel
from typing import List, Optional
from .documents import DocumentModel, SummaryModel

class CaseBase(BaseModel):
    casename: str

class CaseCreate(CaseBase):
    caseid: Optional[str]  # can be auto-generated

class CaseModel(CaseBase):
    caseid: str
    documents: List[DocumentModel] = []
    summaries: List[SummaryModel] = []

    class Config:
        orm_mode = True
