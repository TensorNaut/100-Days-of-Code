from collections import defaultdict
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = defaultdict(int)

        for ch in word:
            freq[ch] +=1

        frequencies = sorted(freq.values(), reverse=True)

        ans = 0

        for i, f in enumerate(frequencies):
            ans += f * (i // 8 + 1)

        return ans

# Time Complexity: O(n log n)
# Space Complexity: O(n)
'''
Approach:
1. Count the frequency of each character in the input word.
2. Sort the character frequencies in descending order.
3. Assign the first 8 characters to cost 1 push each, the next 8 to cost 2, and so on.
4. Accumulate the weighted pushes to return the minimum total.
'''