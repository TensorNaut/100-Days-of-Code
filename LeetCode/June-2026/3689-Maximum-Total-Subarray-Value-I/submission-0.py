class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_val = min_val = nums[0]
        
        for num in nums:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num

        return k*(max_val - min_val)
    
# Time Complexity: O(n) where n is the length of the input array nums.
# Space Complexity: O(1) since we are using only a constant amount of extra space to store the maximum and minimum values.
'''
The algorithm iterates through the input array nums once 
to find the maximum and minimum values. 
It then calculates the maximum total value of a subarray of length k 
using the formula k * (max_val - min_val). 
This works because the maximum total value of a subarray of length k is achieved when 
all elements in the subarray are equal to the maximum value, 
and the minimum value is subtracted from it to get the total value.'''