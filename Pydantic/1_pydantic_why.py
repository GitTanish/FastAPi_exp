from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    Url: AnyUrl
    age: int
    weight: float
    married: Optional[bool] =False
    allergies: Optional[List[str]] =None
    contact_details: Dict[str, str]

def insert(patient: Patient): # patient:Patient is annotation not enforcement
    print(patient.name)
    print(patient.email)
    print(patient.Url)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('Inserted')

# patient_info= {'name':'doof', 'age':42}
# patient1 = Patient(**patient_info)
patient1 = Patient(
    name='doof',
    email='panchax@killi.com',
    Url = 'https://linkedin.com/13',
    age=42,
    weight=62.3,
    allergies=['dust', 'peanut'],
    contact_details={
        'phone': '23940232'
    }
)

insert(patient1)
