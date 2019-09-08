from pprint import pprint

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
INF = float("inf")

def construct_path(node, prevs):
    path = [node]
    curr = node
    while prevs[curr] != curr:
        path.append(prevs[curr])
        curr = prevs[curr]
    return path

def get_neighbours(graph, node, unvisited):
    return dict([[n[0], n[1]] for n in graph[node] if n[0] in unvisited])

def dijkstra(graph, start, goal):
    visited = []
    unvisited = list(graph.keys())
    curr = start
    goal = goal

    distances = {n: INF for n in list(graph.keys())}
    distances[curr] = 0
    prev_nodes = {n: None for n in list(graph.keys())}
    prev_nodes[curr] = curr

    while goal != curr:
        neighbours = get_neighbours(graph, curr, unvisited)
        # print("NEIGHBOURS: ", neighbours)
        for n in neighbours.keys():
            if distances[curr] + neighbours[n] < distances[n]:
                distances[n] = distances[curr] + neighbours[n]
                prev_nodes[n] = curr
        unvisited.remove(curr)
        visited.append(curr)
        # print("DIST: ", distances)
        curr = min(
            dict(filter(lambda node: node[0] in unvisited, distances.items())),
            key=distances.get
            )
        # print("CURR: ", curr)
        # print("PREV: ", prev_nodes)

    return construct_path(curr, prev_nodes)[::-1], distances[curr]

def main():
    start = A
    goal = G
    graph1 = {A:[[B, 4], [C, 3], [E, 7]],
              B:[[A, 4], [C, 6], [D, 5]],
              C:[[A, 3], [B, 6], [D, 11], [E, 8]],
              D:[[B, 5], [C, 11], [F, 5]],
              E:[[A, 3], [C, 8], [F, 2]],
              F:[[E, 2], [D, 5], [G, 3]],
              G:[[D, 9], [F, 3]],
              }

    graph2 = {A:[[B, 1], [C, 9], [E, 10]],
              B:[[A, 1], [C, 3]],
              C:[[A, 9], [B, 3], [D, 1], [E, 4]],
              D:[[C, 1], [E, 8], [F, 7]],
              E:[[A, 10], [C, 4], [D, 8], [F, 2], [G, 7]],
              F:[[D, 7], [E, 2], [G, 3]],
              G:[[E, 7], [F, 3]],
              }

    pprint(graph1)
    path, min_distance = dijkstra(graph1, start, goal)
    print("Shortest path: ", path)
    print("Min distance: ", min_distance)

    pprint(graph2)
    path, min_distance = dijkstra(graph2, start, goal)
    print("Shortest path: ", path)
    print("Min distance: ", min_distance)

if __name__ == "__main__":
    main()
