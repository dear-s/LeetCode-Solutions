class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        
        lowers = "abcdefghijklmnopqrstuvwxyz"
        
        # check all the indexes of pattern
        answer = []
        
        for query in queries:
            found = False
            collect_indexes = [] # from queries
            p = 0
            q = 0
            while p < len(pattern) or q < len(query):
                # if found pattern -- save q value and move forward
                # if lower -- move forward q
                # if upper -- false
                if p < len(pattern) and found == False and q < len(query):
                    if pattern[p] == query[q]:
                        collect_indexes.append(q)
                        q += 1
                        p += 1
                    elif query[q] in lowers:
                        q += 1
                    elif query[q] not in lowers:
                        # false
                        answer.append(False)
                        found = True
                        p = len(pattern)
                elif p == len(pattern) and found == False and q < len(query):
                    if query[q] in lowers:
                        q+=1
                    else:
                        # false
                        answer.append(False)
                        found = True
                        q = len(query)
                        
                elif p < len(pattern) and q == len(query):
                    answer.append(False)
                    p = len(pattern)
                    found = True
                        
                if found == True:
                    p = len(pattern)
                    q = len(query)
                        
            if found == False:
                answer.append(True)
                
        # print("answer: ", answer)
        return answer
        
        
