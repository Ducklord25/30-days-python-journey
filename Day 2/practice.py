len("hello world !") # returns number of characters including spaces
type("hello world") # returns type of data
str(8) # converts to string
int("10") # converts to a number of int type
float(10) # converts a integer to float type

# input('enter your name: ') # takes user input

help('keywords')

l = [1,2,5,2,3,4,11,3,53,23,42,13,]
print(min(10,50,40,5,60))
print(max(20,30,100,40))
print(min(l))
print(max(l))
print(sum([4,3,4,3,5,1,])) # only accepts iterable data types(lists, tuples, set, etc)

# variablessssssssssssss

''' python uses snake_case, meaning that while declaring a variable name, if it 
exceeds more than one word, we use an underscore to separate them out.
eg, wheel_rotation_axis or aditya_food_counter 

variable names cannot start with a number, has alphanumeric values from a-z
and 0-9, they are case sensitive so first_name, First_name, FIRST_name, etc 
are all different variables.'''

print("multiple variable declaration in a single line: ")

first_name , last_name , country , age = 'Aditya' , 'mishra' , 'india' , 20
print(f"first name: {first_name} \n last name: {last_name} \n country: {country} \
      age: {age}" ) 

first_name= input("Enter your first name: ")
print(first_name)

print(type(zip([1,2],[5,8])))