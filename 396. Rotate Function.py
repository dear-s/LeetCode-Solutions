
# 2026 solution - with written notes ~ see "396. Rotate Function - written notes" file
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        # dynamic mathematical programming - need to write the formula by hand in order to understand it
        # F(1) = F(0) + sum - n (arr[-1]) --->>>> last element of previous rotated array

        output = float("-inf")

        # cal F(0) first and sum
        summ = sum(nums)
        n = len(nums)
        f0 = 0
        for i in range(0,n):
            f0 += i*nums[i]
        # print("f0: ", f0)

        fPrev = f0
        output = f0
        
        i = 1
        while i != n:
            print(nums[n-i])
            fn = fPrev + summ - (n * (nums[n-i]))
            # print("new fn: ", fn, " at i: ", i)
            output = max(output, fn)
            fPrev = fn
            i+=1
        
        return output

        
    #     output = float("-inf")

    #     #  number of times, we will rotate and find the max from those rotations functions
    #     for i in range(0,len(nums)):
    #         # given index - we will rotate it
    #         if i != 0:
    #             # do rotation once and forward it in the next runs
    #             n = nums.pop() # remove last item
    #             nums.insert(0, n) # move last item at index-0

    #         output = max(output, self.functionComputation(nums))

    #     return output


    # def functionComputation(self, rNums):

    #     ans = 0
    #     for i in range(0,len(rNums)):
    #         ans += i*rNums[i]

    #     return ans


# ----------------------------
# 2020 solution


# class Solution:
#     def maxRotateFunction(self, A: List[int]) -> int:
        
#         # F(1) = F(0) + sum - (length) * first_element
        
#         total = sum(A)
#         f_zero = 0
#         for a in range(len(A)):
#             f_zero += a * A[a]
            
#         function = f_zero        
        
#         for k in range(len(A)-1):
#             number = A[k]
#             function = function - total + len(A)*number
#             if function > f_zero:
#                 f_zero = function
            
#         return f_zero
        
        
        
#         if len(A) == 0: return 0
#         max_val = float('-inf')
        
#         # rotate and run function 'k' many times
#         for k in range(len(A)):
#             # rotate array once
#             new_array = [A[-1]] + A[:len(A)-1]
#             ans_sum = self.function_f_of_k(new_array)
#             if ans_sum > max_val:
#                 max_val = ans_sum
            
#             A = new_array
            
#         return max_val

        
#     def function_f_of_k(self, array):
        
#         sum_return = 0

#         for i in range(len(array)):
#             sum_return += i * array[i] # index * value
            
#         return sum_return
