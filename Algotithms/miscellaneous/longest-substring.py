""" given a string, find the length of the longest substring without repeating characters: 
    hint: may use the sliding window technique.
    1. verify constraints:
        1. Is the string contiguous(sequential with no breaks between them) ?..yes.look for a substring and not a subsequence..
        2. does case sensitivity matter?..no assume all are in lower case.
    2. Test cases:
        "abccabb" -> 3
        "cccc" -> 1
        "" -> 0
        "abcbda" -> 4

    3. Here, I have used the window technique that allows me to process each element, only once -> O(n)

"""

""" Time complexity is -> O(n)
    Space complexity -> O(n)
"""
def longest_unique_substring(string):
    if len(string) <= 1:
        return len(string)
    
    max_length = 0
    pointer1 = 0
    pointer2 = 0
    seen_chars = {}

    while(pointer2 < len(string)):
        """first check whether we have seen this letter before: """
        position = seen_chars.get(string[pointer2])

        """ seen, it is either a duplicate character or a character seen before but with a position pointer 1 has passed:"""
        if position is not None:
            if (position >= pointer1):
                pointer1 = position + 1
            seen_chars[string[pointer2]] = pointer2    
        else:
            seen_chars[string[pointer2]] = pointer2
        max_length = max((pointer2 - pointer1) + 1, max_length) 
        pointer2 += 1
    return max_length

""" sliding window technique:

    form a window over some portion of sequential data, then move that window throughout the data to 
    capture different parts of it.

"""

if __name__ == "__main__":
    test1 = "abcbda"
    test2 = "abccabb"
    test3 = "bbbbb"
    test4 = "abcdef"
    test5 = ""
    test6 = " "
    test7 = "r"
    print(longest_unique_substring(test4))
