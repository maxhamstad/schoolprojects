
import math
dedef main():

    
    diameter = float(input("Please enter a diameter of can in inches: "))
    height = float(input("Please enter a height of the can in inches: "))
    
    volumecan = (math.pi * ((diameter / 2) ** 2.) * height) 
    volumebox = (diameter ** 2.) * height
    remainder = volumebox % volumecan
   
    print(f"With a diameter of {diameter} inches, and a height of {height} inches,")

    print(f"the can will have a volume of {volumecan} cubic inches")
   
    print(f"and the box will have a volume of {volumebox} cubic inches")
   
    print(f"There will be {remainder} cubic inches of the empty space in the box.")
   
                
mamain()