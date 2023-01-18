# Searching and sorting algorithms:

# Bubble sort algorithm:

This algorithm compares 2 adjacent elements and swaps them until they are in the intended order.

## Working in ascending order:
1. Starting from the first index, compare the first and second element and if the first element is greater than the second element, swap them. Do so until the last element.
2. The same process goes on for the remaining iterations.
3. Note that after each interation, the largest element among the unsorted elements is placed at the end.

## Algorithm:
```
bubbleSort(array)
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
end bubbleSort
```
In the above algorithm, comparisons are made even if the array is already sorted, increasing execution time.
To solve this, we can introduce a variable named `swap`, which is set to true when swapping occurs. If swapped is false after an interation, then there is no need to perform further iterations.

```
bubbleSort(array)
  swapped <- false
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
      swapped <- true
end bubbleSort
```

## Complexity:
```
Time Complexity	 
Best	            O(n)
Worst	            O(n2)
Average	            O(n2)
Space Complexity	O(1)
Stability	        Yes
```

### Time complexities:
1. Worst case: 

If we want to sort in ascending order and the array is in descending order.

2. Best case complexity:

The array is already sorted, no need for sorting

3. Average Case complexity:

Jumbled up elements.

## Space complexity:
Is 0(1) since 1 extra variable is used for swapping. If one extra variable is used, for the optimized case, this becomes 0(2)

## Applications:
1. If complexity does not matter.
2. Shorter code is preferred.

# Selection sort algorithm:
This is an algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the list

## working:
1. Select the first element as `miniumum`.
2. Compare `mininum` with the second element and if it is smaller than `minimum`, assign it as the new `minimum`. This goes on until the last element.
3. This minimum is swapped and placed at the front of the list
4. for each iteration, indexing starts from the first unsorted elements.    

## Algorithm:
```
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
```



