from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for num in nums:
            print(num)
        return [[3,4], [44,55]]


s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))