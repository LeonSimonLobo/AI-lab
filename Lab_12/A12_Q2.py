grid=[
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

domains={}
for i in range(9):
    for j in range(9):
        if grid[i][j]==0:
            domains[(i,j)]=[1,2,3,4,5,6,7,8,9]
        else:
            domains[(i,j)]=[grid[i][j]]

def neighbors(cell):
    i,j=cell
    n=[]
    for k in range(9):
        if (i,k) !=cell and (i,k) not in n:
            n.append((i,k))
        if (k,j) !=cell and (k,j) not in n:
            n.append((k,j))
    bi=(i//3)*3
    bj=(j//3)*3
    for x in range(bi,bi+3):
        for y in range(bj,bj+3):
            if (x,y) !=cell and (x,y) not in n:
                n.append((x,y))
    return n

def revise(xi, xj):
    revised=False
    to_remove=[]
    for x in domains[xi]:
        flag=True
        for y in domains[xj]:
            if x!=y:
                flag=False
                break
        if flag:
            to_remove.append(x)
    for x in to_remove:
        domains[xi].remove(x)
        revised=True
    return revised

def ac3():
    queue=[]
    for xi in domains:
        for xj in neighbors(xi):
            queue.append((xi,xj))
    step=0

    while queue:
        xi,xj=queue.pop(0)
        old_domain=domains[xi][:]

        changed=revise(xi,xj)

        step +=1
        if step <=5:
            if changed:
                print(f"Arc ({xi},{xj}) checked, domain reduced: {old_domain} → {domains[xi]}")
            else:
                print(f"Arc ({xi},{xj}) checked, no change")

        if changed:
            if len(domains[xi])==0:
                return False
            for xk in neighbors(xi):
                if xk !=xj:
                    queue.append((xk,xi))
    return True

def main():
    ac3()

    removed=0
    for cell in domains:
        if grid[cell[0]][cell[1]]==0:
            removed +=9 - len(domains[cell])

    print("Number of values removed:", removed)
    print("\nUpdated domain sizes:")
    for i in range(9):
        row=[]
        for j in range(9):
            row.append(len(domains[(i,j)]))
        print(*row)

if __name__=='__main__':
    main()