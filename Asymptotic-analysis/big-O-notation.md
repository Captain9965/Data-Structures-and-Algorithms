# Big-O-notation: 
Good code can be described as:
- readable
- scalable --> big-O helps us to measure and achieve this.

It is a standard way for us to measure how efficient a code is regardless of the environment. We move away from using time as a measurement of perfomance as it is subjective.

## Linear time O(n): 
for example, a for loop that searches a particular element by traversing through the entire array could be termed as having linear time perfomance. -> `O(n)`.

## Constant time: O(1):
No matter how big our array, for example is, and a function only operates on the first item, then regardless of how big the array is, we are doing the same number of items...whether one or two or three.
This is the best complexity because it is dead predictable. Predictability is precious in computing.

## Big O rules-> 
### 1. Worst Case:
In the grand scheme of things, big O only cares about the worst case. In an iterative looping search algorithm with a break statement, the best case is `O(1)` when the item is the first in the data structure and the worst case is `O(n)` if it is at the end.

### 2. Remove constants:
In asymtotic analysis, we do not care about constants, so `O(1 + n/2 + 100)` is simplified to `O(n)`

### 





