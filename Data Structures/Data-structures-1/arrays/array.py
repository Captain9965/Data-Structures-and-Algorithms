
import math
strings = ['a', 'b', 'c', 'd']

#O(1) operation
print(strings[0])  

#pop -> O(1)
strings.pop()

#push ->O(1)

strings.append("r")
print(strings)

#insert->O(n) because we have to iterate through the data structure and reassign the indices
strings.insert(0, '4')
print(strings)

#middle insert -> O(n)
strings.insert(math.floor(len(strings) / 2), 'y')
print(strings)

