# Backtracking algorithm:

This is a problem-solving algorithm that solves problems by brute force to find the desired output. The brute force approach tries out all the possible solutions and chooses the best/desired solutions. If a solution is not suitable, then back track and try other solutions. Hence, recursion is used. This approach is used to solve problems that have multiple solutions.

```
Algorithm:
Backtrack(x)
    if x is not a solution
        return false
    if x is a new solution
        add to list of solutions
    backtrack(expand x)
```
A way to represent this would be a state space tree representing all possible states of a problem from the root as an initial state to the leaf as a terminal state.

# Rabin Karp algorithm:

This is an algorithm used for searching/matching patterns in the text using a hash function. Unlike Naive string matching algorithm, it does not travel through every character in the initial phase rather it filters the characters that do not match and then performs the comparison.

## Working:
A sequence of characters is taken and checked for the possibility of the prescence of the required string. If a possiblity is found, then character matching is performed.

1. Assign a `numerical value(v)/weight` for the characters we will be using in the problem.
2. let `n` be the length of the pattern and `m` the length of the text. let `d` be the input set. 
3. Calculate the hash value of the pattern. Given by:
    ```
    hash value for pattern(p) = Σ(v * dm-1) mod 13 
                        = ((3 * 102) + (4 * 101) + (4 * 100)) mod 13 
                        = 344 mod 13 
                        = 6
    ```     
    In the calculation above, choose a prime number such that, we can perform all the calculations with single precision arithmetic.
4. Calculate the hash value of the text window of size `m`
    ```
    For the first window ABC,
    hash value for text(t) = Σ(v * dn-1) mod 13 
                    = ((1 * 102) + (2 * 101) + (3 * 100)) mod 13 
                    = 123 mod 13  
                    = 6
    ```
5. Compare the hash value of the pattern and the hash value of the text. If they match, then character matching is performed. In the above instance, the hash value of the first window `t`, matches with `p` so go for character matching between  ABC and CDD. Since they do not match, go for the next window.

6. We calculate the hash value of the next window by subtracting the first term and adding the next term as shown:
    ```
    t = ((1 * 102) + ((2 * 101) + (3 * 100)) * 10 + (3 * 100)) mod 13 
     = 233 mod 13  
     = 12
    ```
    To optimize the process, we make use of the previous hash function as shown below:
    ```
    t = ((d * (t - v[character to be removed] * h) + v[character to be added] ) mod 13  
    = ((10 * (6 - 1 * 9) + 3 )mod 13  
    = 12
    Where, h = dm-1 = 103-1 = 100.
    ```
7. If this does not match, we move to the next window where we will hopefully get a match.

## Algorithm:
```
n = t.length
m = p.length
h = dm-1 mod q
p = 0
t0 = 0
for i = 1 to m
    p = (dp + p[i]) mod q
    t0 = (dt0 + t[i]) mod q
for s = 0 to n - m
    if p = ts
        if p[1.....m] = t[s + 1..... s + m]
            print "pattern found at position" s
    If s < n-m
        ts + 1 = (d (ts - t[s + 1]h) + t[s + m + 1]) mod q
```

## Limitations of Rabin Karp algorithm:
### suprious hit:
This is when the hash value of the pattern matches with the hash value of a window of the text. Hence why we use modulus to minimize the spurious hits.

## Complexity:
The average case and best case complexity is `O(m + n)` and the worst case complexity is `O(mn)`

## Applications:
1. Pattern matching.
2. Searching a string in a bigger text.





    