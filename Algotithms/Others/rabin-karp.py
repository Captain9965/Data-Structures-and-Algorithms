""" rabin karp implementation in python: """

d = 256 #number of characters in the input alphabet

def search(pattern, text, q):
    """ length of pattern"""
    m = len(pattern)
    """ length of text: """
    n = len(text)
    p = 0  # hash value for pattern
    t = 0   # hash value for text
    h = 1
    i = 0
    j = 0

    """The value of h would be "pow(d, M-1)%q" """
    for i in range(m - 1):
        h = (h * d) % q

    """ calculate the hash value of the pattern and first window of text: """
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    """ slide the pattern over text one by one:  """

    for i in range(n - m + 1):
        """
        Check the hash values of current window of text and
        pattern if the hash values match then only check
        for characters one by one
        """
        if p == t:
            """check for the characters one by one: """
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            """if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]"""
            if j == m:
                print("Pattern found at position: " + str(i + 1))
        """
        calculate the hash value of the next window of text. Remove the leading digit and 
        add trailing digits: 
        """
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            """we might get negative values of t, converting it into positive: """
            if t < 0:
                t = t + q

if __name__ == "__main__":
    text = "ABCCDDAEFG"
    pattern = "CDD"
    q = 13
    search(pattern, text, q)



