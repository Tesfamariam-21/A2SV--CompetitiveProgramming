class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        find numbers less than the num using brute force 
        or 
        use sort to optimize it
        '''
        n = count = len(nums)
        sorted_nums = [0] * (max(nums) + 1)
        output = [0] * n

        for num in nums:
            sorted_nums[num] +=1
        

        for i in range(n):
            output[i] = sum(sorted_nums[:nums[i]])

        
        # for i in range(len(sorted_nums) - 1, -1, -1):
        #     count -= sorted_nums[i]
        #     print(count)
        #     print(sorted_nums[i], count, i)

        #     for j in range(n):
        #         if nums[j] == i:
        #             output[j] = count
        
        return output

            
            



        # output = [0] * len(nums)
        
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if j == i: continue
                
        #         if nums[i] > nums[j]:
        #             count +=1

        #     output[i] = count

        # return output
