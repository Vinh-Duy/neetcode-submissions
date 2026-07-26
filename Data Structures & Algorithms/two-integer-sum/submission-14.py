class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ham = {}

        for i, n in enumerate(nums):
            ham[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in ham and ham[diff] != i:
                return [i, ham[diff]]
        return []