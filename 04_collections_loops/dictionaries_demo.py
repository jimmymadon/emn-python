# Simple List
cars_list = ['Mercedes Benz', 'BMW', 'Audi', 'Ferrari']

cars_dictionary = {
    'A Class': 'Mercedes Benz',
    '3 Series': 'BMW',
    'Q7': 'Audi',
    'F350': 'Ferrari',
    'Q5': 'Audi'
}

# print(cars_list)
# print(cars_dictionary)

# print(cars_dictionary.keys())
# print(cars_dictionary.values())

# print(cars_list[2])
# print(cars_dictionary['Q7'])

print("Printing items in cars_list:")
for car in cars_list:
    print(car)

print()
print("Printing items in cars_dictionary")
for car in cars_dictionary:
    print("Key:", car)
    print("Value:", cars_dictionary[car])
