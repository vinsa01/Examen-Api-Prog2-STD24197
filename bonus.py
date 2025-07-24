
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Li

app = FastAPI()
students_db = []

@app.get("/students-authorized")
def get_students_authorized(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        raise HTTPException(status_code=401, detail="Unauthorized: Authorization header missing")
    if auth_header != "bon courage":
        raise HTTPException(status_code=403, detail="Forbidden: Invalid authorization")
    return students_db

