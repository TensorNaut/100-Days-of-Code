import math

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return max(math.prod(nums[:3]), math.prod(nums[-2:])*nums[0])

#Time Complexity: O(nlogn) where n is the length of nums. This is due to the sorting step.
#Space Complexity: O(1) since we are sorting in place and using a constant amount of extra space.
'''
Approach:
1. Sort the array in descending order.
2. The maximum product can be either:
   - The product of the three largest numbers.
   - The product of the two smallest (most negative) numbers and the largest number.
3. Return the maximum of these two possibilities.
'''