class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)

        num = 0
        digit_sum = 0

        for ch in s:
            d = ord(ch) - ord('0')
            if d:
                num = num * 10 + d
                digit_sum += d

        return num * digit_sum
    
#Time Complexity: O(log n)
#Space Complexity: O(log n) since we convert the number to string

'''
Optimized Approach: 
    1. Convert the number to a string to easily iterate through its digits.
    2. For each digit, if it is non-zero, build the new number and calculate the sum of the digits.
    3. Return the product of the concatenated number and the sum of the digits.
'''