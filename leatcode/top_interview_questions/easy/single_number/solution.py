class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {nums[0]}
        for i in range(1, len(nums)):
            if nums[i] in seen:
                seen.remove(nums[i])
            else:
                seen.add(nums[i])
        return seen.pop()

    def singleNumber2(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # 모든 숫자를 XOR 연산 누적
        return result

if __name__ == "__main__":
    nums = [2,2,1]
    print(Solution().singleNumber2(nums))
