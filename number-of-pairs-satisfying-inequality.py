class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        count = 0

        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])

        def merge(left_half, right_half):
            nonlocal count
            ptr1 = len(left_half) - 1
            ptr2 = len(right_half) - 1

            while  ptr1 >= 0:
                count += (len(right_half) - ptr2 -1)

                while left_half[ptr1] - diff <= right_half[ptr2] and ptr2 >=0:
                    count +=1
                    ptr2 -= 1
                ptr1 -=1                    

            ptr1 = ptr2 = 0
            sortedList = []
            while ptr1 < len(left_half) and ptr2 < len(right_half):
                if left_half[ptr1] < right_half[ptr2]:
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

        mergeSort(0, len(arr) - 1, arr)
        return count