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

cities=[0, 1, 2, 3, 4, 5, 6, 7]
n=8
initial_parents=4
iterations=100


def fitness(route):
    cost=0
    for i in range(1,n):
        cost+=graph[route[i-1]][route[i]]
    return 1/cost


def mutate(route):
    chance=random.randint(1,10)
    if chance<3:
        city1=random.randint(0,7)
        city2=random.randint(0,7)
        temp_city=route[city1]
        route[city1]=route[city2]
        route[city2]=temp_city
        #print("mutated")
    return route


def genetic_1(graph):
    parents=[]
    generations=iterations
    for i in range(initial_parents):
        temp=random.sample(cities, n)
        fit=fitness(temp)
        parents.append((fit,temp))
    children=parents.copy()
    print("Initial Parents:-")
    for parent in parents:
        print(parent[1],end=" ")
    print("\n")
    while generations>=0:
        parents=children.copy()
        parents.sort()
        crossover=random.randint(1,n-2)
        children=[]
        for i in range(0,initial_parents-1,2):
            temp1=parents[i][1][:crossover]
            temp2=parents[i+1][1][:crossover]
            for city in parents[i+1][1]:
                if city not in temp1:
                    temp1.append(city)
            for city in parents[i][1]:
                if city not in temp2:
                    temp2.append(city)
            temp1=mutate(temp1)
            temp2=mutate(temp2)
            fit1=fitness(temp1)
            fit2=fitness(temp2)
            children.append((fit1,temp1))
            children.append((fit2,temp2))
        children.sort()
        #print(parents,children,crossover)
        generations-=1
    return children[initial_parents-1]


def genetic_2(graph):
    parents=[]
    generations=iterations
    for i in range(initial_parents):
        temp=random.sample(cities, n)
        fit=fitness(temp)
        parents.append((fit,temp))
    children=parents.copy()
    print("Initial Parents:-")
    for parent in parents:
        print(parent[1],end=" ")
    print("\n")
    while generations>=0:
        parents=children.copy()
        parents.sort()
        crossover1=random.randint(2,n-4)
        crossover2=random.randint(crossover1+2,n-2)
        children=[]
        for i in range(0,initial_parents-1,2):
            temp1=[None]*n
            temp1[crossover1:crossover2]=parents[i+1][1][crossover1:crossover2]
            temp2=[None]*n
            temp2[crossover1:crossover2]=parents[i][1][crossover1:crossover2]
            index=0
            for city in parents[i+1][1]:
                if city not in temp1:
                    while index<n and temp1[index] is not None:
                        index+=1
                    temp1[index]=city
            index=0
            for city in parents[i][1]:
                if city not in temp2:
                    while index<n and temp2[index] is not None:
                        index+=1
                    temp2[index]=city
            temp1=mutate(temp1)
            temp2=mutate(temp2)
            fit1=fitness(temp1)
            fit2=fitness(temp2)
            children.append((fit1,temp1))
            children.append((fit2,temp2))
        children.sort()
        #print(parents,children,crossover1,crossover2)
        generations-=1
    return children[initial_parents-1]


def main():
    print("===== Genetic with one crossover ======")
    fit,path=genetic_1(graph)
    print(path,1/fit)
    print("===== Genetic with two crossovers ======")
    fit,path=genetic_2(graph)
    print(path,1/fit)

if __name__=='__main__':
    main()