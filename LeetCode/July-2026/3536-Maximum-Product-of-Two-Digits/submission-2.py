class Solution:
    def maxProduct(self, n: int) -> int:
        mx = 0 
        mx2 = 0
        while n != 0:
            temp = n%10
            if temp >= mx:
                mx2 = mx
                mx = temp
            elif temp >= mx2:
                mx2 = temp
            n //= 10
        return mx*mx2

#Time Complexity: O(d) where d is the number of digits in n. The while loop iterates through each digit of n once.
#Space Complexity: O(1) as we are using a constant amount of space to store the maximum and second maximum digits.
'''
Approach: Linear Scan

Optimization: 
- Instead of sorting the digits or calculating the product of all pairs, 
- we can find the two largest digits in a single pass through the digits. 
- This reduces the time complexity to O(d) and space complexity to O(1).
'''