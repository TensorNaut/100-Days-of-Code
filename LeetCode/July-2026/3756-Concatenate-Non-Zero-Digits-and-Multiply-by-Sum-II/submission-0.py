from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Prefix sum of digits
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (ord(ch) - ord('0'))

        # Store only non-zero digits and their positions
        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(ord(ch) - ord('0'))

        k = len(digits)

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(k):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        # Rolling hash of non-zero digits
        H = [0] * (k + 1)
        for i in range(k):
            H[i + 1] = (H[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            digit_sum = pref[r + 1] - pref[l]

            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                H[right + 1]
                - H[left] * pow10[length]
            ) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans
    


'''
Approach:
1.  Preprocess the string to compute the prefix sum of digits and store the positions and values
    of non-zero digits.

2.  For each query, calculate the sum of digits in the specified range using the prefix sum

3.  Use binary search to find the range of non-zero digits within the specified range.

4.  Compute the concatenated number of non-zero digits using a rolling hash technique and
    multiply it by the sum of digits.

5.  Return the result modulo 10^9 + 7.
'''