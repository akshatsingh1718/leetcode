class Solution:
    '''
    Runtime
    Details
    36ms
    Beats 82.84%of users with Python3
    Memory
    Details
    16.20MB
    Beats 92.28%of users with Python3
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return -1

        i = 0
        counter = 0

        while i < len(haystack) - len(needle) + 1:
            j = 0
            temp_i = i
            while j < len(needle):
                if haystack[temp_i] == needle[j]:
                    counter += 1
                else:
                    break
                j += 1
                temp_i += 1

            if counter == len(needle):
                return i
            else:
                counter = 0

            i += 1

        return -1


def main():
    s = Solution()
    haystack = "mississippi"
    needle = "issip"
    print(s.strStr(haystack, needle))


main()
