class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum = n * (n + 1)
        odd_sum = n*n

        while odd_sum:
            even_sum, odd_sum = odd_sum, even_sum % odd_sum
        return even_sum
    
#Time Complexity: O(log N)
#Space Complexity: O(1)

'''
Approach:
1. Calculate the sum of the first n even numbers using the formula: even_sum = n * (n + 1).
2. Calculate the sum of the first n odd numbers using the formula: odd_sum = n * n.
3. Use the Euclidean algorithm to compute the GCD of even_sum and odd_sum. 
   This is done by repeatedly replacing even_sum with odd_sum and odd_sum with even_sum % odd_sum 
   until odd_sum becomes zero.
4. Return the final value of even_sum, which will be the GCD of the two sums.
'''