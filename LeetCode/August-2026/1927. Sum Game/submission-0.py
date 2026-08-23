class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left = num[0:n//2]
        right = num[n//2:]

        leftSum = rightSum = 0 
        leftQ = rightQ = 0

        for i in left:
            if i == '?':
                leftQ += 1
            else:
                leftSum += int(i)

        for i in right:
            if i == '?':
                rightQ += 1
            else:
                rightSum += int(i)

        if (leftQ + rightQ)%2 != 0:
            return True

        diff = leftSum - rightSum
        target = (rightQ - leftQ)/2*9
        
        return diff != target


#Time ComplexityL O(n)
#Space ComplexityL O(n)
'''
Approach
    1. Split the string into two equal halves and calculate the sum of digits and count of ? in each half.
    2. If the total number of ? is odd, Alice can always make the final sums unequal, so return True.
    3. Otherwise, calculate the current sum difference between the two halves.
    4. Calculate the maximum adjustment possible using the ? values. 
       If the current difference exactly matches this adjustment, Bob can force equal sums; otherwise, Alice wins.
'''