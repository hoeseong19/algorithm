class MyHashSet:

    def __init__(self):
        self.my_set = set()

    def add(self, key: int) -> None:
        self.my_set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.my_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.my_set
