"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldtoNewHashMap={}

        def dfs(node):
            if node  in oldtoNewHashMap :
                # node is in the hashmap means we already made a clone of it 
                return oldtoNewHashMap[node]

            copy=Node(node.val)
            #add the copy to the hashmap
            oldtoNewHashMap[node]=copy

            #iterate through the neighbours of the original node
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None


"""
Instantiation of a New Node: The Node class represents a node in a graph. When Node(node.val) is called, it creates a new instance of the Node class. This new node is a clone of the current node being processed in the depth-first search (DFS) algorithm. The node.val is passed as an argument to the Node constructor, ensuring that the new node (copy) has the same value as the original node (node).
"""

        
