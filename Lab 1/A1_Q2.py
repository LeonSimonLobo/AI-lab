from collections import deque

def bfs_tree(graph, start):
    queue = deque([start])
    visited = {start}

    parent = {start: None}

    while queue:
        node = queue.popleft()

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    return parent

def dfs_tree(graph, start):
    visited = set()
    parent = {start: None}

    def dfs(node):
        visited.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                parent[neighbour] = node
                dfs(neighbour)

    dfs(start)
    return parent


def get_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]



def main():
    graph = {
        "Raj": ["Sunil", "Neha_1"],
        "Sunil": ["Raj", "Akash", "Sneha", "Maya"],
        "Akash": ["Sunil", "Priya"],
        "Priya": ["Raj", "Akash", "Aarav"],
        "Neha_1": ["Raj", "Akash", "Sneha", "Aarav"],
        "Sneha": ["Sunil", "Rahul", "Neha_1"],
        "Maya": ["Sunil", "Rahul", "Arjun_1"],
        "Rahul": ["Sneha", "Maya", "Pooja", "Arjun_2", "Neha_2", "Neha_1"],
        "Arjun_1": ["Maya", "Pooja"],
        "Pooja": ["Arjun_1", "Rahul", "Arjun_2"],
        "Arjun_2": ["Rahul", "Aarav", "Neha_2"],
        "Neha_2": ["Rahul", "Aarav", "Arjun_2", "Neha_1", "Priya"],
        "Aarav": ["Neha_1", "Neha_2", "Arjun_2"]
    }
    algo=int(input("Enter 1 for BFS, 2 for DFS:"))
    start=input("Enter start node:").strip().capitalize()
    if algo==1:
        parent = bfs_tree(graph, start)
        # Find all nodes that are parents
        parents = set(p for p in parent.values() if p is not None)

        # Leaf nodes = nodes that never act as a parent
        leaf_nodes = [node for node in parent if node not in parents]
        for leaf in leaf_nodes:
            path = get_path(parent,leaf)
            print(" -> ".join(path))
    else:
        parent = dfs_tree(graph, start)
        # Find all nodes that are parents
        parents = set(p for p in parent.values() if p is not None)

        # Leaf nodes = nodes that never act as a parent
        leaf_nodes = [node for node in parent if node not in parents]
        for leaf in leaf_nodes:
            path = get_path(parent,leaf)
            print(" -> ".join(path))


    

if __name__=='__main__':
    main()
