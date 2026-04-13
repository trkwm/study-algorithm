class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n
        self.siz = [1]*n
    
    def find(self, x):
        path = list()
        while self.parent[x]!=-1:
            path.append(x)
            x = self.parent[x]
        for v in path:
            self.parent[v] = x
        return x

    def issame(self, x, y):
        return self.root(x)==self.root(y)
    
    def union(self, x, y):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx == rooty:
            return False
        
        if self.siz[rootx] < self.siz[rooty]:
            rootx, rooty = rooty, rootx
        
        self.parent[rooty] = rootx
        self.siz[rootx] += self.siz[rooty]
        return True
    
    def size(self, x):
        return self.siz[self.root(x)]