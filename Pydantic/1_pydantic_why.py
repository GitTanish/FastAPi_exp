from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

# patient_info= {'name':'doof', 'age':42}
patient1 = Patient(name ='doof', age = 42)

insert(patient1)
