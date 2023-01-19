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

## Complexity:
```
Time Complexity	 
Best	            O(n2)
Worst	            O(n2)
Average	          O(n2)
Space Complexity	O(1)
Stability	        No
```

The time complexity is the same in all cases. This is because at every step, you have to find the minimum element and this cannot be known if the end of the array is not reached.

## Applications:
Used when: 
1. A small list is to be sorted.
2. cost of swapping does not matter.
3. checking of all elements is mandatory.
4. cost of writing to memory matters like in flash memory(number of write/swaps is 0(n) as compared to 0(n2) of bubble sort)

# Insertion sort:
This is an algorithm that places an unsorted element at its suitable position in each iteration.
We assume that the first card is already sorted then take the second card. If it is greater than the first card, put it on the right, otherwise to the left

## Working:
1. Take the second element and store it in `key`.If it is greater that the first element, put it in front of the first element.
2. Since the first element is already sorted, now take the third element and compare it with the elements on the left of it and place it just behind the element smaller than it. If there is no element that is smaller than it, then place it at the beginning of the array.
3. Similarly, place every subsequent element at its correct position.

## Insertion Algorithm:
```
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
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
## Time complexity:
### Worst Case complexity:
suppose an array is sorted in ascending order and we want to sort it in descending order, then every element is compared with each other element. for every element, every `nth` element, `(n - 1)` number of comparisons are made.

### Best case complexity:
If the array is already sorted, only the outer loop runs `n` times

### Average case complexity:
Occurs when the elements are in jumbled order.

### Space complexity:
It is `0(1)` due to the extra variable `key` that is used.

### Applications:
1. The array has a small number of elements.
2. There only a few number of elements to be sorted.