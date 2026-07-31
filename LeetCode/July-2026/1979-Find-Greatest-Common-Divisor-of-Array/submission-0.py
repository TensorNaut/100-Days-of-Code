class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)

        while b != 0:
            a , b = b, a%b
        return a
    
#Time Complexity: O(n), where n is the length of the input list `nums`.
#Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
'''
Algorithm Explanation:
1.  The function `findGCD` takes a list of integers `nums` as input and returns the greatest common divisor (GCD) 
    of the minimum and maximum values in the list.
2.  We first find the minimum value `a` and the maximum value `b` in the input list `nums` using the built-in 
    `min()` and `max()` functions.
3.  We then use the Euclidean algorithm to compute the GCD of `a` and `b`. The algorithm works as follows:
    - While `b` is not zero, we repeatedly update `a` to be `b`, and `b` to be the remainder of `a` divided by `b` 
      (i.e., `a % b`).
4.  When `b` becomes zero, the value of `a` at that point is the GCD of the original minimum and maximum values.
5.  Finally, we return the value of `a`, which is the GCD of the minimum and maximum values in the input list `nums`.
''' 