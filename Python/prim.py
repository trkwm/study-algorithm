from heap import MinHeap

def Prim(graph, start_vertex):
    MST_sum = 0
    checked = [False]*(len(graph))
    Minheapq = MinHeap(10**5)
    Minheapq.Insert((0,start_vertex,-1))
    Tree = list()
    while Minheapq.queue_size>0:
        now_weight,now_vertex,pre_vertex = Minheapq.ExtractMin()
        if checked[now_vertex-1]:
            continue
        checked[now_vertex-1] = True
        if pre_vertex!=-1:
            MST_sum += now_weight
        if pre_vertex!=-1:
            Tree.append((now_vertex,pre_vertex))
        for nxt_vertex, weight in graph[now_vertex-1]:
            if checked[nxt_vertex-1]:
                continue
            Minheapq.Insert((weight,nxt_vertex,now_vertex))
    return MST_sum, Tree

N,M,S = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a-1].append((b,c))
    graph[b-1].append((a,c))
print(Prim(graph, S))