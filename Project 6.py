import math
#input: width, length, radius
#action: find area of dough, and single biscuit
#return: round down the total of dough area and single biscuit area
def biscuit_count(width: float, length: float, radius: float) -> float:
    dough_area = (width * length)
    singlebiscuit = cutter_area(radius)
    return math.floor(dough_area / singlebiscuit) 
#input: radius
#action: find area of cutter 
#return: area of cutter 
def cutter_area(radius: float) -> float:
    return (radius**2) * math.pi 


def main():
    width = float(input("What is the width of your dough in inches? "))
    length = float(input("What is the length of your dough in inches? "))
    radius = float(input("What is the radius of your biscuit cutter in inches? "))
    biscuits = biscuit_count(width, length, radius)
    singlebiscuit = cutter_area(radius)
    
    print(f"You have enough dough to make {biscuits} that are {singlebiscuit} square inches each.")
main()