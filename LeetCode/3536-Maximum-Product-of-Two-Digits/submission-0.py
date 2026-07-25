class Solution:
    def maxProduct(self, n: int) -> int:
        dig = [int(x) for x in str(n)]
        prod = []
        for i in range(len(dig)-1):
            for j in range(i+1, len(dig)):
                prod.append(dig[i]*dig[j])

        return max(prod)


#Time Complexity: O(d^2) where d is the number of digits in n. The nested loops iterate through all pairs of digits to calculate their products.
#Space Complexity: O(d^2) where d is the number of digits in n. The list prod stores all the products of pairs of digits, which can be at most d*(d-1)/2 products.

#Approach: Brute Force
