
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        

    def add(self, key: int) -> None:
        if key not in self.array:
            self.array.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.array:
            self.array.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.array:
            return True
        return False
        
