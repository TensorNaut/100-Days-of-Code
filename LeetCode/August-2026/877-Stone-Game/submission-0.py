class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


#Time Complexity: O(1) since we always return True
#Space Complexity: O(1) since we do not use any additional space

'''
- The number of piles is always even.
- Alex always moves first
- The total number of stones is odd, therefore, impossiblity of a tie
- Given that alex always move first, 
  alex is able to make certain that she always choses iether the odd indices or even indices, 
  for example:

    a b c d e f (letters represent piles)
    0 1 2 3 4 5 (indices)
    alex can chose iether a or f
    say alex chooses 'a'
    lee is left with b c d e f
- doesnt matter what lee chooses now , 
- alex will always have the option to choose c or e in the next turn

- thus by this logic we can make sure that alex is able to choose iether odd or even index piles EVERYTIME

therefore, alex simply makes sure that she chooses whichever indices' sum is max (odd idices or even indices).

Hence proved that when alex plays optimally, she always wins
'''