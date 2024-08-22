# # Question_no1
birth_year= 2004
current_year= 2024
print("Age Calculator")

birth_year = int(input("Enter your Birth-Year: "))
current_year = int(input("Enter your Current-Year: "))

print("Your age is ",(current_year-birth_year))
# # ---------------------------------------------------

# # Question_no2  
length= 10
width= 10
print("Rectangle Area Calculator")
rectangle_length = int(input("Enter your Rectangle-length: "))
rectangle_width = int(input("Enter your Rectangle-Width:  "))

print("The area of your rectangle is ",(rectangle_length*rectangle_width))
# # ---------------------------------------------------

# # Question_no3
circle_radius= 4
print("Circle Area Calculator")
circle_radius = int(input("Enter your circle-radius: "))
pie_value = 3.1416

print("The area of circle is: ", (pie_value*(circle_radius**2)))
# ---------------------------------------------------

# Question_no4
length= 20
width= 10
height= 5
print("Cube Area Calculator")
cube_length = int(input("Enter your Cube-Length: "))
cube_width  = int(input("Enter your Cube-Width:  "))
cube_height = int(input("Enter your Cube-Width:  "))

print("The area of Cube is:  ", (cube_length*cube_width*cube_height))
# ---------------------------------------------------

# Question_no5
celsious= 0
fahrenheit= 32
print("Temperature Convertor (Celsius -> fahrenheit)")
temperature = int(input("Enter your temperature in celsius: "))
print("Temperature in Fahrenheit is: ", ((temperature*9/5)+32))

print("Temperature Convertor (fahrenheit -> Celsius)")
temperature = int(input("Enter your temperature in Fahrenheit: "))
print("Temperature in Celsius is: ", ((temperature-32)*5/9))
# ---------------------------------------------------

# Question_no6
minutes= 30
print("Time Calculator (Minutes -> Seconds)")
time_minutes = int(input("Enter your time in minutes: "))
print("Time in seconds is: ", (time_minutes*60))
# ---------------------------------------------------

# Question_no7
percentage= 50
marks= 100
print("Percentage Calculator")
percentage = int(input("Enter your percentage: "))
marks = int(input("Enter your marks: "))
print("Percentage is: ", ((percentage/100)*marks))
# ---------------------------------------------------

# Question_no8
weight= 10
height= 20
print("BMI Calculator")
weight = int(input())
height = float(input())
x = weight/float(height*height)

if x < 18.5:
    print('Underweight')
if x>=18.5 and x<25:
    print("Normal")
if x >= 25 and x < 30:
   print('Overweight')
if x >= 30:
   print('Obesity')
# ---------------------------------------------------

# Question_no8
radius= 4
height= 10
print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))
pie_value = 3.1416

print("Volume of Cylinder is: ", pie_value*(radius**2)*height)
# ---------------------------------------------------