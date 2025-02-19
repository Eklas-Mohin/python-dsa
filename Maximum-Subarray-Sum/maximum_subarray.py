class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
        