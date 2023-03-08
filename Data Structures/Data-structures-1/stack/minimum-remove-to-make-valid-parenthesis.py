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