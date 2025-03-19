# test if a input is even or odd

def main():
    number = int(input("please enter a integer "))
    
    if number % 2 == 0: #divide by 2 check if the remainder is 0
        print(f"{number} is an even number ")
    else:
        print(f"{number} is a odd number ")
        
        
    
main()