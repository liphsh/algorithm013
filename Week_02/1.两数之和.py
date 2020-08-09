#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        dict_buffer = {}
        for i in range(len(nums)):
            if nums[i] in dict_buffer:
                return(dict_buffer[nums[i]], i)
            else:
                dict_buffer[target - nums[i]] = i

         
# @lc code=end
