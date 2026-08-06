class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(num):
            x = 1
            while num != 0:
                x *= num%10
                num //= 10
            return x

        while prod(n) % t != 0:
            n += 1

        return n



#Time Complexity: O(K log N), where K is the number of iterations needed to find the answer and log N is the time taken to compute the product of digits for each number.
#Space Complexity: O(1)
#Key Idea: Iterate from n upwards, checking if the product of digits is divisible by t.