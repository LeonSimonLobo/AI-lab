variables=["P1","P2","P3","P4","P5","P6"]

domains={v: ["R1","R2","R3"][:] for v in variables}

constraints={
    "P1": ["P2","P3","P6"],
    "P2": ["P1","P3","P4"],
    "P3": ["P1","P2","P5"],
    "P4": ["P2","P6"],
    "P5": ["P3","P6"],
    "P6": ["P1","P4","P5"]
}

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
    for xi in variables:
        for xj in constraints[xi]:
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
            for xk in constraints[xi]:
                if xk !=xj:
                    queue.append((xk,xi))
    return True


def main():
    result=ac3()
    print(result)
    print(domains)
    domains["P1"]=["R1"]
    print("After assigning room 1 to team 1:")
    result=ac3()
    print(result)
    print(domains)

if __name__=='__main__':
    main()