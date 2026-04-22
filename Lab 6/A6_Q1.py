cities=[
    "Syracuse", "Buffalo", "Detroit", "Cleveland", "Pittsburgh", 
    "Columbus", "Indianapolis", "New York", "Philadelphia", 
    "Baltimore", "Providence", "Boston", "Portland", "Chicago"
]


graph=[
#  Sy  Bu  De  Cl  Pi  Co  In  NY  Ph  Ba  Pr  Bo  Po  Ch
 [ 0, 150, 0, 0, 0, 0, 0, 254, 253, 0, 0, 312, 0, 0],  # Syracuse
 [150, 0, 256, 189, 215, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Buffalo
 [ 0, 256, 0, 169, 0, 0, 0, 0, 0, 0, 0, 0, 0, 283],  # Detroit
 [ 0, 189, 169, 0, 134, 144, 0, 0, 0, 0, 0, 0, 0, 345],  # Cleveland
 [ 0, 215, 0, 134, 0, 185, 0, 0, 305, 247, 0, 0, 0, 0],  # Pittsburgh
 [ 0, 0, 0, 144, 185, 0, 176, 0, 0, 0, 0, 0, 0, 0],  # Columbus
 [ 0, 0, 0, 0, 0, 176, 0, 0, 0, 0, 0, 0, 0, 182],  # Indianapolis
 [254, 0, 0, 0, 0, 0, 0, 0, 97, 0, 181, 215, 0, 0],  # New York
 [253, 0, 0, 0, 305, 0, 0, 97, 0, 101, 0, 0, 0, 0],  # Philadelphia
 [ 0, 0, 0, 0, 247, 0, 0, 0, 101, 0, 0, 0, 0, 0],  # Baltimore
 [ 0, 0, 0, 0, 0, 0, 0, 181, 0, 0, 0, 50, 0, 0],  # Providence
 [312, 0, 0, 0, 0, 0, 0, 215, 0, 0, 50, 0, 107, 0],  # Boston
 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 0],  # Portland
 [ 0, 0, 283, 345, 0, 0, 182, 0, 0, 0, 0, 0, 0, 0]   # Chicago
]


class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state=state
        self.parent=parent
        self.cost=cost

def h(node):
    heuristic=(260, 400, 610, 550, 470, 640, 780, 215, 270, 360, 50, 0, 107, 860)
    return heuristic[node.state]


def g(node):
    return node.cost


def f(node):
    return h(node)+g(node)


class pq:
    def __init__(self):
        self.queue=[]

    def push(self, node):
        self.queue.append(node)

    def pop(self,f):
        best=0
        for i in range(1, len(self.queue)):
            if f(self.queue[i])<f(self.queue[best]):
                best=i
        return self.queue.pop(best)

    def is_empty(self):
        return len(self.queue)==0


def expand(node):
    children=[]
    for j in range(len(cities)):
        if graph[node.state][j]!=0:
            child=Node(
                j, 
                node, 
                node.cost+graph[node.state][j]
            )
            children.append(child)
    return children


def best_first_search(start, dest, f):
    start_node=Node(start)
    frontier=pq()
    frontier.push(start_node)
    reached=[None]*len(cities)
    reached[start]=start_node  
    global count_node
    count_node=0

    while not frontier.is_empty():
        node=frontier.pop(f)
        count_node+=1
        if node.parent is not None:
            print(f"({cities[node.parent.state]}->{cities[node.state]}, {node.cost})",end="")
        else:
            print(f"(None->{cities[node.state]}, {node.cost})",end="")

        if node.state==dest:
            return node
        
        print("-->",end="")
        for child in expand(node):
            s=child.state
            if reached[s] is None or child.cost<reached[s].cost:
                reached[s]=child
                frontier.push(child)

    return None


def greedy_bfs(start, dest):
    return best_first_search(start, dest, h)

def A_star(start, dest):
    return best_first_search(start, dest, f)


def print_path(node):
    path=[]
    while node:
        path.append(cities[node.state])
        node=node.parent
    path.reverse()
    print(" → ".join(path))


def main():
    start=cities.index("Chicago")
    dest=cities.index("Boston")
    print("Greedy Best First Search:-")
    result=greedy_bfs(start, dest)
    
    if result:
        print("\nPath found:")
        print_path(result)
        print("Minimmum path cost:", result.cost)
        print("Nodes explored:",count_node)
    else:
        print("No path found")

    print("A* search:-")
    result=A_star(start, dest)

    if result:
        print("\nPath found:")
        print_path(result)
        print("Minimmum path cost:", result.cost)
        print("Nodes explored:",count_node)
    else:
        print("No path found")



if __name__=='__main__':
    main()