class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        # reference - https://www.youtube.com/watch?v=y2BD4MJqV20
        
        if len(s) == 0: return ""

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            length = max(len1, len2)
            if (length > end - start):
                start = i - ((length-1)//2)
                end = i + (length//2)

                
        return s[start:end+1]
	
	
    def expand(self, s, left, right):
        if len(s) == 0 or left > right:
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left -1

        
        """
        # Time out limit :(
        if len(s) in [0,1]: return s
        
        same_palindromes = []
        # expand from center
        list_s = list(s)

        i = 0
        while(i < len(list_s)):
            same_palindromes.append(list_s[i])
            left = i-1
            right = i+1
            while left >= 0:
                temp1 = list_s[left:i+1]
                temp_rev_list1 = temp1[::-1]

                if temp1 == temp_rev_list1:
                    same_palindromes.append(temp1)

                left-=1

            while left >= 0 and right < len(list_s):
                temp = list_s[left:right+1]
                temp_rev_list = temp[::-1]

                if temp == temp_rev_list:
                    same_palindromes.append(temp)

                left -= 1
                right += 1

            i+=1

        print("same_palindromes: ", same_palindromes)

        max_length = 0
        # max_array = []
        for p in same_palindromes:
            if len(p) >= max_length:
                max_length = len(p)
                max_array = p

        print("max_array: ", max_array)


        string_answer = "".join(max_array)
        print("string_answer: ", string_answer)
        
        return string_answer
        """
        
        
        
        # Brute force
        """if s is None or s == "": return ""
        
        output = []
        list_s = list(s)
        print("list_s: ", list_s)

        for i in range(0, len(list_s)):
            temp = []
            temp.append(list_s[i])

            for j in range(i+1, len(list_s)):
                temp.append(list_s[j])

                rev_temp = temp[::-1]

                if temp == rev_temp:
                    new = []
                    for i in temp:
                        new.append(i)
                    output.append(new)

        l_max = 0
        answer = []
        for each_list in output:
            len_each_list = len(each_list)

            if len_each_list > l_max:
                answer = []
                for m in each_list:
                    answer.append(m)
                l_max = len_each_list

        print(answer)
        if len(answer) == 0:
            for i in temp:
                answer.append(i)

        ans_string = "".join(answer)
        print(ans_string)
        return ans_string"""
