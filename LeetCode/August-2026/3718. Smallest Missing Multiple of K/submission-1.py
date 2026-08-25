class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        multiple = k
        while multiple in nums:
            multiple += k
        return multiple

#Time Complexity: O(n + m), where n is the length of nums and m is the smallest missing multiple of k.
#Space Complexity: O(n), where n is the length of nums.
'''
Approach:
    1. Convert the input list nums into a set for O(1) lookups.
    2. Initialize a variable multiple to k, which will be used to find the smallest missing multiple of k.
    3. Use a while loop to check if multiple is present in the set.
    4. If multiple is found in the set, increment multiple by k and continue checking.
    5. If multiple is not found in the set, return multiple as the smallest missing multiple of k.
'''