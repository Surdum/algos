from base import AlgoBase
from collections import defaultdict


class Demoucron(AlgoBase):
    def run(self, graph):
        stack = []
        color = defaultdict(int)

        def _sort() -> list:
            def dfs(v: str) -> bool:
                if color[v] == 1:
                    return True
                if color[v] == 2:
                    return False
                color[v] = 1
                for i in range(len(graph[v]) - 1):
                    if dfs(graph[v][i]):
                        return True
                stack.append(v)
                color[v] = 2
                return False

            for key in graph.keys():
                if dfs(key):
                    print("Cycle found")
                    return []
            stack.reverse()

            return stack

        return _sort()


if __name__ == '__main__':
    dem = Demoucron()
    graph = {'c': ['d'], 'd': ['a', 'b', 'e', 'f'], 'a': ['b'], 'b': ['e'], 'e': ['g'], 'g': ['h'], 'f': ['e', 'h']}
    print(dem.run(graph))
