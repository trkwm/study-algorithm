from heap import MinHeap

def dijkstra(graph, start_vertex):
    checked = [False]*len(graph)
    dist = [float("inf")]*len(graph)
    Minheapq = MinHeap(10**5)
    Minheapq.Insert((0,start_vertex))
    while Minheapq.queue_size>0:
        now_dist, now_vertex = Minheapq.ExtractMin()
        if checked[now_vertex-1]:
            continue
        checked[now_vertex-1] = True
        dist[now_vertex-1] = now_dist
        for nxt_vertex, weight in graph[now_vertex-1]:
            if checked[nxt_vertex-1]:
                continue
            if nxt_dist < dist[nxt_vertex-1]:
                nxt_dist = now_dist+weight
                Minheapq.Insert((nxt_dist,nxt_vertex))
    return dist

N,M,S = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a-1].append((b,c))
    graph[b-1].append((a,c))
print(dijkstra(graph,S)) 