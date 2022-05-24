class UF:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if rootX <= rootY:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]


class Solution:
    def numIslands2(self, m, n, positions):
        uf = UF(m * n)
        res = []
        count = 0
        visited = set()

        for x, y in positions:
            if (x, y) in visited:
                res.append(count)
                continue
            count += 1
            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx == m or yy < 0 or yy == n:
                    continue
                # skip water
                if (xx, yy) not in visited:
                    continue
                component1 = uf.find(x * n + y)
                component2 = uf.find(xx * n + yy)
                if component1 != component2:
                    uf.union(component1, component2)
                    count -= 1
            res.append(count)

        return res