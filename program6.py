import random
def main():
    my_numbers = [5, 2, 4, 8, 0, 9, -1]
    my_words = ["Winter", "Spring", "Summer", "Fall"]
    
    my_initially_empty_list = []
    my_initially_empty_list.append("first item")
    my_initially_empty_list.append("Second item")
    
    for num in my_numbers:
        print(num, end=" ")
    print() # end of line
    
    print(my_numbers)
    
    my_numbers.append(10)
    print(my_numbers)
    
    #change a exising value
    my_numbers[3] = 17
    print(my_numbers)
    
    #note the error if you access something that isn't there, try changing to 7
    #my_numbers[8] = 24
    
    #if you need to know index where an item came from
    print("elements and indices")
    for i in range (0, len(my_numbers)):  #i would like to know how long this list is (length)
        print(f"{my_numbers[i]} is at index {i}")
    
    print(my_numbers)
    print("add 4 to every spot")
    #add 4 to every element
    for i in range(0, len(my_numbers)):
        my_numbers[i] += 4
        
    print(my_numbers)
    
    
    #generate random numbers
    #my_random_number = random.randint(1,100) #only asked for random number 1 time 
    for i in range(0,len(my_numbers)):
        my_numbers[i] = random.randint(1,100)
        #note that the randint includes both end points, unlike range()
        #the above is 1 to 100 including 100
        
    print(my_numbers)
    
    
main()