def main():
    Q1 = input("What type of animal is your pet? ").lower()
    Q2 = input(f"Is your {Q1} Male for Female? ").lower()
    
    if Q1 == "dog":
        print("male dogs are mammals and eat meat")
    elif Q1 == "cat":
        print("male cats are mammals and eat meat")
    elif Q1 == "hamster":
        print("male hamsters are mammals, omnivores, live in cages")
    elif Q1 == "fish":
        if Q2 == "male":
            print("male fish have scales, do not lay eggs")
        else:
            print("female fish have scales, and do lay eggs")
    elif Q1 == "snakes":
        if Q2 == "male":
            print("male snakes eat meat, have scales, live in cages, and do not lay eggs")
        else:
            print("female snakes eat meat, have scales, live in cages, and do lay eggs")
    else:
        if Q2 == "male":
            print("male birds live in cages")
        else:
            print("female birds live in cages, and lay eggs")
    
main()