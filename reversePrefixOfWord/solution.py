class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        for i, ele in enumerate(word):
            if ele == ch:
                return word[: i + 1][::-1] + word[i + 1 :]

        return word


word = "abcdefd"
ch = "d"
output = "dcbaefd"
