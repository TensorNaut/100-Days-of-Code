class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix += nums[i]
            else:
                break

        nums_set = set(nums)
                
        while prefix in nums_set:
            prefix += 1
            
        return prefix



#Time complexity: O(n) average, since we traverse the array once and use O(1) average-time hash set lookups.
#Space complexity: O(n), because we store the elements of nums in a hash set.

'''
Approach:

- Calculate the sum of the longest consecutive prefix.
- Put all elements into a hash set for O(1) average lookup.
- Starting from the prefix sum, increment it while it exists in the set.
- Return the first integer that is not present.
'''