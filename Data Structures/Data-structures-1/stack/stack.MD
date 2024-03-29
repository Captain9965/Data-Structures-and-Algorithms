# Stack:
Linear data structure that follows LIFO. One can only remove and add elements from the top. Basic operations include **push, pop, isEmpty, isFull, and peek** 
Working:
1. A pointer called top is used to keep track of elements in the stack
2. We initialize top to -1 so that we can check whether the stack is empty by comparing top to -1.
3. On pushing an element, we increase the value of top and place the new element in the position pointed to by top
4. On poping an element, we return the element pointed to by top and reduce its value.
5. Before pushing, we check whether the stack is already full and before popping, we check whether the stack is already empty.

Implementation is commonly through arrays, but can also be done through lists.
## Stack time complexity:
For the array implementation, insertion and deletion( push and pop) take constant time 0(1)

## Applications:
1. to reverse a word
2. Used by compilers to evaluate mathematical expressions by converting the experssion to pre-fix or post-fix form.
3. Browsers use a stack to store the urls that one has visited to enable back operation
