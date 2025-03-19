def reverse_string(input: str) -> str:
    if input == "":
        return ""
    if input == [0]:
        return [0]
    return input[-1] + reverse_string(input[:-1])
print(f"{reverse_string('Reversing the string')}")

def has_factors_2_and_3(number: int) -> bool:
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    if number % 3 == 0:
        return has_factors_2_and_3(number // 3)
    if number % 2 == 0:
        return has_factors_2_and_3(number // 2)
    else:
        return False 
print(f"{has_factors_2_and_3(486)}")
    
        