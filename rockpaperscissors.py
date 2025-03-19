def main():
    p1 = input("What is player 1's move? ").lower()
    p2 = input("What is player 2's move? ").lower()
    
    if p1 == p2:
        print("tie game")
    
    elif(p1 == "rock" and p2 == "scissors"
        or p1 == "scissors" and p2 == "paper"
        or p1 == "paper" and p1 == "rock"):
        print("player 1 wins")
        
    else: #all other situations player 2 wins 
        print("player 2 wins")
         
main()