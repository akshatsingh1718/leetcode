NO_OF_CHILDREN = 26

"""
Trie A.K.A Prefix Tree
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * NO_OF_CHILDREN

        self.isEndOfWord = False


class Trie:
    '''
    Runtime
    Details
    255ms
    Beats 8.54%of users with Python3
    Memory
    Details
    35.50MB
    Beats 16.05%of users with Python3
    '''
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _charToIndex(self, char: str) -> int:
        return ord(char.lower()) - ord("a")

    def insert(self, key):
        length = len(key)

        if length == 0:
            return

        # get the root node as a starting point
        pCrawl = self.root

        # iterate over key
        for level in range(length):
            char = key[level]

            # if char is None in the array
            if not pCrawl.children[self._charToIndex(char)]:
                # add a node to the char idx
                pCrawl.children[self._charToIndex(char)] = self.get_node()

            pCrawl = pCrawl.children[self._charToIndex(char)]

        # Mark the node after the last key char to True for end of key
        pCrawl.isEndOfWord = True

    def search(self, key):
        length = len(key)

        if length == 0:
            return False

        pCrawl = self.root

        for level in range(length):
            char = key[level]
            char_idx = self._charToIndex(char)

            if not pCrawl.children[char_idx]:
                return False

            pCrawl = pCrawl.children[char_idx]

        return pCrawl.isEndOfWord

    def startsWith(self, key):
        length = len(key)

        if length == 0:
            return False
        
        pCrawl = self.root

        for level in range(length):
            char = key[level]
            char_idx = self._charToIndex(char)

            if not pCrawl.children[char_idx]:
                return False
            
            pCrawl = pCrawl.children[char_idx]

        return True


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
    print("{} ---- {}".format("thaw", t.startsWith("the")))



if __name__ == "__main__":
    main()
