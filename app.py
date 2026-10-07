import csv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students = []

with open("q-fastapi.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })


@app.get("/api")
def get_students(
    class_: list[str] | None = Query(default=None, alias="class")
):
    if class_:
        return [
            student for student in students
            if student["class"] in class_
        ]

    return students


@app.get("/")
def root():
    return {"status": "ok"}
