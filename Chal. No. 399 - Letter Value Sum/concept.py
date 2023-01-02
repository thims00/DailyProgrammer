#!/usr/bin/env Python3

"""
Assign every lowercase letter a value, from 1 for a to 26 for z. 
Given a string of lowercase letters, find the sum of the values of the letters in the string.

lettersum("") => 0
lettersum("a") => 1
lettersum("z") => 26
lettersum("cab") => 6
lettersum("excellent") => 100
lettersum("microspectrophotometries") => 317
"""




wrkng_dir = "C:\\Users\\rootp\\Documents\\Code\\Python\\DailyProgrammer\\Chal. No. 399 - Letter Value Sum"
data_file = "sample.txt"

alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, \
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, \
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

input_data = ["", "a", "z", "cab", "excellent", "microspectrophotometries", "zyzzyva", "biodegradabilities"]




def lettersum(char_string):
    """ Loop over the chars of char_string, sum up the numeric representation, and return.
    
            Returns:
                Success: sum of chars in char_string
                Error: 1 (Most commonly a typeError due to numbers or symbols)
    """
    char_sum = 0

    # Must be a string type
    try:
        str(char_string)
        
    except:
        print("TypeError: sum_of_chars expected string, got other.")
        return 1

    # Loop the provided string and add sums
    for i in range(len(char_string)):
        # Ensure characters are acceptable chars in alph dict
        try:
            char_sum += alph[char_string[i]]
        except:
            print("TypeError: provided string contains unacceptable characters.")
            return 1
            
    return char_sum
    

# Loop input_data and print out string sums
fd = open(wrkng_dir + "\\" + data_file, "r")

for word in fd: #range(len(input_data)):
    word = word.strip("\n")
    print(word + " => " + str(lettersum(word)))

fd.close()