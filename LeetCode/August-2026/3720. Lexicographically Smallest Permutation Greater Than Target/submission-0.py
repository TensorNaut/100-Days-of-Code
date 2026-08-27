from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        cnt = Counter(s)

        # Try changing target from right to left
        for i in range(len(target) - 1, -1, -1):

            # Count characters used before i
            remaining = Counter(s)

            possible = True

            for j in range(i):
                if remaining[target[j]] == 0:
                    possible = False
                    break

                remaining[target[j]] -= 1

            if not possible:
                continue

            # Find the smallest character greater than target[i]
            for ch in sorted(remaining):

                if ch > target[i] and remaining[ch] > 0:

                    remaining[ch] -= 1

                    # Fill the rest with smallest characters
                    result = target[:i] + ch

                    for c in sorted(remaining):
                        result += c * remaining[c]

                    return result

        return ""


# Time Complexity: O(n^2)
# Space Complexity: O(n)

'''
Approach:
1. Use Counter to store the frequency of each character in s.

2. Traverse the target string from right to left. For each position,
   check whether the prefix before that position can be formed using
   the available characters from s.

3. Try replacing the current character with the smallest available
   character that is greater than it. Once found, append all remaining
   characters in sorted order to get the smallest possible permutation.

4. If no position can be increased, return an empty string because
   no permutation of s is lexicographically greater than target.
'''