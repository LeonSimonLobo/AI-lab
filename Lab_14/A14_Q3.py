def negate(l):
    return l[1:] if l.startswith("~") else "~" + l

def resolve(c1, c2):
    res=[]
    for x in c1:
        if negate(x) in c2:
            new=set(c1 + c2)
            new.remove(x)
            new.remove(negate(x))
            res.append(list(new))
    return res

def resolution(kb):
    print("Initial KB:", kb)
    step=1
    while True:
        new=[]
        for i in range(len(kb)):
            for j in range(i+1, len(kb)):
                resolvents=resolve(kb[i], kb[j])
                if resolvents:
                    step +=1
                    print("Step", step, "Resolving:", kb[i], "and", kb[j])
                    for r in resolvents:
                        print("  Derived:", r)
                        if len(r)==0:
                            print("Empty clause found")
                            return True
                        if r not in kb and r not in new:
                            new.append(r)
        if not new:
            print("No new clauses")
            return False
        print("New clauses added:", new)
        kb +=new

def main():
    print("\n--- Resolution Set A ---")
    kb1=[
        ["P","Q"],
        ["~P","R"],
        ["~Q","S"],
        ["~R","S"],
        ["~S"]
    ]
    resolution(kb1)

    print("\n--- Resolution Set B ---")
    kb2=[
        ["~P","Q"],
        ["~Q","R"],
        ["~S","~R"],
        ["P"],
        ["~R"]
    ]
    resolution(kb2)

if __name__=="__main__":
    main()