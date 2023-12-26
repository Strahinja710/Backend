from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter()

@router.get("/students/", response_model=List[schemas.MyStudent])
def read_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router.get("/students/{student_id}", response_model=schemas.StudentSchema)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/students/by-grade/{student_grade}", response_model=List[schemas.StudentSchema])
def read_student_grade(student_grade: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.grade == student_grade).all()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/students/", response_model=schemas.StudentSchema)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(name=student.name, age=student.age, grade=student.grade, enrollment_date=student.enrollment_date)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.put("/students/{student_id}", response_model=schemas.StudentSchema)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    update_data = student.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
    db.commit()
    return db_student

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}
