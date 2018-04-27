import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.dependencies = set()


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from_nodes = dict()
        for ele in prerequisites:
            if ele[0] not in from_nodes:
                from_nodes[ele[0]] = set()
            from_nodes[ele[0]].add(ele[1])

        to_nodes = dict()
        for ele in prerequisites:
            if ele[1] not in to_nodes:
                to_nodes[ele[1]] = set()
            to_nodes[ele[1]].add(ele[0])

        while set(to_nodes.keys()) != set(from_nodes.keys()):
            sink_nodes = set(to_nodes.keys()) - set(from_nodes.keys())
            from_wheres = set()
            for node in sink_nodes:
                from_wheres |= to_nodes[node]
                del to_nodes[node]
            for node in from_wheres:
                from_nodes[node] = from_nodes[node] - sink_nodes
                if len(from_nodes[node]) == 0:
                    del from_nodes[node]

        return len(from_nodes) <= 1


def main(*args):
    solution = Solution()
    result = solution.canFinish(3, [[1, 0]])
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
