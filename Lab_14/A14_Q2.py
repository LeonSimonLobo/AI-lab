def backward(goal, rules, facts, depth=0):
    print("  " * depth + "Goal:", goal)
    if goal in facts:
        print("  " * depth + "Found in facts")
        return True
    for lhs, rhs in rules:
        if rhs==goal:
            print("  " * depth + "Using rule:", lhs, "->", rhs)
            if all(backward(x, rules, facts, depth+1) for x in lhs):
                print("  " * depth + "Derived:", goal)
                return True
    print("  " * depth + "Failed:", goal)
    return False

def main():
    rules1=[
        (["P"], "Q"),
        (["R"], "Q"),
        (["A"], "P"),
        (["B"], "R")
    ]
    facts1=["A","B"]

    rules2=[
        (["A"], "B"),
        (["B","C"], "D"),
        (["E"], "C")
    ]
    facts2=["A","E"]

    print("\n--- Backward Chaining Set 1 ---")
    backward("Q", rules1, facts1)

    print("\n--- Backward Chaining Set 2 ---")
    backward("D", rules2, facts2)

if __name__=="__main__":
    main()