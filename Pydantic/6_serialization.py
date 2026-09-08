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

temp = patient1.model_dump()
print(temp)
print(type(temp))
temp_j = patient1.model_dump_json()
print(temp_j)
print(type(temp_j))
temp3 = patient1.model_dump(include=['name']) #exclude
print(temp3)
print(type(temp3))
