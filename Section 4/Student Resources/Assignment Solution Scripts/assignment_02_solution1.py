# Assignment 2 Solution

# Subjects wit scores
# ** NOTE: Nothing is stopping you from entering - 101 or 120 or -20 or ten or london
circle_radius = float(input("Enter the radius of the circle : \t"))

pi_value = 3.14
circle_area = pi_value * (circle_radius ** 2)
circle_perimeter = 2 * pi_value * circle_radius

# This is not the best way to format output.
# We will learn more when learning about strings.
print()
print("****************************************")
print("       Circle Information")
print("****************************************")
print(" The Area of the circle : \t\t", circle_area)
print(" The perimeter of the circle : \t", circle_perimeter)

# Perform test runs with 10, 5, 5.5