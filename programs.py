num = int(input("Please enter a positive integer: "))
if num < 1:
    print("I said a positive integer!")
    exit()
prime = num > 1
for i in range(2, num):
    if num % i == 0:
        prime = False;
if prime:
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")