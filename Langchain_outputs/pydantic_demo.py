from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name: str = 'ajay'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {'age':'32', 'email':'ajay@gmail.com', 'cgpa':8} #type parsing , default values, email validation, range valiation ---- pydantic can do all of these.

student = Student(**new_student)

print(student)