def dfs(start, goal, moves):
    stack=[start]
    visited={start}
    explored=0

    while stack:
        state=stack.pop()  

        if state==goal:
            return explored

        explored +=1
        blank=state.index(0)

        for move in moves[blank]:
            next_state=list(state)
            next_state[blank], next_state[move]=next_state[move], next_state[blank]
            new_state=tuple(next_state)

            if new_state not in visited:
                visited.add(new_state)
                stack.append(new_state)



def main():
    puzzle=(7,2,4,
            5,0,6,
            8,3,1)

    goal=(0,1,2,
          3,4,5,
          6,7,8)

    moves=[{
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4,6],
            4: [1,3,5,7],
            5: [2,4,8],
            6: [3,7],
            7: [4,6,8],
            8: [5,7]
        },
        {
            0: [1,3],
            1: [2,4,0],
            2: [5,1],
            3: [4,6,0],
            4: [5,7,3,1],
            5: [8,4,2],
            6: [7,3],
            7: [8,6,4],
            8: [7,5]
        },
        {
            0: [3,1],
            1: [4,0,2],
            2: [5,1],
            3: [6,0,4],
            4: [7,3,1,5],
            5: [8,4,2],
            6: [3,7],
            7: [6,4,8],
            8: [7,5]
        },
        {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4,6],
            4: [3,1,5,7],
            5: [4,2,8],
            6: [3,7],
            7: [6,4,8],
            8: [7,5]
        }]

    direction=int(input("What direction should be prioritised? 0:Left 1:Up 2:Right 3:Down \n Number:"))
    no_of_states=dfs(puzzle,goal,moves[direction])
    print("Number of states explored: ",no_of_states)
    

if __name__=='__main__':
    main()