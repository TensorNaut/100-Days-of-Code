class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
    
#Time Complexity: O(1)
#Space Complexity: O(1)
'''
Why this works:
1.  The sum of the first n even numbers is given by the formula: even_sum = n * (n + 1).

2.  The sum of the first n odd numbers is given by the formula: odd_sum = n * n.

3.  The GCD of even_sum and odd_sum can be simplified as follows:
    - even_sum = n * (n + 1)
    - odd_sum = n * n
    - GCD(even_sum, odd_sum) = GCD(n * (n + 1), n * n) = n * GCD(n + 1, n) = n

4.  Since n and n + 1 are consecutive integers, their GCD is always 1. 
    Therefore, the GCD of even_sum and odd_sum simplifies to n * 1 = n.

5.  Thus, the function returns n as the GCD of the sums of the first n even and odd numbers.
'''