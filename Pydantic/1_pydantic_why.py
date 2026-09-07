from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
# field can be used for data validation and to attach metadata with Annotated
class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient',description='Name should be less than 50 characters', examples=['Doof','Bidoof'])]
    email: EmailStr
    Url: AnyUrl
    age: int= Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False, description="Is the patient married or not?")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
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
    married=True,
    allergies=['dust', 'peanut'],
    contact_details={
        'phone': '23940232'
    }
)

insert(patient1)
