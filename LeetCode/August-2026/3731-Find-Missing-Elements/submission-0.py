class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        sett = set(nums)
        for i in range(min(nums), max(nums)):
            if i not in sett:
                res.append(i)
        return res

#Time Complexity: O(n)
#Space Complexity: O(n)

'''
Approach:
- Iterate through the range from the minimum to the maximum of the input list `nums`.
- For each number in that range, check if it is present in the set created from `the input list `nums`.
- If a number is not present in the set, append it to the result list `res`.
'''