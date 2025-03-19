def make_name_list(desks, a, b, initals):
    if a != -1 and b != -1:
        desks[a-1][b-1] = initals
    return desks

def get_valid_initals():
    while True:
        initals = input("Please enter 2 initials: ")
        if len(initals) == 2:
            return initals 
def get_valid_row(x):
    while True:
        a = int(input(f"Please enter a row between 1 and {x} (-1 to quit) "))
        if a == -1:
            return a
        if 1 <= a <= x:
            return a
def get_valid_col(y):
    while True:
        b = int(input(f"Please enter a column between 1 and {y} (-1 to quit) "))
        if 1 <= b <= y:
            return b
def all_spots_filled(desks):
    for row in desks:
        if "--" in row:
            return False
    return True 
def main():
    x = int(input("how many rows are there? "))
    y = int(input("How many columns are there? "))
    desks = [["--" for col in range(y)] for row in range(x)]
    runtime = 0
    while not all_spots_filled(desks):
        a = get_valid_row(x)
        if a == -1:
            print("goodbye")
            break
        b = get_valid_col(y)
        initals = get_valid_initals()
        desks = make_name_list(desks, a, b, initals)
        print("\nCurrent desk layout:")
        for row in desks:
            for col in row:
                print(col, end=" ")
            print()
        runtime = runtime + 1

    
main()