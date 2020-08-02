#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #暴力法：两次遍历，一层i遍历i, 二层j遍历找target-i, 如果找到，则返回index(i), index(j)
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i] :
                    return i, j

         
# @lc code=end
