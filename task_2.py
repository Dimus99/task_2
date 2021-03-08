def bfs(v, graph, used):
    color = colors[v]
    used[v] = True
    for next_v in graph[v]:
        if colors[next_v] == color:
            return False
        elif colors[next_v] == -1:
            colors[next_v] = 1 - color  # ну можно изменить, но и ладно
    return [bfs(next_v, graph, used) for next_v in graph[v] if not used[next_v]].count(False) == 0


with open("in.txt") as file:
    n = int(file.readline())
    lists = [[int(v)-1 for v in file.readline().split()[:-1]] for line in range(n)]
used = [False for v in range(n)]
colors = [-1 for v in range(n)]
colors[0] = 0
with open("out.txt", "w") as file:
    if bfs(0, lists, used) and not colors.count(-1):
        file.write("Y\n")
        file.write(" ".join([str(v + 1) for v in range(n) if not colors[v]]) + " 0\n")  # 0 всегда тут
        file.write(" ".join([str(v + 1) for v in range(n) if colors[v]]) + " 0")
    else:
        file.write("N")



