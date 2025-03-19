"""
def GCD(a: int, b: int) ->int:
    if b == 0:
        return a
    return GCD(b, a % b)
print(GCD(8, 10)) 


def fib_non_rec(n:int) -> int:
    if n < 3:
        return 1
    
    FibT = []
    fibT.append(1)
    fibT.append(1)
    for i in range (2, n):
        fibT.append(fibT[i -1] +fibT[i -2])
    return fibT[n-1]
                    
                    
def main(): 
    a = int(input("number: "))
    b = int(input("number: "))
    fib = GCD(a,b)
    print(fib)
main()
    """
"""more recursion work"""
"""
def is_power_of_2(num: int) -> bool:
    if num == 1:
        return True
    if num <= 0:
        return False
    if num % 2 != 0:
        return False
    #if we divide by 2 we have a remainder of 0 we are still running
    return is_power_of_2(num // 2)
for i in range(17):
    if is_power_of_2(i):
        print(f"{i} is a power of 2")
    else:
        print(f"{i} is not a power of 2")
"""

"""
from typing import List
def sequential_search(arr: List[str], target: str, cur_index: int = 0) -> int:
    if cur_index >= len(arr):
        return -1 # we ran out of places to look
    if arr[cur_index] == target:
        return cur_index # we found it on firrst try
    return sequential_search(arr, target, cur_index + 1)

my_list = ['Jan', 'feb', 'mar', 'apr']
print(f"search for mar: {sequential_search(my_list, 'mar')}")
print(f"search for may: {sequential_search(my_list, 'may')}")
"""
"""
def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[len(s)-1]:
        return False #first and last letters dont match
    return is_palindrome(s[1:-1])# slice off first and last letters
print(f"testing for plaindrome: racecar - {is_palindrome('racecar')}")
print(f"testing for plaindrome: detartrated - {is_palindrome('detartrated')}")
print(f"testing for plaindrome: abcdegf - {is_palindrome('abdcdegf')}")
print(f"testing for plaindrome: nathan - {is_palindrome('nathan')}")
"""

def repeat(c: str, num: int) -> str:
    if num == 0:
        return "" #base case empty string
    return str(repeat(c, num - 1) + c)
print(f"repeat a 6 times: {repeat('a',6)}")

def repeatTricky(c: str, num: int) -> str:
    if num == 0:
        return ""
    result = repeatTricky(c, num - 1) + c
    print(result)
    return result 
print(f"repeat a 6 times: {repeatTricky('a',3)}")
       
    

    
