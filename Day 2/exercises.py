# Day 2: 30 days of python programming

# exercise level 1
first_name = 'Aditya'
last_name = 'Mishra'
full_name = 'Aditya Mishra'
country = 'india'
city = 'Hyderabad'
age = 21
year = 2026
is_married = False
is_light_on = False
a, b, c, d = 10, 20, 30, 40

# exercise level 2 
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

print(len(first_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

# circle problem 
circle_radius = 30
area_of_circle = 3.14 * (circle_radius ** 2)
circum_of_circle = 2 * 3.14 * circle_radius
print(f"area of circle = {area_of_circle} \n circumference of circle = {circum_of_circle}")

circle_radius = int(input("Enter the Circle's radius : "))
area_of_circle = 3.14 * (circle_radius ** 2)
print(f"Area of circle = {area_of_circle}")

first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
country = str(input("Enter your country : "))
age = int(input("Enter your age : "))