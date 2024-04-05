class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        self.isEndOfWord = False

        self.occurrence = 0
        self.starts_with_occurrence = 0


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _charToIdx(self, char: str) -> int:
        return ord(char.lower()) - ord("a")

    def _markEnd(self, node: TrieNode):
        node.isEndOfWord = True
        node.occurrence += 1
        node.starts_with_occurrence += 1

    def insert(self, key):
        length = len(key)

        if length == 0:
            return

        pCrawl = self.root

        for level in range(length):
            char = key[level]
            char_idx = self._charToIdx(char)

            if not pCrawl.children[char_idx]:
                pCrawl.children[char_idx] = self.get_node()

            pCrawl.starts_with_occurrence += 1
            pCrawl = pCrawl.children[char_idx]

        self._markEnd(pCrawl)

    def search(self, key):
        length = len(key)

        if length == 0:
            return

        pCrawl = self.root

        for level in range(length):
            char = key[level]
            char_idx = self._charToIdx(char)

            if not pCrawl.children[char_idx]:
                return False
            pCrawl = pCrawl.children[char_idx]

        return pCrawl.isEndOfWord

    def startsWith(self, key: str):
        length = len(key)

        if length == 0:
            return False

        pCrawl = self.root

        for level in range(length):
            char = key[level]
            char_idx = self._charToIdx(char)

            if not pCrawl.children[char_idx]:
                return False
            pCrawl = pCrawl.children[char_idx]

        return True

    def countWordsEqualTo(self, key: str) -> int:
        length = len(key)

        if length == 0:
            return False

        pCrawl = self.root

        for level in range(length):
            char = key[level]
            char_idx = self._charToIdx(char)

            # if the word is not present then return 0
            if not pCrawl.children[char_idx]:
                return 0

            pCrawl = pCrawl.children[char_idx]

        return pCrawl.occurrence if pCrawl.isEndOfWord else 0

    def countWordsStartingWith(self, key: str) -> int:
        length = len(key)

        if length == 0:
            return False

        pCrawl = self.root

        for level in range(length):
            char = key[level]

            char_idx = self._charToIdx(char)

            if not pCrawl.children[char_idx]:
                return 0
            pCrawl = pCrawl.children[char_idx]

        return pCrawl.starts_with_occurrence

    def erase(self, key: str) -> bool:
        length = len(key)

        if length == 0:
            return False

        pCrawl = self.root
        prv_pCrawl = None
        pv_char_idx = None

        for level in range(length):
            char = key[level]
            char_idx = self._charToIdx(char)

            # if the word does not exist then return False
            if not pCrawl.children[char_idx]:
                return False

            prv_pCrawl = pCrawl
            pv_char_idx = char_idx
            pCrawl.starts_with_occurrence -= 1
            pCrawl = pCrawl.children[char_idx]

        if not pCrawl.isEndOfWord:
            return False

        if pCrawl.occurrence > 1:
            pCrawl.occurrence -= 1
            pCrawl.starts_with_occurrence -= 1
        else:
            prv_pCrawl.children[pv_char_idx] = None

        return True


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "the", "anaswe", "any", "by", "their"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", [t.search("the")]))
    print("{} ---- {}".format("these", [t.search("these")]))
    print("{} ---- {}".format("their", [t.search("their")]))
    print("{} ---- {}".format("thaw", [t.search("thaw")]))
    print("{} ---- {}".format("the", t.startsWith("the")))

    print("-" * 40)
    print("{} ---- {}".format("the", t.countWordsEqualTo("the")))
    print("{} ---- {}".format("th", t.countWordsStartingWith("th")))

    print("{} ---- {}".format("th", t.erase("th")))
    print("{} ---- {}".format("the", t.erase("the")))

    print("{} ---- {}".format("the", t.countWordsEqualTo("the")))
    print("{} ---- {}".format("th", t.countWordsStartingWith("th")))

    print("{} ---- {}".format("th", t.erase("th")))
    print("{} ---- {}".format("the", t.erase("the")))

    print("{} ---- {}".format("the", t.countWordsEqualTo("the")))
    print("{} ---- {}".format("th", t.countWordsStartingWith("th")))


if __name__ == "__main__":
    main()
