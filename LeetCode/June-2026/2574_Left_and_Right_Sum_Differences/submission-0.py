#O(n) time, O(n) space
'''
Given a 0-indexed integer array nums, return an array 
answer of the same length where answer[i] is equal to 
the absolute difference between the sum of the elements 
to the left of i and the sum of the elements to the right of i.

Note that the sum of the elements to the left of index 0 is considered to be 0, 
and the sum of the elements to the right of index n - 1 is also considered to be 0.
'''

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftsum = [0]
        rightsum = []

        l = 0
        for i in range(1, n):
            l += nums[i-1]
            leftsum.append(l)

        r = sum(nums)
        for i in range(n):
            r -= nums[i]
            rightsum.append(r)

        res = [abs(a-b) for a,b in zip(leftsum, rightsum)]

        return res
    
