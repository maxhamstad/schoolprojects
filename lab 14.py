
#input: x a number
#action: take number, divide by 2
#return: if number has remainder 0, return true, if not false 
def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False 
 #input: x a number
#action: is this prime number, do math to determine it 
#return: if divisible false, if not true 
def is_prime(x: int) -> bool:
    if x <= 1:
        return False 
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def main():
    x = int(input("please enter a integer "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} not even")
    if is_prime(x):
        print(f"{x} is prime")
    else:
        print(f"{x} not prime")
        
main()
        
    
    