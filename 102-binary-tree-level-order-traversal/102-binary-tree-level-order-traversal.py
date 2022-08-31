# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l=[]
        if root==None:
            return l
        else:
            j=0
            l.append([root.val])
            q=[root]
            while q!=[]:
                m=[]
                t=q.copy()
                #print(t)
                for i in range(len(t)):
                    if t[i]!=None:
                        if t[i].left!=None:
                            q.append(t[i].left)
                            m.append(t[i].left.val)
                        if t[i].right!=None:
                            q.append(t[i].right)
                            m.append(t[i].right.val)
                    q.pop(0)
                if m!=[]:
                    l.append(m)
                j+=1
            return l
                    
                    
                    
                    
        