def main():
    Q1 = input("Is it cold outside? ").lower()
    Q2 = input("Are you tired? ").lower()
    
    if (Q1 == "yes" and Q2 == "yes"):
        print("stay inside and read")
        
    elif(Q1 == "yes" and Q2 == "no"):
        print("go skiing")
        
    elif(Q1 == "no" and Q2 == "yes"):
        print("take nap outside")
        
    else:
        print("go running")
        
main()