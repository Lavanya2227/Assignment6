# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
 

states = []
capitals = []
print("\nWe are going to know 7 States and their Capitals!")
for i in range(7):
    state = input("Enter State Name: ")
    capital = input("Enter capital of %s :"%(state))

    states.append(state)
    capitals.append(capital)

print("List of states: ", states)
print("List of capital: ", capitals)

state_capital_dict = {}

for key in states:
    for value in capitals:
        state_capital_dict[key] = value
        capitals.remove(value)
        break

print("\nDictionary formate of States and their Capital:")
print(state_capital_dict)

import json

with open("C:/Users/harsh/OneDrive/Desktop/Python.py/State.json" , 'w') as file:
    json.dump(state_capital_dict,file, indent=3)

print("\n")
print(json.dumps(state_capital_dict, indent=4)) 