from math import gcd

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        calendrix = (s, target)
        target_str = calendrix[1]
        
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        odd = 0
        mid_char = ''
        for i in range(26):
            if cnt[i] % 2 != 0:
                odd += 1
                mid_char = chr(i + ord('a'))

        if odd > 1:
            return ""

        half_cnt = [x // 2 for x in cnt]
        n_half = len(s) // 2
        half_str = [''] * n_half

        def find(k, is_greater):
            if k == n_half:
                rev_half = half_str[::-1]
                res = ''.join(half_str) + mid_char + ''.join(rev_half)
                return res > target_str

            start_c = 'a' if is_greater else target_str[k]
            for c_ord in range(ord(start_c), ord('z') + 1):
                c = chr(c_ord)
                if half_cnt[c_ord - ord('a')] > 0:
                    half_str[k] = c
                    half_cnt[c_ord - ord('a')] -= 1
                    if find(k + 1, is_greater or c > target_str[k]):
                        return True
                    half_cnt[c_ord - ord('a')] += 1
            return False

        if find(0, False):
            rev_half = half_str[::-1]
            return ''.join(half_str) + mid_char + ''.join(rev_half)
        return ""


# Time Complexity: O(n^2)
# Space Complexity: O(n)

'''
Approach:
    1. Count the frequency of each character in s and check if a palindromic permutation is possible 
       (at most one character can have an odd count).
    2. If a palindromic permutation is possible, construct half of the palindrome and use backtracking 
       to find the lexicographically smallest permutation that is greater than the target.
    3. Use a recursive function to build the half of the palindrome, ensuring that at each step, we either 
       match the target character or choose a greater character to ensure the final result is greater than 
       the target.
    4. If a valid permutation is found, construct the full palindrome by mirroring the half and adding the 
       middle character if necessary.
    5. If no valid permutation is found, return an empty string.
'''