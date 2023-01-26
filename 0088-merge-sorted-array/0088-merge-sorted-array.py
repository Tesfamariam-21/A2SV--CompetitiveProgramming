class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        ptr1, ptr2 = m-1, n-1
        zp = len(nums1) - 1
                
        while ptr2 >= 0:
            if ptr1 >= 0:
                if nums2[ptr2] >= nums1[ptr1]:
                    nums1[zp] = nums2[ptr2]
                    ptr2 -= 1
                    zp -= 1
                else:
                    nums1[zp] = nums1[ptr1]
                    # nums1[ptr1] = nums2[ptr2]
                    ptr1 -= 1
                    zp -= 1
            else:
                nums1[ptr2] = nums2[ptr2]
                ptr2-=1