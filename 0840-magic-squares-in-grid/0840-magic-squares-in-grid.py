class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
#         base case return if we can't find a 3*3 matrix
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
#         will be using this variable to count the magic matrix
        count = 0
        flag = True
        
#         function which is going to do all the checking
        def check_magic(a,b,c,d,e,f,g,h,i):                
            if(a+b+c== d+e+f == g + h+ i == a + d +g== b + e+ h == c + f + i== a + e + i == c + e + g == 15 and e == 5):
                return True
            
            return False

        loop = 0
        for i in range(len(grid) -2):
            
            for j in range(len(grid[0]) -2):
     
#                 checking if we don't have any duplicate values
                check_duplicates = set({grid[i][j], grid[i][j+1], grid[i][j+2], 
                      grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], 
                      grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]})
                
        
#                   checking elements of the set whether they are in range 0-9
                for num in check_duplicates:
                    if num > 9:
                        flag = False
                
          
#                  if the above conditions satisfy we send the elements to check_magic function
                if flag and len(check_duplicates) == 9 and check_magic(grid[i][j], grid[i][j+1],    grid[i][j+2], 
                      grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], 
                      grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]): 
                    count += 1
                flag = True
                       
        return count
        