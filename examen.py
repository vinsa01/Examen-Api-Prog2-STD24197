
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()
students_db = []


class Student(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int


# Q1
@app.get("/hello", response_class=PlainTextResponse)
def hello():
    return "Hello Word"

# Q2
@app.get("/welcome", response_class=PlainTextResponse)
def welcome(name: str):
    return f"Welcome {name}"

# Q3
@app.post("/students", status_code=201)
def add_students(new_students: List[Student]):
    students_db.extend(new_students)
    return students_db

# Q4
@app.get("/students")
def get_students():
    return students_db

# Q5
@app.put("/students")
def upsert_student(student: Student):
    for i, s in enumerate(students_db):
        if s.Reference == student.Reference:
            students_db[i] = student
            return {"message": "Student updated", "students": students_db}
    students_db.append(student)
    return {
        "message": "Student added", "students": students_db
        }

