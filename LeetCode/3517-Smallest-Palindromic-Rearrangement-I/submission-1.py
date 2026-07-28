
from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        half = []
        mid = ""
        for ch, cnt in freq.items():
            half.append(ch * (cnt // 2))
            if cnt % 2:
                mid = ch

        half.sort()
        left = ''.join(half)

        res = left + mid + left[::-1]

        return res

#Time Complexity: O(nlogn) where n is the length of the string s. The sorting step takes O(nlogn) time.
#Space Complexity: O(n) where n is the length of the string s. We use additional space to store the frequency count and the half string.

'''
Alternative Approach:
1.  Count the frequency of each character in the string s using a Counter.
2.  Create a list half to store half of the characters that will form the left half of the palindrome.
3.  Iterate through the frequency count and for each character, append half of its count to the half list. 
    If the count is odd, store the character as the middle character (mid).
4.  Sort the half list to ensure the smallest lexicographical order.
5.  Join the half list to form the left half of the palindrome.
6.  Construct the final palindrome by concatenating the left half, the middle character (if any), 
    and the reverse of the left half.
'''