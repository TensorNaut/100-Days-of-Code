class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ones = 0
        sections = []

        i = 0
        while i < n:
            if s[i] == "0":
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                sections.append(j-i)
                i = j
            else:
                ones += 1
                i += 1

        if len(sections) < 2:
            return ones
        
        best = 0
        for i in range(1, len(sections)):
            best = max(best, sections[i] + sections[i-1])

        return ones + best


#Time Complexity: O(n)
#Space Complexity: O(n)

'''
Algorithm:
1. Initialize a variable `ones` to count the number of '1's in the string
2. Identify all contiguous sections of '0's and store their lengths
3. If there are less than 2 sections of '0's, return the count of '1's
4. Otherwise, find the maximum sum of two adjacent sections of '0's
5. Return the count of '1's plus the maximum sum found
'''