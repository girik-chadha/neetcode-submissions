class Solution:
    def findMin(self, nums: List[int]) -> int:
        min1 = float("inf")

        L,R = 0, len(nums) - 1
        for i in nums:
            min1 = min(min1, i)
        return min1

        