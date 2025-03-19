def main():
    n = int(input(" Please enter a number between 2 and 20: "))
    if (n < 2 or n > 20):
        print("please ener a difrent number")
        print("")
    
    else:
        print("     |", end=" ")
        for i in range (1, n + 1):
            print(f"{i:2}", end=" ")
        print()
        print("----" * (n + 1))
    
        for i in range (1, n + 1):
            print(f"{i:2d}   |", end=" ")
            for a in range (1, n + 1):
                multiply= i * a 
                print(f"{multiply:2d}", end=" ")
            print()
        
    
    
    
    
main()