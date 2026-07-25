class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = map(int, sorted(str(n))[-2:len(str(n))])
        return a*b

#Time Complexity: O(d log d) where d is the number of digits in n. The sorting operation takes O(d log d) time.
#Space Complexity: O(d) where d is the number of digits in n. The sorted function creates a new list of digits, which takes O(d) space.
'''
Approach: Sorting
Optimization: Instead of calculating the product of all pairs of digits, 
we can sort the digits and take the two largest digits to calculate their product. 
This reduces the time complexity from O(d^2) to O(d log d) due to sorting.
'''