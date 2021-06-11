
class MyCalendar:

    def __init__(self):
        self.start_end = {} # dictionary {start: end}
        self.c = 0
        

    def book(self, start: int, end: int) -> bool:
        # print("________________________")
        self.c +=1
        # print("count: ", self.c)
        # print("entry val: ", start, end)
        
        
        # check if can be added or not - check for each entry in dictionary
        for s,e in self.start_end.items():
            # 3 poss - false
            if start <= s and end > s and end <= e:
                # print("dict: ", self.start_end)
                return False
            elif start <=s and end >= e:
                # print("dict: ", self.start_end)
                return False
            elif start >= s and start < e and end >= s and end <= e:
                # print("dict: ", self.start_end)
                return False
            elif start >= s and start < e and end >= e:
                # print("dict: ", self.start_end)
                return False
            
            
        # add
        self.start_end[start] = end
        # print("dict: ", self.start_end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

