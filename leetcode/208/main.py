class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.word = True

    def search(self, word: str) -> bool:
        answer = True

        node = self.root
        for c in word:
            if c not in node.children:
                answer = False
                break
            else:
                node = node.children[c]

                answer = node.word

        return answer

    def startsWith(self, prefix: str) -> bool:
        answer = True

        node = self.root
        for c in prefix:
            if c not in node.children:
                answer = False
                break
            else:
                node = node.children[c]

        return answer


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
print(trie.search("app"))  # return False
print(trie.startsWith("app"))  # return True
print(trie.insert("app"))
print(trie.search("app"))    # return True
