from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age:int
    address:Address

address_dict={'city':'Mumbai', "state":'maharashtra','pin':'221221'}

address1= Address(**address_dict)

patient_dict={'name':'Doof','gender':'male','age': 42, 'address':address1}
patient1= Patient(**patient_dict)

print(patient1)
print(patient1.address.city)

# Better organization: Related data can be grouped together (e.g., vitals, address, insurance)
# Reusability: Nested models can be reused in multiple models (e.g., Patient, MedicalRecord)
# Readability: Easier for developers and API consumers to understand
# Validation: Nested models are validated automatically, requiring no extra work
