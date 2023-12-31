from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #indegree identification 
        indegree_hashmap={}

        for courses in range(0,numCourses):
            indegree_hashmap[courses]=0
        print(indegree_hashmap)
        for prerequisite in prerequisites:
            target,source=prerequisite
            indegree_hashmap[target]+=1
        print(indegree_hashmap)

        adjacency_list=defaultdict(list)

        for prerequisite in prerequisites:
            target,source=prerequisite
            adjacency_list[source].append(target)
        print(adjacency_list)

        #start with the element which has a zero indegree and put that element inside a queue
        #put the element with zero indegree in the queue
        queue=[]
        for k,v in indegree_hashmap.items():
            queue.append(k) if v==0 else "rebecca"
        print(queue)
        ans=[]
        while queue:

            pop_node=queue.pop(0)
            ans.append(pop_node)
            childs=adjacency_list[pop_node]
            for child in childs:
                indegree_hashmap[child]-=1
                if indegree_hashmap[child]==0:
                    queue.append(child)
        print(ans)
        return len(ans) == numCourses

"""
used indegree , adj lists concept to do traversal in the graph and then used BFS (queue) 

"""
