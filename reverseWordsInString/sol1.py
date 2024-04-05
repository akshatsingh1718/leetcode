class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        reverse = ""
        while i < n:
            # get to the first char
            while i < n and s[i] == " ":
                i += 1

            # if our starting pointer has reached the end
            if i >= n:
                break

            # now we are at the first char which is not a space
            j = i + 1
            while j < n and s[j] != " ":
                j += 1

            reverse = (s[i:j] + " " + reverse) if len(reverse) > 0 else s[i:j]

            i = j + 1

        return reverse


def main():
    s = Solution()
    res = s.reverseWords("  a good   example      ")
    print(f"->{res}<-")


main()
