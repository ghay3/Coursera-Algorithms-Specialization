from collections import deque


def connected_component(graph):
    visited = {v: False for v in graph.keys()}
    belong_to, cnt = {}, 0
    for v in graph.keys():
        if not visited[v]:
            cnt += 1

            visited[v] = True
            belong_to[v] = cnt
            queue = deque([v])
            while queue:
                u = queue.popleft()
                for w in graph[u]:
                    if not visited[w]:
                        visited[w] = True
                        belong_to[w] = cnt
                        queue.append(w)
    return belong_to, cnt


if __name__ == '__main__':
    # http://cn.bing.com/images/search?view=detailV2&ccid=nMllSUI6&id=18D94DA824409E65CDB1FDF115CF759A50E421D7&thid=OIP.nMllSUI6iC8f-ey5cGHr-wEQCX&q=connected+components&simid=608033831760691741&selectedIndex=3&ajaxhist=0
    g = {
        1: [2],
        2: [1, 3, 4],
        3: [2],
        4: [5],
        5: [6],
        6: [],
        7: [8],
        8: [7, 9],
        9: [8],
    }
    belong_to, cnt = connected_component(g)
    print(belong_to)
    print(cnt)