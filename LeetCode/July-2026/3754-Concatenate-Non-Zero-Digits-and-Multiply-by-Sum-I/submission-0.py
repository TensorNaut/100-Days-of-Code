class Solution:
    def sumAndMultiply(self, n: int) -> int:
        arr = []
        while n != 0:
            temp = n%10
            if temp != 0:
                arr.append(temp)
            n //= 10

        arr.reverse()
        res = 0
        for i in arr:
            res *= 10
            res += i

        return res * sum(arr)
    
#Time Complexity: O(log n)
#Space Complexity: O(log n)

'''
Brute Force Approach: 
    1. Extract non-zero digits from the number and store them in an array.
    2. Reverse the array to maintain the original order of digits.
    3. Concatenate the digits to form a new number.
    4. Calculate the sum of the non-zero digits.
    5. Return the product of the concatenated number and the sum of the digits.
'''