# Hash table:

Store data in key-value pairs where:
1. Key - a unique integer used to index the values
2. value - this is data that is associated with the keys

## Hashing:

In a hash table, a new index is processed using the keys. And the element corresponding to that key is stored in the index. This process is called hashing. Supposing k is a key and h(x) a hash function, then h(k) will give us a new index to store the element linked with k. 

## Hash collision:

When a hashing function produces the same index for multiple keys, there will be a conflict over what value will be stored in that index. It can be however resolved with the following techniques:

1. Collision resolution by chaining
2. Open Addressing: Linear/quadratic probing and double hashing. 

#### Collision resolution by chaining:

If a hash function produces the same index for multiple elements, they are stored in the same index using a doubly-linked list.

If j is the slot for multiple elements, it contains a pointer to the head of the list of elements. If no element is present, j contains a NIL. 

### Open addressing:

Each slot is filled with a single key of left NIL.

Techniques used for open addressing are:

### i) Linear  Probing:

In this method, collision is resolved by checking the next slot:

`h(k, i) = (h'(k) + i) mod m`


where: 

`i = {0, 1, ..}`

`h'(k)` is a new has function

Essentially, if a collision occurs at `h(k, 0)`, then `h(k, 1)` is checked. In this way, the value of i is incremented linearly. 

The disadvantage with linear probing is that a cluster of adjacent slots is filled. When inserting a new element, the entire cluster must be traversed. This adds to the time required to perform operations on the hash table.

### ii) Quadratic probing:
Similar to linear probing but the spacing between the slots is increased(greater than one) by using the following relation:
`h(k, i) = (h'(k) + c<sub>1</sub>i + c<sub>2</sub>i<sup>2</sup>) mod m 

where c<sub>1</sub> and c<sub>2</sub> are auxiliary constants

### iii) Double hashing:

If a collision occurs after the first has function, then another hash function is calculated to find the next slot:


## Good has functions:

A good hash function reduces collisions from occuring.

### 1. Division:

if k is a key and m is the size of the has table, the hash function is calculated as `h(k) = k mod m`


### 2. Multiplication method:

`h(k) = ⌊m(kA mod 1)⌋`

where:

`kA mod 1` gives the fractional part kA, 

⌊ ⌋ gives the floor value

`A` is any constant, whose value lies between 0 and 1. An optimal choice would be `(√5-1)/2` suggested by Knuth.

### 3. Universal hashing:

The hash function is chosen at random independent of keys

## Applications of Hash table:
1. Where constant time lookup and insertion time is required.
2. Cryptographic applications.
3. indexing data.