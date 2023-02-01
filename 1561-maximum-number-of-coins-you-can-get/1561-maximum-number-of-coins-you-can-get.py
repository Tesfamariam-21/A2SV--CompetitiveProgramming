class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        myPile = 0
        
        for i in range(len(piles)-1,len(piles)//3,-2):
            myPile += piles[i-1]
           
        return myPile
            
        