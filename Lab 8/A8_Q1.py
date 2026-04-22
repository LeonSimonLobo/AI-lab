import random
        #0    1   2   3   4   5   6   7
graph=[ [0,  10, 15, 20, 25,  30, 35, 40],  # City 0 
        [12,  0,  35, 15, 20, 25, 30, 45],  # City 1 
        [25, 30,  0,  10, 40, 20, 15, 35],  # City 2 
        [18, 25, 12,  0,  15, 30, 20, 10],  # City 3 
        [22, 18, 28, 20,  0,  15, 25, 30],  # City 4 
        [35, 22, 18, 28, 12,  0,  40, 20],  # City 5 
        [30, 35, 22, 18, 28, 32,  0,  15],  # City 6 
        [40, 28, 35, 22, 18, 25, 12,  0 ]]  # City 7 


def local_beam(graph,k):
    states=[]
    for i in range(k):
        temp_state=random.randint(0,7)
        temp_reached=[0 for i in range(8)]
        temp_reached[temp_state]=1
        states.append([temp_state,temp_reached,0]) #city, reached, cost
    travelled=1
    print("Initial Beam:", states)
    while travelled!=8:
        next_state=[]
        for state in states:
            curr=state[0]
            
            cost=state[2]
            for i in range(8):
                if state[1][i]==0:
                    #print(i,state[0])
                    visited=state[1].copy()
                    visited[i]=travelled+1
                    next_state.append([cost+graph[curr][i],i,visited])

        next_state.sort()
        print("Beam:", states)
        travelled+=1
        for i in range(k):
            states[i][0]=next_state[i][1]
            states[i][2]=next_state[i][0]
            states[i][1]=next_state[i][2].copy()
            if travelled==8:
                final_state=initial_state=0
                for j in range(len(states[i][1])):
                    if state==1:
                        initial_state=j
                    elif state==0:
                        states[i][1][j]=8
                        final_state=j
                return states[i][2]+graph[final_state][initial_state],states[i][1]
        #print(states[i],end=",")
        #print(states,travelled)
        #print("\n")
    return
        

def main():
    k=5
    print("For k =",k)
    cost,travelled=local_beam(graph,k)
    print("\nCost of path =",cost)
    print("Path:-")
    for i in range(8):
        for j in range(8):
            if travelled[j]==i+1:
                print("->",j,end=" ")
                break
        

if __name__=='__main__':
    main()