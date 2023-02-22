# Big-O-notation: 
Good code can be described as:
- readable
- scalable --> big-O helps us to measure and achieve this in terms of ( time and speed of our code and memory )


It is a standard way for us to measure how efficient a code is regardless of the environment. We move away from using time as a measurement of perfomance as it is subjective.

## Linear time O(n): 
for example, a for loop that searches a particular element by traversing through the entire array could be termed as having linear time perfomance. -> `O(n)`.

## Constant time: O(1):
No matter how big our array, for example is, and a function only operates on the first item, then regardless of how big the array is, we are doing the same number of items...whether one or two or three.
This is the best complexity because it is dead predictable. Predictability is precious in computing.

### Quadratic time: O(n2):
This most commonly occurs in nested loops

## Factorial time : O(n!):
You are adding a loop for every element you iterate over. Probably a bad idea.

## Big O rules-> 
### 1. Worst Case:
In the grand scheme of things, big O only cares about the worst case. In an iterative looping search algorithm with a break statement, the best case is `O(1)` when the item is the first in the data structure and the worst case is `O(n)` if it is at the end.

### 2. Remove constants:
In asymtotic analysis, we do not care about constants, so `O(1 + n/2 + 100)` is simplified to `O(n)`

### 3. Different terms for inputs:
For different inputs, we use different terms. Example, if we have 2 for loops for different inputs, the time complexity becomes `O(a + b)`

### 4. Drop non dominant terms:
In this rule, we only maintain the most important term, if we have `O(n + n2)`, we drop the non dominant term to remain with `O(n2)`


# Space complexity:
This is an indication of how many new variables we may need to allocate in processing our data. We talk about additional space, we don't include space taken up by the inputs. We dont care how big our input is.

For example, a simple loop to access elements of an array has a space complexity of `O(1)` since no additional memory is allocated within the for loop.

If for example, we are creating an new array of size n , then we have a space complexity of `O(n)`

## Causes of space complexity:
1. variables
2. Data structures
3. Function calls
4. Allocations

Its all about a balance between runtime, space and readability depending on the time and resources available to a programmer.


