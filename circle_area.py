# Program to calculate area of a circle
import math

# Accept radius input from the user
radius = float(input("Input the radius of the circle : "))

# Calculate area using formula πr^2
area = math.pi * radius * radius

# Display result
print(f"The area of the circle with radius {radius} is: {area}")
