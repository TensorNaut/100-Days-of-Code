class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum = 0
        rev = 0

        # Build the number without zeros, but in reverse order
        while n:
            digit = n % 10
            if digit:
                digit_sum += digit
                rev = rev * 10 + digit
            n //= 10

        # Reverse it back to restore original order
        num = 0
        while rev:
            num = num * 10 + rev % 10
            rev //= 10

        return num * digit_sum
    
#Time Complexity: O(log n)
#Space Complexity: O(1) more optimized than previous solution since we don't use extra space for an array.

'''
Approach: 
    1. Extract non-zero digits from the number and calculate their sum.
    2. Build the number without zeros in reverse order.
    3. Reverse it back to restore the original order of digits.
    4. Return the product of the concatenated number and the sum of the digits.
'''