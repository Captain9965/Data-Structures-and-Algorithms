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