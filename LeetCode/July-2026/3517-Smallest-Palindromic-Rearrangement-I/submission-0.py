class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        half = []
        mid = []

        for key, val in freq.items():
            if val % 2 == 0:
                half.append(key*(val//2))
            elif val%2 != 0 and val > 1:
                half.append(key*((val-1)//2))
                mid.append(key)
            else:
                mid.append(key*val)

        res = ''.join(sorted(half) + sorted(mid) + sorted(half)[::-1])

        return res


#Time Complexity: O(nlogn) where n is the length of the string s. The sorting operation takes O(nlogn) time.
#Space Complexity: O(n) where n is the length of the string s. We are using additional space to store the frequency dictionary, half list, and mid list.

'''
Algorithm:
1.  Create a frequency dictionary to count the occurrences of each character in the input string `s`.

2.  Initialize two lists: `half` to store half of the characters for the palindrome and `mid` to store any character
    that can be placed in the middle of the palindrome (if it has an odd frequency).

3.  Iterate through the frequency dictionary:
    - If the frequency of a character is even, append half of its occurrences to the `half` list.
    - If the frequency is odd and greater than 1, append half of its occurrences to the `half` list and add one occurrence to the `mid` list.
    - If the frequency is odd and equal to 1, add it to the `mid` list.

4.  Sort the `half` list and the `mid` list to ensure the smallest lexicographical order.

5.  Construct the final palindrome by concatenating the sorted `half` list, the sorted `mid` list, 
    and the reverse of the sorted `half` list.
'''