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
    position = 0
    i = 0
    while i < len(string):
        if str_array[position] == '(':
            bracketsToBeRemoved.append(position)
            position += 1
        elif str_array[position] == ')':
            if len(bracketsToBeRemoved) > 0:
                bracketsToBeRemoved.pop()
                position += 1
            else:
                str_array.pop(position)
        else:
            position += 1
        i += 1
    while len(bracketsToBeRemoved) > 0:
        str_array.pop(bracketsToBeRemoved.pop())
    return "".join(str_array)


"""
    time complexity -> O(n)
    space complexity -> O(n)

"""
def minimumRemovev2(string:str):
    str_array = list(string)
    bracketsToBeRemoved = []
   
    for position in range(len(string)):
        if str_array[position] == '(':
            bracketsToBeRemoved.append(position)
        elif str_array[position] == ')':
            if len(bracketsToBeRemoved):
                bracketsToBeRemoved.pop()
                
            else:
                str_array[position] = ''
    while len(bracketsToBeRemoved):
        str_array[bracketsToBeRemoved.pop()] = ''
    return "".join(str_array)






if __name__ == "__main__":
    testString1 = "a)bc(d)"
    testString2 = "(())"
    testString3 = "))(("

    print(minimumRemovev2(testString1))