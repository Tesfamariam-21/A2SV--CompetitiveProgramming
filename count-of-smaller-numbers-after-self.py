class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i], i))

        def merge(left_half, right_half):
            ptr1 = ptr2 = 0
            while  ptr1 < len(left_half):
                res[left_half[ptr1][1]] += ptr2

                while ptr2 < len(right_half) and right_half[ptr2][0] < left_half[ptr1][0]:
                    res[left_half[ptr1][1]] += 1
                    ptr2 += 1
                    
                ptr1 +=1  


            ptr1 = ptr2 = 0
            sortedList = []

            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1][0] < right_half[ptr2][0]:
                    sortedList.append(left_half[ptr1])
                    ptr1 += 1
                else:
                    sortedList.append(right_half[ptr2])
                    ptr2 += 1

            if ptr1 < len(left_half):
                sortedList.extend(left_half[ptr1:])
            if ptr2 < len(right_half):
                sortedList.extend(right_half[ptr2:])

            return sortedList



        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid+1, right, arr)

            return merge(left_half, right_half)

        mergeSort(0, len(nums) - 1, arr)
        return res