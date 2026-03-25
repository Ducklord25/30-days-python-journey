x1, x2, y1, y2 = 2, 6, 2, 10
slope = (y2 - y1)/(x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5 
print(f"Slope is {slope} and distance is {distance}")

# new exercise

x=-3 
y = x**2 + 6*x + 9 
print(y)

a = 'python'
b = 'dragon'
print(len(a), len(b))
print(a > b, a < b, a>=b, a<=b)

print('on' in a and 'on' in b)

random = "i hope this course is not full of jargon"
print("jargon is present in the sentence ? : ", 'jargon' in random)

print('on' not in a and 'on' not in b)

python_value = float(len('python'))
print(python_value)
python_string = str(python_value)
print(type(python_string))

print(5 % 2 is 0) # checks whether a number is even or not 
print(7//3  == int(2.7))