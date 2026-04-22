import random

seed=int(input("Enter a random number for initial state: "))
random.seed(seed)

choice=['Left', 'Right']
state=['Unclean', 'Clean']

def main():
    rule_table={
        ('A', 'Unclean'): 'Cleanse',
        ('A', 'Clean'): 'Right',
        ('B', 'Unclean'): 'Cleanse',
        ('B', 'Clean'): random.choice(choice),
        ('C', 'Unclean'): 'Cleanse',
        ('C', 'Clean'): 'Left'
    }

    environment={
        'A': random.choice(state),
        'B': random.choice(state),
        'C': random.choice(state)
    }

    print("\nInitial Environment State:", environment, end="\n\n")

    room='A'
    cost=0
    steps=12

    for step in range(steps):
        status=environment[room]
        percept=(room, status)
        action=rule_table[percept]

        print(f"{step+1:>4}  {room:^8}  {status:^7}  {action}")

        if action=='Cleanse':
            environment[room]='Clean'
            cost +=20
        elif action=='Right':
            if room=='A':
                room='B'
            elif room=='B':
                room='C'
            cost +=5
        elif action=='Left':
            if room=='C':
                room='B'
            elif room=='B':
                room='A'
            cost +=5

    print("\nFinal Environment State:", environment)
    print("\nTotal Performance Cost:", cost)


if __name__=='__main__':
    main()