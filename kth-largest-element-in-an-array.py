class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *=-1

        heapq.heapify(nums)

        for _ in range(k):
            ans = heapq.heappop(nums)

        return -1*ans
        # def partition(left, right):
        #     if right - left <= 0:
        #         if left == len(nums) - k:
        #             return nums[left]
        #         return

        #     pivot = right
        #     leftmost = left

        #     while left < right:
        #         if nums[left] < nums[pivot]:
        #             left +=1

        #         else:
        #             if nums[right] >= nums[pivot]:
        #                 right -=1
        #             else:
        #                 nums[left], nums[right] = nums[right], nums[left]
                

        #     nums[left], nums[pivot] = nums[pivot], nums[left]

        #     if left == len(nums) - k:
        #         return nums[left]

            
        #     l = partition(leftmost, left - 1)
        #     r = partition(left + 1, pivot)

        #     if l != None:
        #         return l

        #     return r

        # return partition(0, len(nums) - 1)