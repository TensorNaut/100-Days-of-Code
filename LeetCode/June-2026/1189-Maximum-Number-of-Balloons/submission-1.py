from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"], count["a"], count["l"]//2, count["o"]//2, count["n"])
    
#Time Complexity: O(n) where n is the length of the input string text. We iterate through the string once to count the occurrences of each character.
#Space Complexity: O(1) as we are using a constant amount of extra space to store the counts of each character.
