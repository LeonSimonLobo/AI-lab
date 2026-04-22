matrix=[
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1], 
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

class Node:
    def __init__(self, state, action, parent=None, cost=0, goals=[1, 1, 1, 1]):
        self.state=state
        self.parent=parent
        self.action=action
        self.cost=cost
        self.goals=goals


def h(node):
    x=node.state[0]
    y=node.state[1]
    heuristic=[]
    heuristic.append((abs(x-1)+abs(y-4))*node.goals[0])
    heuristic.append((abs(x-2)+abs(y-1))*node.goals[1])
    heuristic.append((abs(x-4)+abs(y-0))*node.goals[2])
    heuristic.append((abs(x-4)+abs(y-4))*node.goals[3])
    min_h=float('inf')
    for h in heuristic:
        if (h==0 and node.goals[heuristic.index(h)]==1) or h!=0:
            min_h=min(h,min_h)
    return min_h

def g(node):
    return node.cost


def f(node):
    cost=g(node)
    heuristic=h(node)
    return (cost+heuristic)



class pq:
    def __init__(self):
        self.queue=[]

    def push(self, node):
        self.queue.append(node)

    def pop(self):
        best=0
        for i in range(1, len(self.queue)):
            if f(self.queue[i])<f(self.queue[best]):
                best=i
        return self.queue.pop(best)

    def is_empty(self):
        return len(self.queue)==0


def expand(problem, node):
    s=node.state
    children=[]

    moves=[(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        s0=(s[0]+dx, s[1]+dy)

        if 0<=s0[0]<len(problem) and 0<=s0[1]<len(problem[0]):
            
            if problem[s0[0]][s0[1]]!=1:
                cost=node.cost+1
                child=Node(s0, (dx,dy), node, cost, node.goals.copy())
                children.append(child)

    return children


def A_star(problem, start, rewards):

    node=Node(start, None, None, 0)

    frontier=pq()
    frontier.push(node)
    reached={}
    reached[(start, tuple(node.goals))]=0
    explored_count=0

    while frontier.queue:                 

        node=frontier.pop()
        explored_count+=1
        
        if node.state in rewards:
            node.goals[rewards.index(node.state)]=0
            
        if node.parent is not None:
            print(node.parent.state, "->", node.state, ",",g(node), h(node), f(node), node.goals)

        if all(g==0 for g in node.goals):
            return node, explored_count
        
        for child in expand(problem, node):
            s=(child.state,tuple(child.goals))
            if s not in reached or child.cost<reached[s]:
                reached[s]=child.cost
                frontier.push(child)

    return None, explored_count

def print_path(node):
    path=[]
    while node:
        path.append(f"({node.state[0]},{node.state[1]})")
        node=node.parent
    path.reverse()
    print(" → ".join(path))

def main():
    goals=[(1, 4), (2, 1), (4, 0), (4, 4)]
    ans,count=A_star(matrix, (0, 0), goals)
    if ans:
        print("\nPath to collect all rewards:")
        print_path(ans)
    print("Nodes explored:", count)

if __name__=="__main__":
    main()