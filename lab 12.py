def main():
     getint = int(input("How many numbers do you plan to enter: "))
     numbers = []
     n = 0
     for i in range(1, getint + 1):
        n = n + 1
        num = int(input(f"give me number {n}: "))
        numbers.append(num)
     print(f"Your list is: ", end=" ")
     for num in numbers:
         print(f"{num} ", end=" ")
     print()
     
     largest = numbers[0]
     for num in numbers:
         if num > largest:
             largest = num
     print(f"largest value is {largest}")
     
main()

