"""
    Question: Given a string containing only round brackets and lowercase characters, remove the least amount of brackets
                so the string is valid.

    Verify the contraints:
        1. We return a valid string with the fewest brackets removed
        2. A string without parenthesis is still valid
        3. It cannot contain a space.
    Test cases:
        1. "a)bc(d)" -> "abc(d)"
        2. "(ab(c)d" -> "(abc)d" or "ab(c)d" 
        3. "))((" -> ""

"""


def minimumRemove(string: str):
    str_array = list(string)
    bracketsToBeRemoved = []
    for i in range(len(string)):
        print(i)
        if str_array[i] == '(':
            bracketsToBeRemoved.append(i)
        elif str_array[i] == ')':
            if len(bracketsToBeRemoved) > 0:
                bracketsToBeRemoved.pop()
            else:
                bracketsToBeRemoved.append(i)
    print(bracketsToBeRemoved)
    if len(bracketsToBeRemoved) > 0:
        for i in bracketsToBeRemoved:
            str_array.pop(i)
    return "".join(str_array)






if __name__ == "__main__":
    testString1 = "a)bc(d)"
    testString2 = "(())"
    testString3 = "))(("

    print(minimumRemove(testString3))