class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        temp = n
        while temp:
            summ += temp%10
            prod *= temp%10
            temp //= 10

        return  n%(summ+prod) == 0



# Time complexity: O(log n)
# Space complexity: O(1)

