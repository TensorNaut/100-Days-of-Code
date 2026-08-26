class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)

        for i in range(n):

            oneCnt = 0
            cur = ""

            for j in range(i, n):

                cur += s[j]

                if s[j] == '1':
                    oneCnt += 1

                if oneCnt > k:
                    break

                if oneCnt == k:
                    if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                        ans = cur

        return ans

#Time Complexity: O(n^2), where n is the length of the input string s.
#Space Complexity: O(n), where n is the length of the input string s.
'''
Approach:
    1. Initialize an empty string ans to store the shortest beautiful substring.
    2. Iterate through each character in the input string s using index i.
    3. For each starting index i, initialize a counter oneCnt to count the number of '1's and an empty string cur to build the current substring.
    4. Use a nested loop with index j starting from i to iterate through the substring.
    5. Append the current character s[j] to cur and update oneCnt if s[j] is '1'.
    6. If oneCnt exceeds k, break out of the inner loop as we cannot have more than k '1's.
    7. If oneCnt equals k, check if cur is shorter than ans or lexicographically smaller if they are of equal length, and update ans accordingly.
    8. After checking all substrings, return ans as the shortest beautiful substring.
'''