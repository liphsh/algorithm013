#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# @lc code=start
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
           return None
        root = TreeNode(preorder[0])
        mid_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])
        root.right = self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
        return root

# @lc code=end

