import bisect
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        total_ones = s.count('1')
        n = len(s)
        
        Z_blocks = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                Z_blocks.append((start, i - 1))
            else:
                i += 1
                
        K = len(Z_blocks)
        
        if K < 2:
            return [total_ones] * len(queries)
            
        U = [u for u, v in Z_blocks]
        V = [v for u, v in Z_blocks]
        Z_len = [v - u + 1 for u, v in Z_blocks]
        
        A_val = [Z_len[i] + Z_len[i+1] for i in range(K - 1)]
        
        LOG = (K - 1).bit_length() + 1
        st_A = [[0] * (K - 1) for _ in range(LOG)]
        
        for i in range(K - 1):
            st_A[0][i] = A_val[i]
            
        for k in range(1, LOG):
            step = 1 << (k - 1)
            for i in range(K - 1 - (1 << k) + 1):
                st_A[k][i] = max(st_A[k-1][i], st_A[k-1][i + step])
                
        def query_st_A(start: int, end: int) -> int:
            if start > end:
                return -1
            k = (end - start + 1).bit_length() - 1
            return max(st_A[k][start], st_A[k][end - (1 << k) + 1])
            
        ans = []
        
        for l, r in queries:
            L = bisect.bisect_left(V, l)
            R = bisect.bisect_right(U, r) - 1
            
            if R < L + 1:
                ans.append(total_ones)
                continue
                
            Z_L_len = min(V[L], r) - max(U[L], l) + 1
            Z_R_len = min(V[R], r) - max(U[R], l) + 1
            
            if R == L + 1:
                max_gain = Z_L_len + Z_R_len
            else:
                max_gain = max(
                    Z_L_len + Z_len[L+1],
                    Z_len[R-1] + Z_R_len,
                    query_st_A(L + 1, R - 2)
                )
                
            ans.append(total_ones + max_gain)
            
        return ans
    

# Time Complexity: O(n + q * log K)
# Space Complexity: O(n + K * log K)

'''
Algorithm:
1. Count the total number of '1's in the string `s`.
2. Identify all contiguous sections of '0's and store their start and end indices in `Z_blocks`.
3. If there are less than 2 sections of '0's, return the count of '1's for each query.
4. Prepare arrays `U`, `V`, and `Z_len` to store the start indices, end indices, and lengths of the '0' sections respectively.
5. Create an array `A_val` to store the sum of lengths of adjacent '0' sections.
6. Build a Sparse Table `st_A` for range maximum queries on `A_val`.
7. For each query, use binary search to find the relevant sections of '0's that intersect with the query range.
8. Calculate the maximum gain from merging sections of '0's within the query range and add it to the total count of '1's.
9. Return the results for all queries.
'''