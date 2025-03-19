def main():
    n = int(input("What do you want to be the maximum capacity of your list? \n"))
    wordlist = []
    i = 0
    while n > i:
        i = i + 1
        word =input("Please enter a word to add to the list: \n")
        wordlist.append(word)
        if len(wordlist) == 1:    
            print(f"The current list is: \n{wordlist[0]}.")
        elif len(wordlist) == 2:
            print(f"The current list is: \n{wordlist[0]} and {wordlist[1]}.")
        elif len(wordlist) == 3:
            print(f"The current list is: \n{wordlist[0]}, {wordlist[1]}, and {wordlist[2]}.")
        else:
            print(f"The current list is: {', '.join(wordlist[:-1])} and {wordlist[-1]}.")
            #had to look up how to do the join function, couldn't figure out any other way to do it 
    print("goodbye")
main()