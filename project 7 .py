#input: count 
#action: find letters that are not used 
#return:  index of unused letters 
def not_used_number(count):
    not_used = []
    for i in range(26):
        if count[i] == 0:
            not_used.append(chr(i + ord("a")))
    return not_used
#input: count 
#action: find letters that are most used 
#return:  most common letter  
def common_number(count):
    max_count = 0
    most_common_index = -1 
    for i in range(26):
        if count[i] > max_count:
            max_count = count[i]
            most_common_index = i
    most_common_letter = chr(most_common_index + ord("a"))
    return most_common_letter

def main():
    text = input("Please enter a sentence: ").lower()
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for c in text:
        if 97 <= ord(c) <= 122:
            index = ord(c) - ord("a")
            count[index] += 1
    print("letter counts: ")
    for i in range(26):
        letter = chr(i + ord("a"))
        print(f"{letter}: {count[i]}", end =" ")
    print()
    mostcommon = common_number(count)
    print(f"the most common letter is: '{mostcommon}'")
    notusednumber = not_used_number(count)
    print(f"the following letters were not used: ", end=" ")
    for letter in notusednumber: 
        print(letter, end=" ")
main()