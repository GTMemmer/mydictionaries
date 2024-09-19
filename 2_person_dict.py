person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)
print(person)

# print out the name of the second child
child = person['children']
print(child[1])
#or
print(person['children'][1])


# print out the name of the cat
pet = person['pets']
print(pet['cat'])
#or
print(person['pets']['cat'])

# use a loop to print out the names of each child
for child in person['children']:
    print(child)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido
pet = person['pets']
for k,v in pet.items():
    print(f'The type of pet is: {k} and the name of the pet is: {v}')
#or
for k,v in person['pets'].items():
    print(f'The type of pet is: {k} and the name of the pet is: {v}')