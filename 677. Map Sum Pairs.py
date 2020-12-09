
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        
        self.map[key] = val
        

    def sum(self, prefix: str) -> int:
        
        out = 0
        getlen = len(prefix)
        
        # checking prefixes of keys
        
        for k,v in self.map.items():
            
            if k[:getlen] == prefix:
                out += v
            
        return out


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

  
