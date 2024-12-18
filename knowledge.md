# sliding window

-   Whenever question states about continuous subarray think if sliding window can be used or not using any type of prefix hashmap algo.

# Subsets

-   There can be `2^n` subsets we can create from a given n length array.

# Binary

## what is a set bit?

A set bit is a bit in a binary number that has a value of 1

## How to select bit range ?

In practical terms, for numbers constrained to be less than or equal to 10^7 (requiring a maximum of 24 bits), we only need to check bit positions 0 to 23 when working with 32-bit integers. For larger numbers, like those up to 10^9, we would check up to 30 bits, since 2^30 =1,073,741,824.

## Count no of set bits / count no of 1's in a binary representation.

-   brian kernighan’s algorithm

## Create a binary of all 1's given a number

-   We left shift 1 with the length of the binary num and negating 1 from it will give us that last all ones before becoming the 1000...
    as left shift will create the binary nums staring with a single one and rest all zeros.

```py
num = 5
length = num.bit_length()
all_ones = (1 << length) - 1

# 5 -> 101
# length = 3
# (b0001 << 3) - 1 = (b1000) - 1= 8 - 1 = 7 => b111
```

## Odd or even ?

-   if the least significant digit is 1 then number is odd else even.
-   Eg 1. Bin(2) = b"10" least significant digit is 0 so its even.
-   Eg 2. Bin(3) = b"11" least significant digit is 1 so its odd.
-   odd & 1 => 1; even & 1 => 0

## Divide by 2 (using >> )

-   Diving any number by 2 can be done using right shift `>>` operator or chopping of the least significant digit from binary representation.
-   For even number division:
    -   Eg. Bin(100) = "0b1100100"; bin(50) = '0b110010'. This example shows that how right shift divides.
-   For odd num division
    -   Eg. bin(99) = '0b1100011'; bin(49) = '0b110001'. The int value of 99 / 2 will be used given since right shift will give the (num // 2) or the floor value of num / 2.

# Numbers

## Powers of 2

-   All the numbers which are powers of 2 when divided by 2 will give even numbers.
-   Its not necessarily the case that dividing every even number by 2 will provide an even num.
-   Diving every odd number by 2 will give odd number.

# Heap

-   If asked about kth smallest take max heap and vice versa because heap can pop the top elements and if we take an example of kth smallest then max heap will have larger elements on the top and we can easily pop bigger elements. The size of the heap will be k. If a new element is added to the heap and its length gets greater than k then we will pop the largest (top element) and at the end out heap will have the smallest element at the top.

# DSU

-   used for dynamic graphs which are constantly changing.
-   Takes O(1) constant time to find if a node is connected with another given node.
-   It has 2 things:
    -   `find_parent()`: finds the parent of the node.
    -   `union`: has `rank` and `size`.

## Pseudo code:

1. find ultimate parent of u & v which is pu & pv.
2. Find rank of pu & pv.
3. Connect smaller rank to larger rank always.

-   **path compression**:
    -   Make the ultimate parent of all nodes as their parent.
    -   Eg.- 1 -> 2 -> 3 -> 4 -> 5. The parent of 5 should be 1 (ultimate parent) and not 4 as we want to get the parent in O(1) constant time to know whether two nodes are in the same component or not.

# String

## KMP String matching

-   Find the LSP Longest suffix prefix.
-   LSP[0] = 0 (since the first char will be only suffix and prefix).
-   After that we need to have a counter for prevLSP which is the previous LSP we have. Consider a string "AAACAAAA"

# Maths

## Handling -ve remainders

-   (num % k + k) % k

# sequence

## TC: 2^n \* n

-   `2^n`: Since at every recursion call we are taking elements till n starting from i. So 2 ^ n like in subsets where we take two possibilities at a time copy or not copy.
-   `n` : It is for the copy operation.
