grid=[
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
explored=0
def utility(state):
    if (state[0][0]==state[1][1] and state[1][1]==state[2][2]) or (state[0][2]==state[1][1] and state[1][1]==state[2][0]):
            if state[1][1]=="X":
                return 1
            elif state[1][1]=="O":
                return -1
            else:
                return 0
    for i in range(3):
        if (state[i][0]==state[i][1] and state[i][2]==state[i][1]):
            if state[i][0]=="X":
                return 1
            elif state[i][0]=="O":
                return -1
            else:
                return 0
        if (state[0][i]==state[1][i] and state[1][i]==state[2][i]):
            if state[0][i]=="X":
                return 1
            elif state[0][i]=="O":
                return -1
            else:
                return 0
    return 0


def is_terminal(state):
    if utility(state)==0:
        for i in range(3):
            for j in range(3):
                if state[i][j]=="-":
                    return 0
    return 1


def to_move(state):
    x_moves=0
    o_moves=0
    for i in range(3):
        for j in range(3):
            if state[i][j]=="X":
                x_moves+=1
            elif state[i][j]=="O":
                o_moves+=1
    if x_moves>o_moves:
        return 0
    else:
        return 1
    

def actions(state, player):
    new_states=[]
    if player:
        for i in range(3):
            for j in range(3):
                if state[i][j]=="-":
                    temp=[row[:] for row in state]
                    temp[i][j]="X"
                    new_states.append(temp)
    else:
        for i in range(3):
            for j in range(3):
                if state[i][j]=="-":
                    temp=[row[:] for row in state]
                    temp[i][j]="O"
                    new_states.append(temp)
    return new_states



def minimax_search(state):
    player=to_move(state)
    value, move=max_value(state, player, 0)
    return move


def max_value(state, player, depth):
    if depth<4:
        print("\t"*depth,"min_move", state)
    global explored
    explored+=1
    if is_terminal(state):
        return utility(state), None
    v=-10000000000
    move=None
    for a in actions(state, player):
        v2, a2=min_value(a, player^1, depth+1)
        if v2>v:
            v, move=v2, a
    return v, move


def min_value(state, player, depth):
    if depth<4:
        print("\t"*depth,"max_move", state)
    global explored
    explored+=1
    if is_terminal(state):
        return utility(state), None
    v=10000000000
    move=None
    for a in actions(state, player):
        v2, a2=max_value(a, player^1, depth+1)
        if v2<v:
            v, move=v2, a
    return v, move


def main():
    move=minimax_search(grid)
    print("Optimal first move is:", move)
    print("Total nodes explored:",explored)

if __name__=='__main__':
    main()