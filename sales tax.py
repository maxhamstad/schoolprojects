def main():
    purchasetotal = float(input("Please enter your purchase total: "))
    
    Totalcost = (purchasetotal *.08375) + purchasetotal
    
    print(f"For a purchase of ${purchasetotal}, you will have a sales tax of $8.375 for a total of ${Totalcost}.")

main()