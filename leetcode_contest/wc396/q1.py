import string
# string.ascii_letters
# string.ascii_lowercase

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_digit = False
        has_vowel = False
        has_consonant = False
        has_uppercase = False
        has_lowercase = False

        for char in word:

            if char.isdigit():
                has_digit = True
                continue

            if char.isupper():
                has_uppercase = True
            elif char.islower():
                has_lowercase = True

            if char.lower() in ["a", "e", "i", "o", "u"]:
                has_vowel = True
            elif ord("a") <= ord(char.lower()) <= ord("z"):
                has_consonant = True
            
            if char in ['@', '#', '$']: return False

        return all([has_vowel, has_consonant]) and any([has_digit, has_uppercase, has_lowercase])


print(Solution().isValid("Ya$"))
