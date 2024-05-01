'''
references:
1. https://leetcode.com/problems/minimum-array-end/solutions/5082310/bit-interweaving/

'''

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    
    GOT TLE

    '''
    def minEnd(self, n: int, x: int) -> int:
        nbin = n-1
        xbin = x


        i = 0
        print("X    =", bin(xbin))
        print(f"n-1 = {n-1}", bin(nbin))

        n_bin_idx = 0
        while n_bin_idx < 64:
            bit_to_choose = (1 << i) # get the selector for ith bit

            if bit_to_choose & xbin == 0: # check if the ith bit is 0
                # grab the next bit from the nbit from right to left

                n_bit_choose =  nbin & (1 << n_bin_idx)
                before = n_bit_choose
                n_bit_choose = n_bit_choose << i
                print(f"Shift by {i=} | before= {bin(before)} | after= {bin(n_bit_choose)}")

                xbin = xbin | n_bit_choose

                # print(xbin)
                n_bin_idx += 1

            i += 1
        return xbin
    
print(Solution().minEnd(n=3, x= 4))