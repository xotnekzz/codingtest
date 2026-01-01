class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums_cnt = len(set(nums))
        if unique_nums_cnt != len(nums):
            return True
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))
