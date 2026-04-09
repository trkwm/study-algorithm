
def bfs(graph, start_vertex):
    discovered = [False]*(len(graph))
    discovered[start_vertex-1] = True
    L = [[start_vertex]]
    T = list()
    depth = 0
    while L[depth]:
        L.append([])
        for vertex in L[depth]:
            for nxt_vertex in graph[vertex-1]:
                if not discovered[nxt_vertex-1]:
                    discovered[nxt_vertex-1] = True
                    T.append((vertex,nxt_vertex))
                    L[depth+1].append(nxt_vertex)
        depth += 1
    return T

#===================================================================#
graph = [[2,3],[1,3,4,5],[1,2,5,7,8],[2,5],[2,3,4,6],[5],[3,8],[3,7]]
print(bfs(graph,1))