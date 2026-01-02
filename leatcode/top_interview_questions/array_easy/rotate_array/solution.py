class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums


if __name__ == "__main__":
    nums = [1,2]
    print(Solution().rotate(nums, 7))
