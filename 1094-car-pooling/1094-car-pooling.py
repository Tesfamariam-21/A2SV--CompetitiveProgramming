class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:  
        lengthOfTrip = [0] * 1001 
        
        
        for trip, i, j in trips:
            lengthOfTrip[i] += trip 
            lengthOfTrip[j] -= trip 
            
        carLoad = 0
        
        for i in range( len(lengthOfTrip) ):
            carLoad += lengthOfTrip[i] 
            if carLoad > capacity: 
                return False                
        return True
        