import sys
from collections import defaultdict, deque
from typing import Dict


class Solution:
    def topo_sort(self, vertices, edges):
        result = []
        q = deque()
        # init in_degree
        in_graph = dict()
        for v in vertices:
            in_graph[v] = set()
            for edge in edges:
                if edge[1] == v:
                    in_graph[v].add(edge[0])

        for v, from_v_set in in_graph.items():
            if len(from_v_set) == 0:
                q.append(v)
        for v in q:
            del in_graph[v]
        while len(q) > 0:
            tmp_v = q.popleft()
            result.append(tmp_v)
            v_has_zero_in_degree = []
            for v, from_v_set in in_graph.items():
                if tmp_v in from_v_set:
                    from_v_set.remove(tmp_v)
                if len(from_v_set) == 0:
                    q.append(v)
                    v_has_zero_in_degree.append(v)
            for v in v_has_zero_in_degree:
                del in_graph[v]
        if len(in_graph) > 0:
            return None
        return result


def main(*args):
    g = defaultdict(list)
    v = [0, 1, 2, 3, 4, 5]
    e = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    solution = Solution()
    result = solution.topo_sort(v, e)
    print(result)


if __name__ == '__main__':
    main(*sys.argv[1:])
