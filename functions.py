 # Alexander
# Dec 12
# functionz
import math

def cheese():
    '''Makes a screen full of i like cheeses!'''
    print("I like cheese! " * 100)

def temp_C(temp_F):
    '''Converts a temperature in Fahrenheit to Celsius'''
    answer = (temp_F - 32) * (5/9)
    return answer

def sphere_v(radius):
    '''Calculates the volume of a sphere'''
    volume = (4/3)*math.pi*r**3
    return volume

cheese()

t_in_C = temp_C(float(input("Please enter a temperature in Fahrenheit. ")
))
print("That temperature in Celsius is ", t_in_C, ".")

r = float(input("Please enter a radius of a sphere. "))
print("The volume of the sphere is ", sphere_v(r))

