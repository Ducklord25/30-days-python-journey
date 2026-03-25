# exercises, each in order

age = int(21)
height = float(180)
complex_num = 1 + 4j

# problem 3, area of triangle based on user input

base = int(input("Enter base : "))
height = int(input("Enter Height : "))
area_of_triangle = 0.5 * base * height
print(f"The area of the triangle is {area_of_triangle} \n")

side_a = int(input("Enter side a :"))
side_b = int(input("Enter side b :"))
side_c = int(input("Enter side c : "))
perimeter_of_triangle = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter_of_triangle} \n")

rect_length = int(input("Enter the length of rectangle : "))
rect_breadth = int(input("Enter the breadth of rectangle : "))

rect_area = rect_length * rect_breadth
rect_perimeter = 2*(rect_breadth + rect_length)
print(f"Area of the rectangle = {rect_area}")
print(f"Perimeter of the rectangle = {rect_perimeter}")

circle_radius = int(input("Enter the radius of the circle : "))
circle_area = 3.14 * circle_radius ** 2 
circle_circum = 2 * 3.14 * circle_radius
print(f"Area of the circle = {circle_area}")
print(f"Circumference of the circle = {circle_circum}")

m = 2
c = -2
y_intercept = (0,-2)
x_intercept = -c / m
slope = m
print(x_intercept)

