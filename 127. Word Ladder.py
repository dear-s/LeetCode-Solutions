
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        if endWord not in wordList:
            return 0

        alphabets = "abcdefghijklmnopqrstuvwxyz"
        # graph approach - and apply BFS
        visited_map = {} # to keep the track of visited nodes when traversing
        for wL in wordList:
            visited_map[wL] = False

        queue = [] # this will hold the adjacent nodes and unvisited ones

        queue.append(beginWord)
        queue.append("-") # delimiter to keep the count value in storage
        if beginWord in visited_map:
            visited_map[beginWord] = True

        count = 0
        
        # add adjacent nodes -- that differ by one letter only - BFS approach
        while queue:
            wordy = queue.pop(0)
            if wordy == "-":
                count += 1
                if len(queue) > 0:
                    queue.append("-")
            else:
                if wordy == endWord:
                    if len(queue)>0:
                        count += 1
                    return count
                char_array = list(wordy) # in order to find the adjacent nodes

                ind = 0
                while ind < len(char_array):
                    temp_array = []
                    for ca in char_array:
                        temp_array.append(ca)
                    for a in alphabets:
                        temp_array[ind] = a
                        temp_string = "".join(x for x in temp_array)
                        if temp_string in visited_map and visited_map[temp_string] == False:
                            queue.append(temp_string)
                            visited_map[temp_string] = True
                    ind += 1

        return 0
        
