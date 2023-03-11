"""
    Given a string containing only parenthesis, determine if the input string is valid.

"""

"""

    space analysis -> O(n)
    time analysis -> O(n)
"""

def isValid(string: str):
    bracket_pairs = {'(': ')', '{':'}', '[': ']'}
    opening_brackets = []

    for i in string:
        if bracket_pairs.get(i):
            opening_brackets.append(i)
        else:
            if len(opening_brackets):
                last_saved = opening_brackets.pop()
                if i != bracket_pairs.get(last_saved):
                    return False
            else:
                return False 
    
    return len(opening_brackets) == 0
    
     

if __name__ == "__main__":
    testCase1 = "(())"
    testCase2 = "{(]}"
    testCase3 = ""
    testCase4 = "{[)]}"
    testCase5 = "()"

    print(isValid(testCase5))