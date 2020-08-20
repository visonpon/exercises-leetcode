class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        rl=[]
        queue=[(0,root)]
        while len(queue):
            num,node=queue.pop()
            print(num,node.val)
            if num==len(rl):
                rl.append([])
            rl[num].append(node.val)
            if node.left:
                queue.insert(0,(num+1,node.left))
            if node.right:
                queue.insert(0,(num+1,node.right))
        return rl
        
        
        
        
   # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
