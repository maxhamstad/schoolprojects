def main():
    Q1 = input("Is it cold outside? ").lower()
    Q2 = input("Are you tired? ").lower()
    
    if Q1 == "yes": 
        if Q1 == Q2:
            print("you should stay inside and read a book") 
        else: 
            print("Go skiing")
            
    else:
        if Q2 == "yes":
            print ("you should take a nap")
        
        else:
            print("then go running") 
        
main()
