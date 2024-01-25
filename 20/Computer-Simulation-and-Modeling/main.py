# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This is a message inside the class.")
#
# myobjectx = MyClass()
#
# print(myobjectx.variable)
import random

# my_information = {'name':'Fahim', 'age':24, 'occupation':'Student'}
#
# print(my_information)

import pandas as pd
# dict = {"Country":["Bangladesh", "India", "USA"],
#         "Capital":["Dhaka", "Delhi", "Washington DC"],
#         "Population":[100, 150, 125]}
#
# bricks = pd.DataFrame(dict)
# bricks.index = ["Bd", "In", "US"]
# print(bricks)
# importing the module

# def outer_function():
#     message = "Hi"
#
#     def inner_function():
#         print(message)
#     return inner_function
# my_func = outer_function()
# my_func()
#
my_pets = ['Alfread', 'Nobel', 'Simi']

new_list = list(map(str.upper, my_pets))
print(new_list)