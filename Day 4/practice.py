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

# STRING OPERATIONS !!!!!!!!!!!!!!!!1

language = 'python'
print(language[0]) # p
print(language[1]) # y
print(language[2]) # t
print(language[3]) # h
print(language[4]) # o
print(language[5], 'end') # n

print(language[-1]) # n reverse order
print(language[-2]) # o
print(language[-3]) # h
print(language[-4]) # y

# String Slicing

print(language[0:3]) # pyt starts at 0 index and goes until index 3 EXCLUSIVELY
print(language[3:9]) # hon even if you exceed upper limit ie, 5, it will print result
print(language[:3]) # pyt
print(language[-3:-3]) # prints blank
print(language[3:])

''' basically the first value indicated where to start, second value indicates
where to stop and the third value tells the compiler what step value to take'''

a = "my name is aditya"
print(a[2::1]) #starts at index 2, second value infinite, third value is default step
print(a[0::3]) #starts at index 0, second value infinite, third value is skip 2
#if skip value is 3, it will skip 2 digits only

print(a.capitalize()) # first letter caps
print(a.count('a', 0, 17)) # count of (substring, start= , end= )
print(a.endswith('ya')) # true
print(a.endswith('b')) # false
print(a.expandtabs(100)) # replaces tab size with spaces, default size is 8
print(a.find("a")) # finds the first occurence and returns index, not found -1
print(a.rfind('a')) # same but last occurence
print(a.isalnum()) # checks if alphanumeric, whitespace is not alnum
print(a.isalpha()) # checks if all elements belong to a-z, A-Z, space is not included
print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())
print(a.islower())
print(a.isupper())

hy = ['aditya', 'naughty', 'eshika', 'smarty']
print(' '.join(hy)) # aditya naughty eshika smarty
print('$$'.join(hy)) # aditya$$naughty$$eshika$$smarty
print(a.strip('y')) # removes these letters only from start and end
print(a.replace('aditya','eshika')) # replaces first substring with second
print(a.split()) 
print(a.title())
print(a.swapcase())
