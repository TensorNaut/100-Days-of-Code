class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""

        for i in range(len(words)):
            val  = 0
            for j in range(len(words[i])):
                val += weights[ord(words[i][j]) - ord('a')]

            ch = chr(25 - (val%26) + ord('a'))
            ans += ch

        return ans
    
# Time Complexity: O(n * m) where n is the number of words and m is the average length of the words.
# Space Complexity: O(n) for storing the output string.
'''
The code defines a class `Solution` with a method `mapWordWeights` that takes 
a list of words and a list of weights.
For each word, it calculates a value by summing the weights of its characters 
(where the weight is determined by the position of the character in the alphabet). 
Then, it maps this value to a character by taking the modulus with 26 and adjusting it 
to get a character from 'a' to 'z'.
'''