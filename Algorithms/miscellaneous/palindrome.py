""" A palindrome is a string that reads the same forwards and backwards.
    eg, "aba", "a", "race car", "", "A man, a plan, a canal: Panama" 

    Almost all the time, the string is not case, space or symbol sensitive
    There are 3 techniques to solve this-> 
        1. Center beginning 2 pointer technique
        2. End beginning 2 pointer technique
        3. reverse string 2 pointer technique

    Question: given a string, determine if its a palindrome, considering only alphanumeric characters and ignoring case
                sensitivity
    Test cases:
        1. "aabaa" -> true
        2. "aabbaa"-> true
        3. "abc" -> false
        4. "a" -> yes
        5. "A man, a plan, a canal: Panama" -> yes
        6. "" -> true

    - Then remove all non-alphanumeric characters: 
        use regex matching for this
"""
import re

def isValidPalindrome(string: str):
    string = re.sub("[^0-9A-Za-z]",'', string)
    print(string)
    
    pointer1 = 0
    pointer2 = len(string) - 1

    """ if odd: """
    
    while(pointer1 < pointer2):
        if(string[pointer1] == string[pointer2]):
            pointer2 -= 1
            pointer1 += 1
        else:
            return False
        
    return True

if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    if(isValidPalindrome(string)):
        pointer