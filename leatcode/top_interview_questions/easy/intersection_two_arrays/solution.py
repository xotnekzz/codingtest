from collections import Counter

class Solution:
 
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Hash Map"""
        if len(nums1) > len(nums2):
            return self.interserct(nums2, nums1)
        
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        print(result)
        return result


    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Sorting & Two Pointer"""
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            if nums1[i] > nums2[j]:
                j += 1
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
        print(res)


if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    Solution().intersect2(nums1, nums2)
