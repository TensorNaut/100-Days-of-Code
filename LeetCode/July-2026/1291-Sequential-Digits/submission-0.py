class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        s = "123456789"

        low_len = len(str(low))
        high_len = len(str(high))

        for i in range(low_len, high_len+1):
            for j in range(10-i):
                num = int(s[j: j+i])
                if low <= num <= high:
                    res.append(num)
        
        return res


#Time Complexity: O(1), since the number of sequential digits is limited and does not depend on the input size.
#Space Complexity: O(1), as the space used does not scale with the input size

'''
Approach:
1.  Create a string `s` containing the digits from 1 to 9.
2.  Determine the lengths of the `low` and `high` numbers.
3.  Iterate through the lengths from `low_len` to `high_len`.
4.  For each length `i`, generate all possible sequential digits by slicing the string `s` from 
    index `j` to `j+i`.
5.  Convert the sliced string to an integer and check if it falls within the range [low, high]. 
    If it does, append it to the result list.
6.  Return the result list containing all valid sequential digits within the specified range.
'''