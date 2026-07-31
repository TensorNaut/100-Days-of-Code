class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []

        for i in s:
            freq[i] -= 1
            if i in seen:
                continue
            while stack and stack[-1] > i and freq[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(i)
            seen.add(i)

        return "".join(stack)
    
#Time Complexity: O(n)
#Space Complexity: O(n)
'''
Algorithm:
1. Create a frequency counter for the characters in the string.
2. Initialize an empty set to keep track of seen characters and an empty stack to build the result.
3. Iterate through each character in the string:
   a. Decrease the frequency of the current character.
   b. If the character has already been seen, skip it.
   c. While the stack is not empty and the top character of the stack is greater than the current character and 
      there are still occurrences of the top character left in the string, pop the top character from the stack 
      and remove it from the seen set.
   d. Append the current character to the stack and add it to the seen set.
4. Finally, join the characters in the stack to form the result string and return it. 
'''