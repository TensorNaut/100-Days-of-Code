class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)

        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
    

#Time Complexity: O(N)
#Space Complexity: O(N)

'''
Approach
- Sliding Window and Hash Table

Key Idea:
- Use a sliding window with a hash map to track element frequencies and maintain the constraint.

    1. left and right define our current subarray.
    2. freq stores how many times each number occurs in the current window.
    3. Expand right.
    4. If nums[right] makes its frequency > k, move left forward until the window becomes valid again.
    5. Keep track of the maximum window length.
'''