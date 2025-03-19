def main():
    num1 = int(input("Please enter a integer: "))
    num2 = int(input("Please enter a integer: "))
    #you have one if and one else, and as many elifs in the middle as possible
    if num1 < num2:
        print("first number is smaller")
    elif num1 > num2:
        print("First number is bigger")
    else:
        print("Numbers are equal")

main()