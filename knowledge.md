# sliding window

- Whenever question states about continuous subarray think if sliding window can be used or not using any type of prefix hashmap algo.

# Subsets

- There can be `2^n` subsets we can create from a given n length array.

# Binary

## Odd or even ?

- if the least significant digit is 1 then number is odd else even.
- Eg 1. Bin(2) = b"10" least significant digit is 0 so its even.
- Eg 2. Bin(3) = b"11" least significant digit is 1 so its odd.

## Divide by 2 (using >> )

- Diving any number by 2 can be done using right shift `>>` operator or chopping of the least significant digit from binary representation.
- For even number division:
  - Eg. Bin(100) = "0b1100100"; bin(50) = '0b110010'. This example shows that how right shift divides.
- For odd num division
  - Eg. bin(99) = '0b1100011'; bin(49) = '0b110001'. The int value of 99 / 2 will be used given since right shift will give the (num // 2) or the floor value of num / 2.

# Numbers

## Powers of 2

- All the numbers which are powers of 2 when divided by 2 will give even numbers.
- Its not necessarily the case that dividing every even number by 2 will provide an even num.
- Diving every odd number by 2 will give odd number.

# Heap

- If asked about kth smallest take max heap and vice versa because heap can pop the top elements and if we take an example of kth smallest then max heap will have larger elements on the top and we can easily pop bigger elements. The size of the heap will be k. If a new element is added to the heap and its length gets greater than k then we will pop the largest (top element) and at the end out heap will have the smallest element at the top.
