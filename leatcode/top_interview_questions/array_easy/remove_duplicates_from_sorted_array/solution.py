class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] > nums[j-1]:
                nums[i] = nums[j]
                i += 1


if __name__ == "__main__":
    nums = [0,0,1,2,2,3,3,3,4,4,5,5,5]
    Solution().removeDuplicates(nums)
