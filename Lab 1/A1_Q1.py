def bfs(graph, start, end):
    q=[(start, 0, [start], {start})]  
    results=[]

    while q:
        node, cost, path, visited=q.pop(0)  

        if node==end:
            results.append((path, cost))
            continue

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                q.append((
                    neighbour,
                    cost + weight,
                    path + [neighbour],
                    visited | {neighbour}
                ))

    return results


def dfs(graph, start, end):
    results=[]

    def df_search(node, cost, path, visited):
        if node==end:
            results.append((path[:], cost))
            return

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                df_search(
                    neighbour,
                    cost + weight,
                    path + [neighbour],
                    visited | {neighbour}
                )

    df_search(start, 0, [start], {start})
    return results


def main():
    graph={
    "Syracuse": [("Buffalo",150),("Boston",312),("New York",254),("Philadelphia",253)],
    "Buffalo": [("Syracuse",150),("Detroit",256),("Cleveland",189),("Pittsburgh",215)],
    "Detroit": [("Buffalo",256),("Chicago",283)],
    "Cleveland": [("Buffalo",189),("Chicago",345),("Detroit",169),("Columbus",144),("Pittsburgh",134)],
    "Pittsburgh": [("Buffalo",215),("Cleveland",134),("Columbus",185),("Baltimore",247),("Philadelphia",305)],
    "Columbus": [("Pittsburgh",185),("Indianapolis",176),("Cleveland",144)],
    "Indianapolis": [("Columbus",176),("Chicago",182)],
    "New York": [("Syracuse",254),("Philadelphia",97),("Providence",181),("Boston",215)],
    "Philadelphia": [("New York",97),("Baltimore",101),("Pittsburgh",305),("Syracuse",253)],
    "Baltimore": [("Philadelphia",101),("Pittsburgh",247)],
    "Providence": [("New York",181),("Boston",50)],
    "Boston": [("Syracuse",312),("Providence",50),("Portland",107)],
    "Portland": [("Boston",107)],
    "Chicago": []
    }

    algo=int(input("Enter 1 for BFS, 2 for DFS: "))
    start=input("Enter starting city: ").strip().capitalize()
    end=input("Enter end city: ").strip().capitalize()

    if algo==1:
        bfs_costs=bfs(graph, start, end)
        for path, cost in bfs_costs:
            for city in path:
                print(city, "-", end=" ")
            print(cost)
    else:
        dfs_costs=dfs(graph, start, end)
        for path, cost in dfs_costs:
            for city in path:
                print(city, "-", end=" ")
            print(cost)


if __name__=='__main__':
    main()