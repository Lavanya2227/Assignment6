

# 1. Assignment on employee details.

import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employees_data = [
    {
        "Name": "Lavanya",
        "DOB": "2000-08-15",
        "Height": 169,
        "City": "Vizag",
        "State": "Andhrapradesh"
    },
    {
        "Name": "Ramya",
        "DOB": "1998-07-26",
        "Height": 175,
        "City": "Bobbili",
        "State": "Andhrapradesh"
    },
    {
        "Name": "Mahesh",
        "DOB": "1995-07-22",
        "Height": 179,
        "City": "Vizag",
        "State": "Andhrapradesh"
    },
    {
        "Name": "Vijaya",
        "DOB": "1986-10-23",
        "Height": 167,
        "City": "Guntur",
        "State": "Andhrapradesh"
    },
    {
        "Name": "Lakshmi",
        "DOB": "1998-11-01",
        "Height": 157,
        "City": "seetanagaram",
        "State": "Andhrapradesh"
    }
]

with open('C:/Users/harsh/OneDrive/Desktop/Python.py/employee.json', 'w') as json_file:
    json.dump(employees_data, json_file)

employees = []

with open('C:/Users/harsh/OneDrive/Desktop/Python.py/employee.json', 'r') as json_file:
    employees_data = json.load(json_file)
    
    for employee_data in employees_data:
        name = employee_data['Name']
        dob = employee_data['DOB']
        height = employee_data['Height']
        city = employee_data['City']
        state = employee_data['State']
        
        employee = Employee(name, dob, height, city, state)
        employees.append(employee)

for employee in employees:
    print(employees_data)  










