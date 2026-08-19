class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, c in reservedSeats:
            rows.setdefault(r, set()).add(c)

        ans = 2 * n

        for reserved in rows.values():
            left = {2, 3, 4, 5}
            right = {6, 7, 8, 9}
            middle = {4, 5, 6, 7}

            left_free = not (reserved & left)
            right_free = not (reserved & right)
            middle_free = not (reserved & middle)

            if left_free and right_free:
                # Can fit 2 families, so no adjustment needed
                continue
            elif left_free or right_free or middle_free:
                # Can fit 1 instead of the assumed 2
                ans -= 1
            else:
                # Can fit 0 instead of the assumed 2
                ans -= 2

        return ans


#Time Complexity: O(m), where m is the number of reserved seats.
#Space Complexity: O(m)

'''
Approach:
1. Create a dictionary to store the reserved seats for each row.
2. For each row, check the availability of the left, right, and middle blocks of seats.
3. If both left and right blocks are free, we can fit 2 families, so no adjustment is needed.
4. If either left, right, or middle block is free, we can fit 1 family instead of the assumed 2, so we decrement the answer by 1.
5. If none of the blocks are free, we can fit 0 families instead of the assumed 2, so we decrement the answer by 2.
'''