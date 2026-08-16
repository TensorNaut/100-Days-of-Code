class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1

        if cnt[0] % 2 == 0:
            return cnt[1] >= 1 and cnt[2] >= 1
        else:
            return abs(cnt[1] - cnt[2]) > 2


# Time Complexity: O(n)     Single pass to bucket stones by residue
# Space Complexity: O(1)    Fixed-size count array of length 3

'''
Approach
- Count stones by value % 3 into cnt[0], cnt[1], cnt[2] — O(n).
- Check the parity of cnt[0].
- Apply the corresponding condition above.
- Return the boolean result — O(1) after counting.
-No simulation, no per-stone game tree needed, the entire game outcome is determined by three integers.
'''