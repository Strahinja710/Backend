from pydantic import BaseModel
import datetime 

class StudentSchema(BaseModel):
    name: str
    age: int
    grade: str
    enrollment_date: datetime.date

class StudentCreate(StudentSchema):
    pass

class StudentUpdate(StudentSchema):
    pass

class MyStudent(BaseModel):    
    id: int
    name: str
    age: int
    grade: str
    enrollment_date: datetime.date
