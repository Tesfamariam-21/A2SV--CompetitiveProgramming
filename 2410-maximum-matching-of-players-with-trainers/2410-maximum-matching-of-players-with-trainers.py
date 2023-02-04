class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
#        length of player and trainer so we could iterate over the min
        playerSize = len(players)
        trainerSize = len(trainers)
#         sort them to compare
        players.sort()
        trainers.sort()
#         assign a right and left pointer for player and trainers respectivly

        right = 0
        left = 0
        matches = 0
        # for i in ragne(min(playerSize, trainerSize)):
        while right < trainerSize and left < playerSize:
            if players[left] <= trainers[right]:
                matches +=1
                left +=1
                right += 1
            else:
                right +=1
                
        return matches
                
            