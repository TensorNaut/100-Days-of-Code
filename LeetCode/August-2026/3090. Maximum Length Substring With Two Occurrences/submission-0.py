from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        left = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


#Time Complexity: O(n)
#Space Complexity: O(1)

'''
Approach: Sliding Window
- Use two pointers to maintain a window of characters with at most two occurrences of each character.
- Expand the window by moving the right pointer and update character frequencies.
- If any character exceeds two occurrences, shrink the window from the left until all characters have at most two occurrences.
- Keep track of the maximum window size encountered.
'''