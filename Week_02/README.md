学习笔记
### 本周补了二叉树的基础知识，记录如下。
  * 满二叉树：叶子节点全部在最底层，除了叶子节点之外，每个节点都有左右两个子节点。
  * 完全二叉树： 叶子节点都在最底下两层，最后一层的叶子节点都靠左排列，并且除了最后一层，其他层的节点个数都要达到最大。
  * 如果某棵二叉树是完全二叉树，最节省内存的存储方式是数组。因为数组不需要像链式存储那样，要存储额外的左右子节点的指针。
  * 二叉查找树：树中的任意一个节点，其左子树中的每个节点的值，都要小于该节点的值。而这个节点的右子树节点的值，都要大于该节点的值。