# NOTE: STRINGS

''' all texts are strings.
everything written in single, double or triple quotes count as a string'''

multiline_string = ''' My name is aditya mishra and i love many things in life. 
i really enjoy eating food, talking to my partner, playing video games, drawing 
art and sleepnig'''
print(multiline_string)
double_quotes_string = """ this is the same
as the above"""

print(double_quotes_string)
print(multiline_string + double_quotes_string)

first_name = 'Aditya'
last_name = 'Mishra'
print(len(first_name) > len(last_name))

# string formatting 

print(" hy my name is %s %s" %(first_name , last_name))

radius = 2
area_of_circle = 3.14 * radius ** 2
formatted_string = ' the area of the circle with radius %d is %.2f' %(radius, area_of_circle)

print(formatted_string)

# new string formatting

a = 5
b = 10
print("the area of the circle with radius {} is {}".format(radius, area_of_circle))
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# string interpolation (fav method)

print(f"the area of the circle with radius {radius} is {area_of_circle}")
