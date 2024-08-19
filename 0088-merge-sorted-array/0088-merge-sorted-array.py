class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1, ptr2, ptr3 = m-1, n-1, len(nums1)-1

        while ptr3 >= 0:
            if ptr2 >= 0 and ptr1 >=0:            
                if nums1[ptr1] < nums2[ptr2]:
                    nums1[ptr3] = nums2[ptr2]
                    ptr2 -=1
                    ptr3 -=1
                else:
                    nums1[ptr3] = nums1[ptr1]
                    ptr1 -=1
                    ptr3 -=1
            else:
                if ptr2 < 0:
                    nums1[0:ptr3+1] = nums1[0:ptr1+1]
                    break
                else:
                    nums1[0:ptr3+1] = nums2[0:ptr2+1]
                    break
        
        return nums1

        # nums1[m:] = nums2
        # return nums1.sort()