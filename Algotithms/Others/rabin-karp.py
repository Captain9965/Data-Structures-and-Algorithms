""" rabin karp implementation in python: """

d = 10

def search(pattern, text, q):
    """ length of pattern"""
    m = len(pattern)
    """ length of text: """
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    """calculate h: """
    for i in range(m - 1):
        h = (h * d) % q

    """ calculate the hash value of the pattern and text: """
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    """ find the match: """

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern found at position: " + str(i + 1))

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t = t + q

if __name__ == "__main__":
    text = "ABCCDDAEFG"
    pattern = "CDD"
    q = 13
    search(pattern, text, q)



