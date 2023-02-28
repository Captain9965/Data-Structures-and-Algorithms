""" 
    Given 2 strings S and T, determine whether the two strings are equal if they are typed out. a 3 is a backspace

    verify the constraints:
        1. can we contain one of the strings as empty?..yes
        2. Can we contain 2 consecutive ##?..yes
        3. What happens to 3 when there are no characters to remove? nothing...I guess.
        4. case sensitivity matters? ...yes

    test cases:
        1. "" and ""-> true
        2. "ab#z" and "az#z" -> true
        3. "a#b#r#" and "a#" -> true
        4. "a####b" and "b" -> true

        1. "abc#d" and "acc#d" -> false
        2. "Ab#z" and "ab#z" -> false
    logical solution ( Brute force ):
        1. Process each string, removing all #
        2. compare lengths and if they are equal, go into the next stage. If not, return false.
        3. compare values from the first one until a difference is found. If so, return false.
        4. Else return true.
"""


""" 
    time complexity is O(a + b)
    space complexity is O(a + b)

"""
def isEqual_brute_force(string1: str, string2: str): 
    """ process the 2 strings"""
    index1 = 0
    l1 = len(string1)
    stringlist1 = []

    while(index1 < l1):
        if (string1[index1] != '#'):
            stringlist1.append(string1[index1])
        else:
            """ do nothing if we are already at the end, """
            if stringlist1:
                stringlist1.pop()
        index1 += 1
  

    index2 = 0
    l2 = len(string2)
    stringlist2 = []

    while(index2 < l2):
        if (string2[index2] != '#'):
            stringlist2.append(string2[index2])
        else:
            """ do nothing if we are already at the end, """
            if stringlist2:
                stringlist2.pop()
        index2 += 1
    
    """ compare: """

    if len(stringlist1) == len(stringlist2):
        for i in range(len(stringlist1)):
            if (stringlist1[i] != stringlist2[i]):
                return False
    else:
        return False

    return True

""" lets reduce the space complexity by using the 2 pointer technique:
    time complexity is O(a + b)
    space complexity is O(1)

 """

def isEqual_2pointer(string1: str, string2: str):
    pointer1 = len(string1) - 1
    pointer2 = len(string2) - 1
    


    while(pointer1 >= 0  or pointer2 >= 0):
        if ((string1[pointer1] == '#' and pointer1 >= 0) or (string2[pointer2] == '#' and pointer2 >= 0)):
            if (string1[pointer1] == '#' and pointer1 >= 0):
                bck_space_count = 2

                while(bck_space_count > 0):
                    pointer1 -= 1
                    bck_space_count -= 1
                    if (pointer1 < 0):
                        continue
                    if (string1[pointer1] == '#'):
                        bck_space_count += 2

            if (string2[pointer2] == '#' and pointer2 >= 0):
                bck_space_count2 = 2

                while(bck_space_count2 > 0):
                    pointer2 -= 1
                    bck_space_count2 -= 1
                    if pointer2 < 0:
                        continue
                    if (string2[pointer2] == '#'):
                        bck_space_count2 += 2
        else:            
            """ if it is not a backspace character, process any pending backspaces:"""
            print(f"pointer 1 -> {pointer1}  pointer 2 -> {pointer2}")
            if pointer1 < 0:
                return False
            if pointer2 < 0:
                return False
            if (string1[pointer1] != string2[pointer2]):
                return False
            else:
                pointer2 -= 1
                pointer1 -= 1
    
    
    return True


if __name__ == "__main__":
    string1 = "###c##d"
    string2 = "abd"

    print("equal") if isEqual_2pointer(string1, string2) else print("not equal")





