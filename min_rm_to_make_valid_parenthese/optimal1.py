'''
Leetcode Sol (Shoe store problem): https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/solutions/4980158/100-beat-easy-2-approaches-stack-without-stack-detailed-explanation/


# Shoe Problem:

## First Pass: Finding Extra Right Shoes
- The manager goes through the list one customer at a time.
- If a customer needs a left shoe (arr[i] == '('), they increase the counter (openParenthesesCount+= 1). This means we have a request for a right shoe as well.
- If a customer needs a right shoe (`arr[i] == ')'), they check:
    - If a customer needs a left shoe as well then the counter goes down (openParenthesesCount-=1) as a pair is made.
    - If no customer needs a left shoe (openParenthesesCount==0), then right shoe is extra and they mark it for return using arr[i] = "*". Later on we will remove this shoe/parenthesis from the array as an extra shoe/parenthesis.

> NOTE: After all the shoes looked by the manager if openParenthesesCount > 0 if means there are still RIGHT shoe demands by the customers.
    
**Till Now all the extra right shoes has been marked as "*". But what happen if we have an extra left shoe ?**  

## Second Pass: Finding Extra Left Shoes:
- The manager starts from the end of the list, looking for extra left shoes.
- If the customer needs a left shoe (arr[i]=="(") and our openParenthesesCount > 0 which means there are customers needing righ shoe, then the left shoe is extra as openParenthesesCount depcits the supply of left shoe and mark left shoe as "*" for return.

**Till now we have marked all the extra shoes as "*". **

Arranging the shelves:
- The manager takes all non-marked shoes (arr[i] != "*") and puts them neatly on the shelves.
'''

class Solution:
    '''
    
    TC: O(n) + O(n) ~ O(n)
    SC: O(n) [list of string items] + O(n) [store resutl]
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        # Initialize variables
        openParenthesesCount = 0
        arr = list(s)

        # First pass: mark excess closing parentheses with '*'
        for i in range(len(arr)):
            if arr[i] == '(':
                openParenthesesCount += 1
            elif arr[i] == ')':
                if openParenthesesCount == 0:
                    arr[i] = '*' # Mark excess closing parentheses
                else:
                    openParenthesesCount -= 1

        # Second pass: mark excess opening parentheses from the end
        for i in range(len(arr) - 1, -1, -1):
            if openParenthesesCount > 0 and arr[i] == '(':
                arr[i] = '*' # Mark excess opening parentheses
                openParenthesesCount -= 1
        
        # Filter out marked characters and construct the result string
        result = ''.join(c for c in arr if c != '*')

        return result


# testcase 1
s = "a(b(c)d"
output= "a(bc)d"

res = Solution().minRemoveToMakeValid(s)
print(res)