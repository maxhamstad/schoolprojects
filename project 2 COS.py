def main():
    Q1 = input("Do you have an MN Driver's License? ").lower()
    if Q1 == "yes":
        Q2 = input("Does your Driver's License list a valid address for this precinct? ").lower()
        if Q2 == "yes":
            print("You can register to vote!")
        else:
            Q3 = input("Do you have a student ID from a Minnesota University or College? ").lower()
            if Q3 == "yes":
                print("You can register to vote!")
            else:
                Q4 = input("Do you have a phone bill with your name and address due within 30 days? ").lower()
                if Q4 == "yes":
                    print("You can register to vote!")
                else:
                    Q5 = input("Do you have a rent statement with your name and address due within 30 days? ").lower()
                    if Q5 == "yes":
                        print("You can register to vote!")
                    else:
                        print("Sorry, you can't register to vote.")
    if Q1 == "no":
        Q6 = input("Do you have a student ID from a Minnesota University or College? ").lower()
        if Q6 == "yes":
            Q7 = input("Do you appear on the housing list provided by your college to the election officials? ").lower()
            if Q7 == "yes":
                    print("You can register to vote!")
            else:
                Q8 = input("Do you have a phone bill with your name and address due within 30 days? ").lower()
                if Q8 == "yes":
                    print("You can register to vote!")
                else: 
                    Q9 = input("Do you have a rent statement with your name and address due within 30 days? ").lower()
                    if Q9 == "yes":
                        print("You can register to vote!")
                    else:
                        Q10 = input("Do you have student fee statement with your name and address due within 30 days? ").lower()
                        if Q10 == "yes":
                            print("You can register to vote!")
                        else:
                            print("Sorry, you can't register to vote.")
    
        if Q6 == "no":
            Q11 = input("Do you have a US Passport? ").lower()
            if Q11 == "yes":
                Q12 = input("Do you have a phone bill with your name and address due within 30 days? ").lower()
                if Q12 == "yes":
                    print("You can register to vote!")
                else:
                    Q13 = input("Do you have a rent statement with your name and address due within 30 days? ").lower()
                    if Q13 == "yes":
                        print("You can register to vote!")
                    else:
                        Q14 = input("Do you have student fee statement with your name and address due within 30 days? ").lower()
                        if Q14 == "yes":
                            print("You can register to vote!")
                        if Q14 == "no":
                            print("Sorry, you can't register to vote.")
            else:
                print("Sorry, you can't register to vote.")
main()