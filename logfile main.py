from datetime import datetime #so we can call now() below

def main():
    filename = "logfile.txt"
    outfile = open(filename, 'w')
    
    while True: #keep going as long as true (its always true) break or return stops this
        fname = input("please enter your first name ")
        lname = input("please enter your last name: ")
        rating = -1
        while rating < 0 or rating > 5:
            rating = int(input("Please enter your rating out of 5: "))
        outfile.write(f"{datetime.now()} {fname} {lname} {rating} \n")
        more = input("do you have another rating? (yes/no) ")
        if more.lower() == "no":
            break
    outfile.close()
main()
                         
        
        