import random
add_sign = 0
parity_score = 0
loop_time = 0
while (parity_score < 10 and add_sign < 10):
    loop_time = loop_time + 1
    random_number = random.randint(-100, 101)
    print(f"Random number {loop_time} is: {random_number}")
    if (random_number % 2 == 0):
        parity_score = parity_score + 1
        print("Parity Player scores for Even Number")
        print(" ")
    if (random_number >= 1):
        add_sign = add_sign + 1
        print("Sign Player scores for Positive Number")
        print(" ")
    else:
        print(" ")
print(f"After {loop_time} turns, Parity Player: {parity_score}, Sign Player: {add_sign}")
if (add_sign == 10 and parity_score < 10):
    print("Sign Player Wins")
elif (parity_score == 10 and add_sign < 10):
    print("Parity Player Wins")
else:
    print("Tie Game")
    
