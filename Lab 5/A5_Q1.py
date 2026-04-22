class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state=state
        self.parent=parent
        self.depth=depth


class Problem:
    def __init__(self):
        self.initial=(3, 3, 0) 
        self.goal=(0, 0, 1)

    def is_goal(self, state):
        return state==self.goal


def is_valid(girl_left, boy_left):
    girl_right=3-girl_left
    boy_right=3-boy_left

    if not (0<=girl_left<=3 and 0<=boy_left<=3):
        return False

    if girl_left!=0 and boy_left>girl_left:
        return False

    if girl_right!=0 and boy_right>girl_right:
        return False

    return True


def expand(node):
    girl_left, boy_left, boat=node.state
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    children=[]

    for girl, boy in moves:
        if boat==0:
            new_state=(girl_left-girl, boy_left-boy, 1)
        else:
            new_state=(girl_left+girl, boy_left+boy, 0)

        if is_valid(new_state[0], new_state[1]):
            children.append(Node(new_state, node, node.depth+1))

    return children


def is_cycle(node):
    current=node.state
    node=node.parent
    while node:
        if current==node.state:
            return True
        node=node.parent
    return False


def DLS(problem,l):
    frontier=[]
    frontier.append(Node(problem.initial))
    result="FAILURE"
    global node_count
    node_count=0
    while frontier:
        node=frontier.pop() 
        if problem.is_goal(node.state):
            return node
        
        if node.depth>l:
            result="CUTOFF"

        elif not is_cycle(node):
            node_count+=1
            for child in expand(node):
                frontier.append(child)
    return result


def IDPS(problem):
    depth=0
    global total_nodes
    total_nodes=0
    while True:
        result=DLS(problem, depth)
        total_nodes+=node_count
        if result!="CUTOFF":
            return result
        depth+=1


def main():
    problem=Problem()

    print("Depth Limited Search (limit=3):-")
    dls_result=DLS(problem, 3)
    print(dls_result)
    print("Nodes Explored:",node_count)

    print("\nIterative Deepening Search:-")
    ids_result=IDPS(problem)

    if isinstance(ids_result, Node):
        path=[]
        while ids_result:
            path.append(ids_result.state)
            ids_result=ids_result.parent
        path.reverse()
        print("Succesful path [Node=(girls at left side, boys at left side, boat position)]:")
        print(path)
    else:
        print(ids_result)

    print("Total Nodes Explored:", total_nodes)


if __name__=='__main__':
    main()