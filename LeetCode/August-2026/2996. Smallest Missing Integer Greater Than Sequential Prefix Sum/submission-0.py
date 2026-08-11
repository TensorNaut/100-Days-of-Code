class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix += nums[i]
            else:
                break
                
        while prefix in nums:
            prefix += 1
            
        return prefix

    
# Time complexity: O(n²) in the worst case, because checking prefix in nums takes O(n) for a list, and this check can be performed O(n) times.
# Space complexity: O(1), since only a constant amount of extra space is used.

'''
Approach:
- Find the sum of the longest consecutive prefix of the array.
- Start from this sum and check if it exists in nums.
- If it exists, increment it until finding an integer that is not present.
- Return that integer.
'''