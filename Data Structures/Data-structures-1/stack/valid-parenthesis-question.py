"""
    Given a string containing only parenthesis, determine if the input string is valid.

"""

def isValid(string: str):
    pointer1 = 0
    pointer2 = len(string) - 1

    while (pointer1 < pointer2):
        if (string[pointer1] != string[pointer2]):
            print(pointer1, pointer2)
            print(string[pointer1], string[pointer2])
            return False
        else:
            pointer2 -= 1
            pointer1 += 1
    return True

if __name__ == "__main__":
    testCase1 = "(())"
    testCase2 = "{(]}"
    testCase3 = ""
    testCase4 = "{[)]}"

    print(isValid(testCase1))