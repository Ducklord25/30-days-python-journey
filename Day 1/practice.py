print("Data types in python and Comments")

# single line comment 

''' Python does not have a dedicated multiline comment syntax, instead we can use 
triple single quotes to replicate a similar effect.'''

""" triple double quotes also has the same multi-line effect in python"""

''' NOTE: these are "multiline comments" are ignored by the compiler ONLY if they are not 
assigned to a variable.'''



l = [1,2,3,4,5] # this is a list. ORDERED elements of same data types
l1 = [1,4,'aditya',7.4] # differnet data types - int, int, string, float
tu = ('aditya',20, True, False, 79.4) # This is a tuple, they are immutable (cant change)
# lists use square brackets and can be changed so they are mutable 
# tuples use parentheses and cannot be changed so they are called immutable
#both are ordered, both can contain different data types.


a= {
    'first-name':'aditya',
    'last-name' : "mishra",
    'age': 20,
} # this is a dictionary, they are unordered collection of data in key value pair format.

b = {1,2,3,4,'aditya'} # this is a set, uses curly brackets, mutable and heterogenous 



