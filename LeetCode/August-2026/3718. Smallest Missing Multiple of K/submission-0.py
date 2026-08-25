class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        x = 1
        while True:
            if x*k not in s:
                return x*k
            x += 1

#Time Complexity: O(n + m), where n is the length of nums and m is the smallest missing multiple of k.
#Space Complexity: O(n), where n is the length of nums.
'''
Approach:
    1. Convert the input list nums into a set for O(1) lookups.
    2. Initialize a variable x to 1, which will be used to find the smallest missing multiple of k.
    3. Use a while loop to check if x*k is present in the set.
    4. If x*k is not found in the set, return x*k as the smallest missing multiple of k.
    5. If x*k is found, increment x and continue checking.
'''