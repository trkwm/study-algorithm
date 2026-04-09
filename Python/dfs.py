def dfs(graph, start_vertex):
    explored = [False]*len(graph)
    stack = list()
    stack.append(start_vertex)
    L = list()
    while stack:
        vertex = stack.pop()
        if not explored[vertex-1]:
            explored[vertex-1] = True
            L.append(vertex)
            for nxt_vertex in graph[vertex-1]:
                stack.append(nxt_vertex)
    return L

#===================================================================#
graph = [[2,3],[1,3,4,5],[1,2,5,7,8],[2,5],[2,3,4,6],[5],[3,8],[3,7]]
print(dfs(graph,1))