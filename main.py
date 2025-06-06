from fastapi import FastAPI
from database import db
from fastapi import APIRouter, HTTPException
from router import case


app = FastAPI()


app.include_router(case.router)