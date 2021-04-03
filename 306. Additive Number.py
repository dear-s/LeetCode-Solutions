  
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        
        # digits form additive sequence
        
        # additive sequence -- at least three numbers
        # a b a+b a+2b 2a+3b -- fibonacci
        
        # :i, i:j --- proceed with fibonacci
        original_num = ""
        for n in num:
            original_num += n
        
        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                
                a = num[:i] # first
                b = num[i:j] # second
                
                if a[0] == "0" and len(a) > 1:
                    continue
                elif b[0] == "0" and len(b) > 1:
                    continue
                else:                    
                    fibonacci = [a,b]
                    updated_fibo = self.make_fibonacci(a, b, num, fibonacci)
                    str_updated_fibo = "".join(x for x in updated_fibo)
                    if str_updated_fibo == original_num:
                        return True  
        return False  
        
                
    def check_for_next(self, num, j, str_to_find, fibo):
        if str_to_find == num[j:j+len(str_to_find)]:
            fibo.append(str_to_find)
            return True
        
                    
    def make_fibonacci(self, a, b, num, fibo):
        
        str_to_find = str(int(a) + int(b))
        if self.check_for_next(num, len(a) + len(b), str_to_find, fibo):
            # means next available
            self.make_fibonacci(b, str_to_find, num[len(a):], fibo)
        
        return fibo
      
