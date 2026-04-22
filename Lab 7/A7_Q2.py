import random
e=2.718
iterations=8

def generate_board():
    #queens=[3,7,0,4,6,1,5,2]
    queens=[random.randint(0,7) for i in range(8)]
    return queens

def h(queens):
    attacks=0
    for i in range(8):
        for j in range(i+1,8):
            if queens[i]==queens[j] or (i-queens[i])==(j-queens[j]) or (i+queens[i])==(j+queens[j]):
                #print(f"({queens[i]},{i}) ({queens[j]},{j})")
                attacks+=1
    return attacks


def first_choice(queens):
    state=queens.copy()
    steps=0
    while True:
        attacks=h(queens)
        steps+=1
        flag=0
        for i in range(8):
            state=queens.copy()
            for j in range(15):
                state[i]=random.randint(0,7)
                #print(state)
                #print(h(state))
                if(h(state)<attacks):
                    queens=state.copy()
                    #print(h(state))
                    if h(state)==0:
                        return queens, 0, steps
                    flag=1
                    break
                    #print(neighbour)

            if flag:
                break    
        if h(queens)==attacks:
            return queens, h(queens), steps
        #print(h(queens),attacks,queens,neighbour)


def random_restart(queens):
    state=queens.copy()
    neighbour=state.copy()
    steps=0
    while True:
        attacks=100
        for i in range(8):
            state=queens.copy()
            for j in range(8):
                state[i]=j
                #print(state)
                #print(h(state))
                if(h(state)<attacks):
                    attacks=h(state)
                    neighbour=state.copy()
                    if attacks==0:
                        return neighbour, attacks, steps
                    #print(neighbour)
      
        steps+=1
        if h(queens)<=attacks:
            queens=generate_board()
        #print(h(queens),attacks,queens,neighbour)
        else:
            queens=neighbour.copy()


def schedule(t):
    T0=100
    a=0.9
    return T0*(a**t)

def sim_annealing(queens):
    state=queens.copy()
    steps=0
    for t in range(1000000000):
        T=schedule(t)
        attacks=h(queens)
        if T==0:
            return state,h(state),steps
        state=queens.copy()
        state[random.randint(0,7)]=random.randint(0,7)
        delE=h(state)-attacks
        #print(state)
        #print(h(state))
        if delE<0:
            queens=state.copy()
            steps+=1
            #print(h(state))
            if h(state)==0:
                return queens, 0, steps
                    #print(neighbour)
        else:
            prob=e**(-delE/T)
            if random.random()<=prob:
                steps+=1
                queens=state.copy()

        #print(h(queens),attacks,queens,neighbour)


def main():
    success=0
    avg_steps=0
    for i in range(iterations):
        print(f"Board {i+1}:")
        queens=generate_board()
        ans,attacks,cost=first_choice(queens)
        print(queens,h(queens))
        print(ans,attacks,cost)
        avg_steps+=cost
        if attacks==0:
            success+=1
            print("Solved\n")
        else:
            print("Failed\n")
    avg_steps/=iterations
    print("===== First Choice =====")
    print(f"Success Rate={success/iterations*100}%    Average Steps Taken={avg_steps}\n")

    success=0
    avg_steps=0
    for i in range(iterations):
        print(f"Board {i+1}:")
        queens=generate_board()
        ans,attacks,cost=random_restart(queens)
        print(queens,h(queens))
        print(ans,attacks,cost)
        avg_steps+=cost
        if attacks==0:
            success+=1
            print("Solved\n")
        else:
            print("Failed\n")
    avg_steps/=iterations
    print("===== Random Restart =====")
    print(f"Success Rate={success/iterations*100}%    Average Steps Taken={avg_steps}\n")

    success=0
    avg_steps=0
    for i in range(iterations):
        print(f"Board {i+1}:")
        queens=generate_board()
        ans,attacks,cost=sim_annealing(queens)
        print(queens,h(queens))
        print(ans,attacks,cost)
        avg_steps+=cost
        if attacks==0:
            success+=1
            print("Solved\n")
        else:
            print("Failed\n")
    avg_steps/=iterations
    print("===== Simulated Annealing =====")
    print(f"Success Rate={success/iterations*100}%    Average Steps Taken={avg_steps}\n")

if __name__=="__main__":
    main()