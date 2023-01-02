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


import os


wrkng_dir = "C:\\Users\\rootp\\Documents\\Code\\Python\\DailyProgrammer\\Chal. No. 399 - Letter Value Sum"
data_file = "enable1.txt"


alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, \
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, \
        'w': 23, 'x': 24, 'y': 25, 'z': 26}

input_data = ["", "a", "z", "cab", "excellent", "microspectrophotometries"]




"""
    Global function definitions
"""
def sum_of_chars(char_string):
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
    



"""
    void main();
"""
# Open our data file and error handle
try:
    fd = open(wrkng_dir + "\\" + data_file)
except FileNotFoundError:
    print("FileNotFoundError: No such file or directory: " + data_file)
   
    
    
    
# Loop input_data and print out string sums
i = 0
for word in fd:
    """ 1). microspectrophotometries is the only word with a letter sum of 317. 
            Find the only word with a letter sum of 319."""
    if len(word) == 319:
        print(word + " => " + str(len(word)))

    
    """ 2). How many words have an odd letter sum?"""
    
    
    
    """ 3). There are 1921 words with a letter sum of 100, making it the second 
            most common letter sum. What letter sum is most common, and how many 
            words have it?"""
    
    
            
    """ 4). zyzzyva and biodegradabilities have the same letter sum as each other 
            (151), and their lengths differ by 11 letters. Find the other pair of 
            words with the same letter sum whose lengths differ by 11 letters."""

            
          
    """ 5). cytotoxicity and unreservedness have the same letter sum as each other 
            (188), and they have no letters in common. Find a pair of words that 
            have no letters in common, and that have the same letter sum, which is 
            larger than 188. (There are two such pairs, and one word appears in 
            both pairs.)"""


  
    """ 6). The list of word { geographically, eavesdropper, woodworker, oxymorons } 
    contains 4 words. Each word in the list has both a different number of letters, 
    and a different letter sum. The list is sorted both in descending order of word 
    length, and ascending order of letter sum. What's the longest such list you can 
    find?"""