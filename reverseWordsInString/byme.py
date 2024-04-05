class Solution:
    """
    Runtime
    Details
    52ms
    Beats 20.04%of users with Python3
    Memory
    Details
    16.46MB
    Beats 55.71%of users with Python3
    """

    def reverseWords(self, s: str) -> str:
        arr = []
        n = len(s) - 1

        # append all the chars to an array
        while n >= 0:
            arr.append(s[n])
            n -= 1

        n = len(s) - 1
        reverse = ""

        # iterate from the last in array
        while n >= 0:
            # temp to store the words in array (which are seperated by spaces)
            temp = ""

            # if space is there then continue
            if arr[n] == " ":
                n -= 1
                continue

            # get the word from the array until end n is at the start of array
            # or we hit the space
            while n >= 0 and arr[n] != " ":
                temp += arr[n]
                n -= 1

            # add the word to the first of the current reversed string
            reverse = temp + " " + reverse
            n -= 1
        return reverse.strip()  # strip spaces


def main():
    s = Solution()

    print(s.reverseWords("  a good   example   "))


main()
