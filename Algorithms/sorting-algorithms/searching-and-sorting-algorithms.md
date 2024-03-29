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

# Merge Sort algorithm:
This is based on the principle of divide and conquer algorithm. 
Here, a problem is divided into multiple sub-problems and each sub-problem is solved seperately. Finally, sub-problems are combined into the final solution.

## Divide and conquer algorithm:
Supposing we have an array `A`, a subproblem  would be to sort a sub-section of this array starting at index `p` and ending at index `r`, denoted as `A[p...r]`

## Divide:
If `q` is the halfway point between `p` and `r`, then we can split the subarray A[p...r] into 2 arrays: A[p...q] and A[q + 1, r]

## conquer:
In this step, we try to sort the subarrays A[p...q] and A[q...r]...If we haven't reached the base yet, we try to split the subarray again and again try to sort.

## Combine:
When the conquer array reaches the base step and we get 2 sorted subarrays, we we combine the results to get a sorted array A[p..r]

## Algorithm theory:
The mergesort function repeatedly divides the array into 2 halves until we reach  a stage where we try to perform mergesort on an array of size 1. i.e p == r.

After that, the merge funciton comes to play and combines the sorted arrays into a larger array until the whole array is merged.

```
MergeSort(A, p, r):
    if p > r 
        return
    q = (p+r)/2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)
```
To sort an entire array, we need to call `MergeSort(A, 0, length(A) - 1)`

### The merge step:

Every recursive algorithm is dependent on a base case and the ability to combine the results from the base cases. The most important step being the merge step.

The algorithm maintains 3 pointers, one for each array and the third for maintaining the current index of the final sorted array.

```
Have we reached the end of any of the arrays?
    No:
        Compare current elements of both arrays 
        Copy smaller element into sorted array
        Move pointer of element containing smaller element
    Yes:
        Copy all remaining elements of non-empty array
```
### Merge sort complexity:
```

Time Complexity	 
Best	            O(n*log n)
Worst	            O(n*log n)
Average         	O(n*log n)
Space Complexity	O(n)
Stability	        Yes
```
## Applications:
1. Inversion count problems
2. External 
3. E-commerce applications

# Quick sort algorithm:

Also uses the divide and conquer approach whereby:
1. An array is divided into sub-arrays by selecting a pivot element. While selecting it, it should be positioned in such a way that elements less than it are to the left and those greater than it are to the right.
2. The left and right sub-arrays are divided in like manner until each sub-array consists of one element.
3. At this point, elements are already sorted and are then combined to form the sorted array.

## Working of the algorithm:
1. Selecting the pivot element: we can select the righmost element.
2. Re-arrange the array such that elements that are smaller are to the left while those that are greater are to the right, in any order
    - A pointer is fixed at the pivot element. This is compared with the elements beginning from the first index.
    - If it is > pivot element, a second pointer is set for that element.
    - Now, pivot is compared to other elements. If an element smaller than the pivot element is reached, it is swapped with the larger element found earlier.
    - Again the process is repeated to set the next greater element as the second pointer. And swap it with another smaller element.
    - This goes on until the second last element is reached.
    - Finally, the second pointer is swapped with the second pointer.
3. Divide sub-arrays:

    Pivot elements are chosen for the left and right  sub-arrays seperately. and step 2 is repeated.

4. Once each sub-array is a single element, then the array is already sorted.

## Algorithm:
```
quickSort(array, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
    quickSort(array, leftmostIndex, pivotIndex - 1)
    quickSort(array, pivotIndex, rightmostIndex)

partition(array, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
  if element[i] < pivotElement
    swap element[i] and element[storeIndex]
    storeIndex++
  swap pivotElement and element[storeIndex+1]
return storeIndex + 1
```

## Quick sort complexity:
```
Time Complexity	 
Best	            O(n*log n)
Worst	            O(n2)
Average	            O(n*log n)
Space Complexity	O(log n)
Stability	        No
```
## Application:
Used when:
1. The programming language is good for recursion.
2. Time complexity matters
3. space complexity matters


# Counting sort:

This algorithm sorts an array by counting the number of unique occurrences of an element in the array. The count is stored in an auxiliary array and sorting is done by mapping the count as an index of the auxiliary array.

## Working: 
1. Find out the maximum element from the given array `max`.
2. Initialize an array of length ` max + 1` with all elements 0. This is used for storing the count of elements in the array.
3. Store the count of each element at their respective index in `count` array. 
4. Store cummulative sum of elements in the `count` array.
5. Find the index of each element of the original array in the count array. Place the element at the index calculated.
6. After placing each element at its correct position, decrease its count by 1.

## Algorithm:
```
countingSort(array, size)
  max <- find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and 
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
```

## Time complexity:
```
Complexity	 
Best	            O(n+k)
Worst	            O(n+k)
Average	            O(n+k)
Space Complexity	O(max)
Stability	        Yes
```

where `k` is the max element and `n` is the number of elements to be sorted. 
The complexity is the same since no matter how the elements are placed in the array, the algorithm goes through `n + k` times.
Bad if the intergers are very large because an array of that size should be made.

## Space complexity:
This is O(max) because the larger the range of elements, the larger the space complexity.

## Applications:
1. Used when there are smaller integers with multiple counts.
2. Linear complexity is needed.

# Radix sort:
This is a sorting algorithm that sorts elements by first  grouping the individual digits of the same place value.
Then sort the elements according to their increasing or decreasing order.

Uses the counting sort algorithm. 

## Working:
1. Find the largest element in the array, and let it be `max`. Let also the number of digits in `max` be `x`. `x` is calculated because we have to go through all the significant places of all the elements.

2. Go through each significant place one by one..using any stable sorting technique to sort the digits at every signifiant place.

3. Sort the units place, then the tens place, then the hundreds place.

## Algorithm:
```
radixSort(array)
  d <- maximum number of digits in the largest element
  create d buckets of size 0-9
  for i <- 0 to d
    sort the elements according to ith place digits using countingSort

countingSort(array, d)
  max <- find largest element among dth place elements
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique digit in dth place of elements and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
  ```

  ## Radix sort complexity:

  ```
Time Complexity	 
Best	            O(n+k)
Worst	            O(n+k)
Average	            O(n+k)
Space Complexity	O(max)
Stability	        Yes
```
  since its a non-comparative algorithm, it has an advantage over comparative sorting algorithms. For the radix sort that uses conting sort as an intermediate stable sort, the time complexity is `O(d(n + k))` where `d` is the number cycle and `O(n + k)` is the time complexity of counting sort. 
  Thus, radix sort has linear time complexity which is better than `O(n log n)` of comparative sorting algorithms.

  It therefore can perform in linear time with numbers of other bases. However, intermediate sort takes large space. This is why it is not used in software libraries.


  ## Applications:

  1. DC3 algorithm ( karkkainnen-Sanders-Burkhadt ) algorithm while making a suffix array.
  2. Places where there are numbers in large ranges.

  # Bucket sorting algorithm:

  This algorithm divides the unsorted array elements into several groups called buckets. Each bucket is then sorted by using any stable algorithm or recursively using the same bucket technique.

  They are then combined to form the final sorted array.

  ## Scatter Gather approach:
  Here, elements are first scattered into buckets then elements in each bucket are sorted. Finally, the elements are gathered in order.

  ## Working of the algorithm:

  1. Given an array, initialize another array in which each slot will be used as buckets for storing elements.
  2.  Insert elements into buckets from the array, each according to the range in the bucket. If it is a decimal, the element is * the least X to make it a mixed number. The floor value is used. If we take interger numbers as input, we have to divide it by the interval to get the floor value.
  3. Each bucket is sorted using any stable sorting algorithm eg. quicksort.   
  4. The elements from each array are gathered. This is done by iterating through each bucket and inserting an individual element into the original array in each cycle. Once copied into the original array, the element is erased from the bucket.

  ## Algorithm:
  ```
  bucketSort()
  create N buckets each of which can hold a range of values
  for all the buckets
    initialize each bucket with 0 values
  for all the buckets
    put elements into buckets matching the range
  for all the buckets 
    sort elements in each bucket
  gather elements from each bucket
  end bucketSort
  ```

## Complexity:
```
Time Complexity	 
Best	            O(n+k)
Worst	            O(n2)
Average	            O(n)
Space Complexity	O(n+k)
Stability	        Yes
```

## Worst case complexity: 
When the elements are in close range, they are likely to be placed in the same bucket, with some having more elements than others. 
This makes bucket sort dependent on the complexity of the sorting algorithm used to sort the elements in the bucket. It gets even worse if the elements are in reverse order. 
If insertion sort is used, the complexity becomes O(n2)

## Best case complexity:
Occurs when there are equal number of elements in each bucket, with the elements uniformly distributed. It even gets better when the elements in the bucket are already sorted. The complexity is therefore O(n + k) if we are using insertion sort. O(n) for making the buckets and O(k) for sorting the bucket elements using a linear time algorithm.

## Average Case complexity:
In this case, elements are randomly distributed in the array.

## Applications:
1. When input is uniformly distributed over a range.
2. There are floating point values.


# Heap Sort:

## Relationship between tree elements and array indices:
If the index of any element is `i`, then the element in the index `2i + 1` will become the left child and the element in the index `2i + 2` will become the right child.

Also, the parent of any element at index `i` is given by the lower bound of `(i -1)/2`

## What is a heap data structure?

A binary tree is said to follow a heap data structure if:

1. It is a complete binary tree.
2. All nodes in the tree follow a property that they are greater than their children i.e. the largest element is at the root and both of its children are smaller than the root in the case of max-heap. If all nodes are smaller than their children, then it is called a min-heap.

## How to heapify a tree: 
Starting from a complete binary tree, we can modify it to become a max-heap by calling a function called  "heapify" on all non-leaf elements of the heap.

With just 3 elements, the algorithm would look like:
```
heapify(array)
    Root = array[0]
    Largest = largest( array[0] , array [2*0 + 1]. array[2*0+2])
    if(Root != Largest)
          Swap(Root, Largest)
```
To maintain the max-heap property in a tree where both sub-trees are max-heaps, we need to run heapify on the root element repeatedly until it is larger than its children or it becomes a leaf node. 


## Building a max-heap:
To build a max-heap from any tree, we can start by heapifying each sub-tree from the bottom up and we end up with a max-heap when heapify is applied on all elements including the root element.
In the case of a complete binary tree, the first index of a non-leaf node is given by `n/2 -1`. All other nodes after that are leaf nodes and do not need to be heapified.

Therefore:
```
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
      heapify(arr, n, i);

```
## Working of the heap sort:
1. Since the tree satisfies the max-heap property, then the largest item is stored at the root node. 
2. Swap: remove the root element and put it at the end of the array. Put the last item of the tree at the vacant place. 
3. Remove: reduce the size of the heap by 1. 
4. Heapify the root element again such that we have the highest element at the root.
5. Repeat the process until all the elements in the list are sorted.

Operation:
```
    // Heap sort
    for (int i = n - 1; i >= 0; i--) {
      swap(&arr[0], &arr[i]);

      // Heapify root element to get highest element at root again
      heapify(arr, i, 0);
    }
```

## Heap sort complexity:
```
Time Complexity	 
Best	            O(nlog n)
Worst	            O(nlog n)
Average	            O(nlog n)
Space Complexity	O(1)
Stability	        No
```
The height of a tree containing `n` elements is `log n`. As we have seen, to fully heapify an element whose sub-trees are already max-heaps, we need to keep comparing its elements with its children and pushing it downwards until it reaches a point where both its children are smaller than it. ,

In the worst case scenario, we need to move an element from the root, to the leaf node, making a multiple of `log n` comparisons and swaps.

During the buld_max_heap stage, we do that for `n/2` elements so the worst case complexity of this stage is `n/2 * log n ~ n log n`

During the sorting stage, after we swap, we may also need to push down the element from the root to the leaf hence `log n` complexity. We need to repeat this `n` times so `nlogn`

These steps are exectuted one after another hence the algorithmic complexity remains in the order of `n log n`. 

Also performs sorting in `O(1)` space complexity 

In comparison with Quick sort, it has a better worst case. But in other cases, quick sort is fast. 

An alternative is introsort which combines the worst case speed of heap sort and the average speed of quick sort. 

## Applications:
1. In systems concerned with security and embedded applications due to the `n log n` upper bound on running time and constant O(1) upper bound on the auxiliary space.

2. The underlying data structure i.e. the heap data structure can be used if we want to efficiently extract the smallest or the largest element from a list without the overhead of having to keep all the elements in order. eg. priority queues


# Shell sort: 
It is a genaralized version of the insertion sort algorithm. It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted. 

The interval between the elements is reduces based on the interval used. Some of the optimal sequences used are: 
1. Shell's original
2. Knuth's increments
3. Pratt's increments
4. Hibbard's increments
5. Sedgewick's increments
6. Papernov's and Stasevich's increments

The perfomance depends on the type of sequence used for a given input array. 

## Working of shell sort:
Using the shell's orignal sequence: `N/2, N/4....1`,
1. If the array size is 8, then elements lying at the interval of `N/2` are compared and swapped if not in order. 
  - The `0th` element is compared with the `4th` element
  - If the `0th` element is greater than the `4th` element, then swap them.
  - The process goes on for all remaining elements.
  - Then rearrange at `N/2` intervals
  - The same process goes on for the remaining elements.
  - Finally the array elements lying at the interval of 1 are sorted. The array is now completely sorted.

  ## Shell sort algorithm:
```
  shellSort(array, size)
  for interval i <- size/2n down to 1
    for each interval "i" in array
        sort all the elements at interval "i"
end shellSort
```

## Complexity:
```
Time Complexity	 
Best	            O(nlog n)
Worst	            O(n2)
Average	            O(nlog n)
Space Complexity	O(1)
Stability	        No
```

This is an unstable algorithm because it doesnt examine the elements lying between the intervals.

## Applications:
1. When calling a stack is overhead.
2. When recursion exceeds a limit.e.g. in `bzip2`
3. Insertion sort does not perform well when the close elements are far apart. Shell sort helps in reducing the distance between those elements. Hence, there are less number  of swappings to be performed.

# Linear Search:
This is a sequential searching algorithm where we start from one end and check every element until the desired element is found.

## Algorithm:
  ```
  LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
  ```
## Complexity:
Time complexity is `O(n)`
Space complexity is `O(1)`

## Applications:
1. Searching operations in arrays of less than 100 items.

# Binary search:
This is an algorithm for finding the position of an element in a sorted array. 

## Working:
We have the iterative and recursive methods.
General steps:
1. Set 2 pointers high and low at the highest and lowest positions respectively. 
2. Find the middle element `mid` of the array ie. `arr[(low + high) / 2]`
3. If `x == mid` then return `mid`. Else, compare the element to be searched with `mid`.
4. If `x > mid`, compare `x` with the middle element on the right side of `mid` by setting `low = mid + 1`, otherwise compare with the middle element on the left side of `mid` by setting `high = mid - 1`.
5. Repeat steps 2 - 4 until low meets high.

## Algorithm:
## Iterative method:
```
do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > arr[mid]) // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1
```

## Recursive method:
```
binarySearch(arr, x, low, high)
    if low > high
        return False 
    else
        mid = (low + high) / 2 
        if x == arr[mid]
            return mid
        else if x > arr[mid]        // x is on the right side
            return binarySearch(arr, x, mid + 1, high)
        else                               // x is on  the right side
            return binarySearch(arr, x, low, mid - 1)
```

## Complexity:
```
Time Complexities: 

Best case complexity:       O(1)
Average case complexity:    O(log n)
Worst case complexity:      O(log n)
```

space complexity:

The space complexity of binary search is `O(1)`.

## Applications:
1. In libraries of Java, .NET, C ++, STL.
2. Pinpointing where the error happens while debugging.