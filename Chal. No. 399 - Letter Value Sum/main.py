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
data_file = "enable1.txt"

debug = False
debug_file="debug.txt"


alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, \
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, \
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}




"""
    Global function definitions
"""
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
        print("TypeError: lettersum() expects string, got other.")
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
    fd = open(wrkng_dir + "\\" + data_file, "r")
    if debug:
        bd = open(wrkng_dir + "\\" + debug_file, "w")
except FileNotFoundError:
    print("FileNotFoundError: No such file or directory: " + data_file)


# Loop input_data and populate information
""" word_struct = {} - Data Structure
    
    word_struct = {"word_sum" : [qty, ["word1", "word2", "word3", "etc"],
                   "5"        : [2, ["hello", "world"]],
                   "7"        : [3, ["empathy", "matress", "earlier"]],
                   "2"        : [6, ["to", "of", "we", "no", "be", "at"]]
                  } """
word_struct = {}
odd_lttrs = 0


for word in fd:
    word_sum = lettersum(word.strip("\n"))


    """ 1). microspectrophotometries is the only word with a letter sum of 317. 
            Find the only word with a letter sum of 319."""
    if word_sum == 319:
        print("1) Find the only word with a letter sum of 319: ", end="")
        print(word + " => " + str(len(word)))

    
    """ 2). How many words have an odd letter sum? - preprocessing"""
    if (word_sum % 2) == 1:
        odd_lttrs += 1
    
    
    # Populate our data structure for post processing
    if not word_struct.get(str(word_sum)):
        word_struct[str(word_sum)] = [0, []]
        
    word_struct[str(word_sum)][0] += 1
    word_struct[str(word_sum)][1].append(word.strip("\n"))


if debug:
    for key in word_struct.keys():
        bd.write("\"" + str(key) + "\"")
        bd.write(" => [" + str(word_struct[str(key)][0]))
        bd.write(", " + str(word_struct[str(key)][1]) + "]")
        bd.write("\n")




""" 2). How many words have an odd letter sum? - postprocessing"""
print("2) How many words have an odd letter Sum: ", end="")
print(odd_lttrs)
    
    
""" 3). There are 1921 words with a letter sum of 100, making it the second 
        most common letter sum. What letter sum is most common, and how many 
        words have it?"""
ceil = 0
ceil_id = 0

# Loop data structure and seek most common letter sum
for key in word_struct.keys():  
    if word_struct[key][0] > ceil:
        ceil = word_struct[key][0]
        ceil_id = key
                
print("3) What letter sum is most common, and how many words have it: ")
print("    Most common: ", end="")
print(ceil_id)
print("    Word Qty: ", end="")
print(ceil)

        
""" 4). zyzzyva and biodegradabilities have the same letter sum as each other 
        (151), and their lengths differ by 11 letters. Find the other pair of 
        words with the same letter sum whose lengths differ by 11 letters."""
# TODO: This approach is ignorant, takes awhile and very redundant
smllr = []
lrgr = []
for letter_sum in word_struct:
    for eleven in word_struct[letter_sum][1]:
        elev_len = len(eleven)
        
        for word in word_struct[letter_sum][1]:
            word_len = len(word)
            

            if (len(word) - len(eleven)) == 11:
                smllr.append(eleven)
                lrgr.append(word)

print("4) Find the other pair of words with the same letter sum ")
print("   whose lengths differ by 11 letters: ", end="")
print(str(smllr[1]) + " and " + str(lrgr[1]))

if debug:
    print("No. 4 Debug:")
    print(smllr)
    print(lrgr)


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
        
        
        
        
        
if debug:
    bd.close()
fd.close()