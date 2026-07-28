from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        half = []
        mid = ""

        for i in range(26):
            ch = chr(ord('a') + i)

            if ch in freq:
                half.append(ch * (freq[ch] // 2))
                if freq[ch] % 2:
                    mid = ch

        base = ''.join(half)
        res = base + mid + base[::-1]

        return res

# Time Complexity: O(n) where n is the length of the string s.
# Space Complexity: O(n) where n is the length of the string s.

'''
Optimized Approach:
1. Count the frequency of each character in the string using a Counter.
2. Initialize an empty list `half` to store the left half of the palindrome
   and an empty string `mid` to store the middle character (if any).
3. Iterate through the lowercase English letters from 'a' to 'z' in
   lexicographical order.
4. For each character, append `freq[ch] // 2` occurrences to `half`.
   If its frequency is odd, store it as the middle character.
5. Join the strings in `half` to form the left half of the palindrome.
6. Construct the final palindrome by concatenating the left half,
   the middle character, and the reverse of the left half.
'''