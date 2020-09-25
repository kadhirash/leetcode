class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # initialization
        stack, ans, target = [[0]], [], len(graph)-1
        while stack:
            path = stack.pop()
			# check if the current path we are examinating reaches the N-1 node we desire
			# if the last node of the path is the N-1 node, it is guaranteed that it is a valid
			# path since acyclicity.
            if path[-1] == target:
                ans.append(path)
			# if the last node of the path is not the N-1 node,
            else:
				# we need to check first if it reaches a deadend, in other words, if the
				# node where the current path stops at has no outreaching edge.
				# if no, then this is an invalid path and we discard it. 
				# if not graph[path[-1]]:
			    #      continue
				# if yes, we push all new paths on stack for further examinations.
                if graph[path[-1]]:
                    for i in graph[path[-1]]:
                        stack.append(path + [i])
        
        return ans