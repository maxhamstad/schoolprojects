import math
def main():
    integer = int(input("Please enter a number between 0 and 255, -1 to quit: "))
    if (integer < 0 and integer != -1 or integer > 255):
        print("please ener a differnet number")
    elif (integer > 0 and integer < 255):
        
        print("In binary: ", end= "")
        for i in range (7, -1, -1):
            power = 2 ** i
            if power > integer:
                print("0", end= "" )
            else:
                print("1", end="" ) 
                integer = integer - power
    else:
        print("goodbye")
              
main()



for i in range (1, n + 1):
        print(" ",i,end=" ")
    print()
    for i in range (1, n + 1):
        number = 1
        number = number * i
        print(f"{number}")
        print()