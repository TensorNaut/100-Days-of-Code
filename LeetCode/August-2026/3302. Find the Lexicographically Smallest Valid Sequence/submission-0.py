class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        
        n1, n2 = len(word1), len(word2)
        w2_idx, ans_len = n2 - 1, 0
        match_cnt, ans = [0] * (n1 + 1), []


        for w1_idx in range(n1 - 1, -1, -1):            # <-- #1)

            match_cnt[w1_idx] = match_cnt[w1_idx + 1]

            if w2_idx == -1: continue

            if word1[w1_idx] == word2[w2_idx]:
                match_cnt[w1_idx]+= 1
                w2_idx -= 1


        for w1_idx in range(n1):                        # <-- #2)

            if ans_len == n2: break

            if word1[w1_idx] == word2[ans_len]: 
                ans.append(w1_idx)
                ans_len+= 1
            
            elif match_cnt[w1_idx + 1] + ans_len >= n2 - 1:
                ans.append(w1_idx)
                ans_len+= 1
                break
    
        if ans_len == n2: return ans

        
        w1_idx = 0 if not ans else ans[-1] + 1          # <-- #3)
        w2_idx = ans_len

        if match_cnt[w1_idx] + w2_idx < n2: return []

        while w2_idx < n2:
            if word1[w1_idx] == word2[w2_idx]:
                ans.append(w1_idx)
                w2_idx += 1
            w1_idx += 1
        
        
        return ans




#Time Complexity: (O(n1 + n2))
#Space Complexity: O(n1)
'''
1.  We populate the match_cnt, a list that tracks how many characters from word2 can be matched from each position of word1 
    as we traverse word1 from right to left. We use match_cnt to track the potential number of matches starting from any 
    given index in word1. If the current character in word1 matches the current character in word2, the appropriate element 
    of match_cnt is incremented.

2.  We construct the initial sequence of indices ans, in which characters from word2 matched in word1. 
    It iterates over word1 , appending matching indices to ans. If the sequence length (ans_len) matches word2, 
    we have an exact match, so the loop exits early. If not, we continue the iteration.

3.  If we do not have an exact match in 2) above, we attempt to complete it by substituting one character per the 
    problem description.It starts from the next index after the last added match (or from the beginning if ans is empty). 
    If we cannot find all but one remaining match, we return []. 
    Otherwise, it continues adding indices until the sequence fully matches word2. 
    Finally, the completed sequence is returned.
'''