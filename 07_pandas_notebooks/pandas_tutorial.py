import pandas as pd

cars_list = ["Mercedes", "BMW", "Audi"]
# Creating a Pandas Series using 1 simple python list
cars_series = pd.Series(cars_list)
print("Printing cars_series:")
print(cars_series)
print()
print("Third car in cars_series is:", cars_series[2])

cars_models = ["A Class", "3 Series", "Q5"]
# Creating a Pandas Series using 2 python lists: First list for values, second list for index/labels
cars_series_with_labels = pd.Series(cars_list, cars_models)
print("Printing cars_series_with_labels:")
print(cars_series_with_labels)
print()
print("Third car in cars_series_with_labels:", cars_series_with_labels["Q5"])

cars_dictionary = {
    'A Class': 'Mercedes',
    '3 Series': 'BMW',
    'Q5': 'Audi',
}
# Creating a Pandas Series using a single python dictionary
cars_series_with_labels_2 = pd.Series(cars_dictionary)
print("Printing cars_series_with_labels_2:")
print(cars_series_with_labels_2)
print()


car_passing_table = {
    'cars': ["BMW", "Volvo", "Ford", "Lamborghini"],
    'passings': [3, 7, 2, 5]
}

# Example of accessing the cars_passing_table dictionary
print("car_passing_table:", car_passing_table, type(car_passing_table))
# Example of accessing the 'cars' item of the dictionary which is a list
print(
    "car_passing_table['cars']:",
    car_passing_table['cars'],
    type(car_passing_table['cars'])
)
# Example of accessing the 'cars' item of the dictionary which is a list, and then accesing the first item of that list
print(
    "car_passing_table['cars'][0]:",
    car_passing_table['cars'][0],
    type(car_passing_table['cars'][0])
)

# Creating a Pandas DataFrame from a Python dictionary
car_passing_dataframe = pd.DataFrame(car_passing_table)
print(car_passing_dataframe)
