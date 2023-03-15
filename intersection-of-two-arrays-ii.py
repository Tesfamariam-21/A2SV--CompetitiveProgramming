class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # for the follow up in 3
        if len(nums2) > len(nums1):
            return self.intersect(nums2, nums1)
        c = Counter(nums1)
        ans = []

        for num in nums2:
            if num in c and c[num] > 0:
                ans.append(num)
                c[num] -=1

        return ans

        # nums1 = sorted(nums1)
        # nums2 = sorted(nums2)

        # ptr1 = ptr2 = 0
        # ans = []

        # while ptr1 < len(nums1) and ptr2 < len(nums2):
        #     if nums1[ptr1] > nums2[ptr2]:
        #         ptr2 +=1
        #     elif nums1[ptr1] < nums2[ptr2]:
        #         ptr1 +=1
        #     else:
        #         ans.append(nums1[ptr1])
        #         ptr1 +=1
        #         ptr2 +=1

        # return ans