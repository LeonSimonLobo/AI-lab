import random
iterations=50

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


def steepest_ascent(queens):
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
            return queens, h(queens), steps
        #print(h(queens),attacks,queens,neighbour)
        queens=neighbour.copy()



def main():
    success=0
    avg_steps=0
    for i in range(iterations):
        print(f"Board {i+1}:")
        queens=generate_board()
        ans,attacks,cost=steepest_ascent(queens)
        print(queens,h(queens))
        print(ans,attacks,cost)
        avg_steps+=cost
        if attacks==0:
            success+=1
            print("Solved\n")
        else:
            print("Failed\n")
    avg_steps/=iterations
    print("===== Steepest Ascent =====")
    print(f"Success Rate={success/iterations*100}%    Average Steps Taken={avg_steps}\n")

if __name__=="__main__":
    main()