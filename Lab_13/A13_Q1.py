class Symbol:
    def __init__(self, name):
        self.name=name
        self.value=False

def NOT(p):
    return not p

def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IMP(p, q):
    return NOT(p) or q

def IFF(p, q):
    return p==q

def b(x):
    return 1 if x else 0

def truth_table_2(name, func):
    vals=[False, True]
    P=Symbol("P")
    Q=Symbol("Q")

    print(name)
    print("P Q Result")

    for p in vals:
        for q in vals:
            P.value=p
            Q.value=q
            result=func(P, Q)
            print(b(P.value), b(Q.value), "True" if result else "False")
    print()

def truth_table_3(name, func):
    vals=[False, True]
    P=Symbol("P")
    Q=Symbol("Q")
    R=Symbol("R")

    print(name)
    print("P Q R Result")

    for p in vals:
        for q in vals:
            for r in vals:
                P.value=p
                Q.value=q
                R.value=r
                result=func(P, Q, R)
                print(b(P.value), b(Q.value), b(R.value), "True" if result else "False")
    print()

def main():
    truth_table_2("~P -> Q", lambda p,q: IMP(NOT(p.value), q.value))
    truth_table_2("~P ∧ Q", lambda p,q: AND(NOT(p.value), q.value))
    truth_table_2("~P ∨ Q", lambda p,q: OR(NOT(p.value), q.value))
    truth_table_2("P -> Q", lambda p,q: IMP(p.value, q.value))
    truth_table_2("~P <-> Q", lambda p,q: IFF(NOT(p.value), q.value))
    truth_table_2("(P ∨ Q) ∧ (~P -> Q)", lambda p,q: AND(OR(p.value,q.value), IMP(NOT(p.value), q.value)))

    truth_table_3("(P ∨ Q) -> R", 
                  lambda p,q,r: IMP(OR(p.value,q.value), r.value))

    truth_table_3("((P ∨ Q) -> R) <-> ((~P ∧ Q) -> R)", 
                  lambda p,q,r: IFF(
                      IMP(OR(p.value,q.value), r.value),
                      IMP(AND(NOT(p.value), q.value), r.value)
                  ))

    truth_table_3("((P -> Q) ∧ (Q -> R)) -> (P -> R)", 
                  lambda p,q,r: IMP(
                      AND(IMP(p.value,q.value), IMP(q.value,r.value)),
                      IMP(p.value,r.value)
                  ))

    truth_table_3("((P -> (Q ∨ R)) -> (~P ∧ ~Q ∧ ~R))", 
                  lambda p,q,r: IMP(
                      IMP(p.value, OR(q.value,r.value)),
                      AND(NOT(p.value), AND(NOT(q.value), NOT(r.value)))
                  ))

if __name__=='__main__':
    main()