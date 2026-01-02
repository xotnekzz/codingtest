class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            new = nums[i+1:]
            if diff in new:
               return [i, new.index(diff)+i+1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
               return [i, seen[diff]]
            seen[nums[i]] = i
             


if __name__ == "__main__":
    nums = [1,3,11,15]
    target = 26
    print(Solution().twoSum(nums, target))
