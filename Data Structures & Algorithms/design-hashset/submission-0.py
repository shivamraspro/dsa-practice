class MyHashSet:

    def __init__(self):
        self.arr = []
        

    def add(self, key: int) -> None:
        for a in self.arr:
            if key == a:
                return
        self.arr.append(key)

    def remove(self, key: int) -> None:
        arr = []
        for a in self.arr:
            if a != key:
                arr.append(a)
        self.arr = arr

    def contains(self, key: int) -> bool:
        for a in self.arr:
            if a == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)