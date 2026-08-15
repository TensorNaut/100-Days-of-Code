class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n * [0] == nums:
            return 0
        x = 0
        for i in nums:
            x ^= i

        return n if x else n-1

#Time complexity: O(n)
# Space complexity: O(1)

'''
Approach
- Check whether every element in the array is 0.
- If so, return 0.
- Compute the XOR of all elements.
- If the XOR is non-zero, return the array length.
- Otherwise, return n - 1.
'''