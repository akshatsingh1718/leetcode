class Solution:
    """
    TC: O(N) [while loop from left to right] + O(K) [special case]
    SC: O(N) [stack]

    ======================================================
    Intuition:
    ======================================================
    Reomving the digits from first left is more important as greater values in front will make the result bigger. And after remvoing the the greater digits from left then lookup for right side digits.

    Take eg.-
    Example 1: N="9991" with k = 2
        output should be: "91" (Removing two 9's from front)
    Example 2: N="1999" with k = 2
        output should be: "19" (Removing two 9's from back)
    Example 3: N="9119" with k = 2
        output should be "11" (Removing one 9 from both ends)


    ======================================================
    Algo:
    ======================================================
    (Optional) 1. Add the first element from num in a stack (which we want to be monotonic increasing stack).
    2. Move from left to right in num string and check if the top of stack is gt the current element which means that a higher order number can be removed from the starting of the stack which can make our result more smaller. The value of k should also be greater than 0 since we have only limited number to pop.
    3. After the while loop if we are having the  k >0 and stack is non empty then it is telling the a substring of the num follows only ascending order. So the number should be removed from now right to left until the k's value has been exhausted since greater values are present in the right of the array.

    """

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        # stack = [num[0]] # Optional from step 1
        stack = []

        # i = 0 # Optional from step 1
        # i = 0
        # n = len(num)
        # while i < n:
        for ni in num:
            # while len(stack) > 0 and stack[-1] > num[i] and k > 0:
            while len(stack) > 0 and stack[-1] > ni and k > 0:

                stack.pop()
                k -= 1
            # Either stack should not be empty or number should not be zero at same time
            # if the stack is not empty then only zero element can be added
            # if ni == 0 or len(stack) > 0: # uncommenting this will prevent adding zero in stack; but this has been handled by lstrip "0" in python when returning the result
            # stack.append(num[i])
            stack.append(ni)

            # i += 1

        # special case where all the number are in ascending order
        # and we dont have and uphill. So out stack will contain all the
        # element from num and k will also remain unchanged
        # So for this case we can remove all the elements from right to left to elemenate
        # all the high elements

        # while len(stack) > 0 and k > 0:
        #     stack.pop()
        #     k -= 1
        ## OR
        stack = stack[: len(stack) - k]

        return "".join(j for j in stack).lstrip("0") or "0"


# TS1
# TS1
num = "1432219"
k = 3
output = "1219"

# TS2
# num = "10001"
# k = 4
# output = "0"

# TS3
# num = "10"
# k = 2
# output = "0"

# TS4
# num = "10200"
# k = 1
# output = "200"


# TS4
# num = "9"
# k = 1
# output = "0"


num = "112"
k = 1
output = "11"

print(Solution().removeKdigits(num=num, k=k))
