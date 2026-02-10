from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Jay'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5.0, description='A decimal value representing cgpa of a student.')

new_student = {'age' : '23', 'email': 'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])
# print(student) 
student_json = student.model_dump_json()
print(student_json)