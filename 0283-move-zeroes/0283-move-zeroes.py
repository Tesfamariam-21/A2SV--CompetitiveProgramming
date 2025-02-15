class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read =  write = 0 

        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write],  nums[read]
                write +=1
            
            read +=1

        return nums
        # ptr1, ptr2 = 0, 0
        
        # while ptr2 < len(nums):
        #     if nums[ptr1] != 0:
        #         ptr1 +=1 
        #         ptr2 +=1
        #     elif nums[ptr2] == 0:
        #         ptr2 +=1
        #     else:
        #         nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
        
        # ptr = 0

        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[ptr] = nums[i]
        #         ptr +=1
        
        # nums[ptr:] = [0] * (len(nums) - ptr)

        # left = 0

        # for i in range(len(nums)):
        #     if nums[i]:
        #         nums[i], nums[left] = nums[left], nums[i]
        #         left +=1




        # read = 0
        # write = 0

        # while read < len(nums):
        #     if nums[write] != 0:
        #         read +=1
        #         write +=1
        #     elif nums[read] != 0:
        #         nums[write], nums[read] = nums[read], nums[write]
        #     else:
        #         read +=1

        
        # # for i in range(len(nums)):
        # #     if nums[i] == 0:
        # #         nums.append(nums.pop(i))

        # # return nums