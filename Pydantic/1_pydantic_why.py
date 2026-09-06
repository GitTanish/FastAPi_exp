from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert(patient: Patient): # patient:Patient is annotation not enforcement
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('Inserted')

# patient_info= {'name':'doof', 'age':42}
# patient1 = Patient(**patient_info)
patient1 = Patient(
    name='doof',
    age=42,
    weight=62.3,
    married=True,
    allergies=['dust', 'peanut'],
    contact_details={
        'email': 'xyz@abc.com',
        'phone': '23940232'
    }
)

insert(patient1)

insert(patient1)
