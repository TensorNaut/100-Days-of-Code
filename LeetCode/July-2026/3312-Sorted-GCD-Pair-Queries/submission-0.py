from math import gcd
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        arr = [0] * (mx+1)
        for num in nums:
            arr[num] += 1

        for i in range(1, mx+1):
            for j in range(i*2, mx+1, i):
                arr[i] += arr[j]

        for i in range(1, mx+1):
            #arr[i] = comb(arr[i], 2)
            arr[i] = arr[i] * (arr[i] - 1) // 2

        for i in range(mx, 0, -1):
            for j in range(i*2, mx+1, i):
                arr[i] -= arr[j]

        for i in range(1, mx+1):
            arr[i] += arr[i-1]
        
        res = []

        for q in queries:
            idx = bisect.bisect_left(arr, q+1)
            res.append(idx)

        return res
    

#Time Complexity: O(m log m), where m is the maximum number in nums  
#Space Complexity: O(m log m), where m is the maximum number in nums
'''
Algorithm Explanation:
1.  First, we find the maximum number in the input list `nums` and create an array `arr` of size `mx + 1` initialized to zero. 
    This array will be used to count the occurrences of each number in `nums`.

2.  We iterate through each number in `nums` and increment the corresponding index in `arr to count how many times each number appears.

3.  Next, we iterate through the `arr` array to count the number of pairs (i, j) such that gcd(i, j) = i. 
    For each number i, we add the counts of its multiples (j = 2*i, 3*i, ...) to arr[i].

4.  We then calculate the number of pairs for each gcd value using the formula for combinations:
      - For each i, the number of pairs is given by arr[i] * (arr[i] - 1) // 2, 
        which represents the number of ways to choose 2 elements from arr[i].

5.  After that, we iterate through the `arr` array in reverse order to subtract the counts of pairs for multiples of each gcd value. 
    This ensures that we only count pairs where gcd(i, j) = i and not any multiples of i.

6.  We then compute the prefix sum of the `arr` array so that arr[i] contains the total number of pairs with gcd values less than or equal to i.

7.  Finally, for each query in `queries`, we use binary search (via `bisect.bisect_left`) to find the smallest index in `arr` such 
    that arr[index] >= query + 1. This index represents the number of pairs with gcd values less than or equal to the query value, 
    and we append this index to the result list.

8.  The function returns the result list containing the answers for all queries.
'''