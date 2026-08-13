class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)

        # Each node:
        # [length, left_char, right_char, prefix, suffix, best]
        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right

            if right is None:
                return left

            length = left[0] + right[0]

            left_char = left[1]
            right_char = right[2]

            prefix = left[3]
            suffix = right[4]

            best = max(left[5], right[5])

            # Can the suffix of left and prefix of right join?
            if left[2] == right[1]:
                combined = left[4] + right[3]
                best = max(best, combined)

                # Entire left segment is the same character
                if left[3] == left[0]:
                    prefix = left[0] + right[3]

                # Entire right segment is the same character
                if right[4] == right[0]:
                    suffix = right[0] + left[4]

            return [
                length,
                left_char,
                right_char,
                prefix,
                suffix,
                best
            ]

        def build(node, start, end):
            if start == end:
                tree[node] = [
                    1,          # length
                    s[start],   # left_char
                    s[start],   # right_char
                    1,          # prefix
                    1,          # suffix
                    1           # best
                ]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, start, end, idx, char):
            if start == end:
                tree[node] = [
                    1,
                    char,
                    char,
                    1,
                    1,
                    1
                ]
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, end, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)

            # tree[1] represents the entire string
            ans.append(tree[1][5])

        return ans



#Time Complexity: O(n + q log n), where n = len(s) and q = number of queries.
#Space Complexity: O(n) for the segment tree.

'''
Approach

1. Store information for every segment in a segment tree:
   - prefix → longest repeating sequence starting from the left.
   - suffix → longest repeating sequence ending at the right.
   - best → longest repeating sequence anywhere in the segment.
   - left_char / right_char → first and last characters of the segment.

2. Merge two segments:
    - Take the maximum best from both segments.
    - If left.right_char == right.left_char, the suffix of the left segment and prefix of the right segment can be joined.
    - Therefore, check:left.suffix + right.prefix
    - Update prefix and suffix if an entire segment consists of the same character.

3. For each character update, update only the path from the modified leaf to the root.
    - This takes O(log n).
    - The root always represents the entire string, so root.best gives the answer after each query.
'''
