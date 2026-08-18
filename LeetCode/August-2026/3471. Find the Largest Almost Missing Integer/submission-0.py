from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)

        if k == 1:
            candidates = [x for x in freq if freq[x] == 1]
            return max(candidates) if candidates else -1

        if k == n:
            return max(nums)

        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])

        return max(candidates) if candidates else -1


#Time Complexity: O(n)
#Space Complexity: O(n)

'''
Approach:
1. We first count the frequency of each number in the input list `nums` using the `Counter` class from the `collections` module.
2. If `k` is equal to 1, we find all numbers that appear exactly once in the list and return the maximum among them. If there are no such numbers,
   we return -1.
3. If `k` is equal to the length of the list `n`, we return the maximum number in the list since all numbers are considered.
4. For other values of `k`, we check the first and last elements of the list. If either of them appears exactly once in the list, 
   we add them to the candidates list.
5. Finally, we return the maximum number from the candidates list if it is not empty;
'''