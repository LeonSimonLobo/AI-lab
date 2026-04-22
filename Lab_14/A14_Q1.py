def forward(rules, facts, goal):
    inferred=set(facts)
    step=1
    print("Initial facts:", inferred)
    while True:
        added=False
        for lhs, rhs in rules:
            print("Step", step, "Checking rule:", lhs, "->", rhs)
            step +=1
            if all(x in inferred for x in lhs):
                if rhs not in inferred:
                    inferred.add(rhs)
                    print("  Condition Satisfied")
                    print("  Added:", rhs, "| New facts:", inferred)
                    added=True
                else:
                    print("  Already present")
            else:
                print("  Condition not satisfied")
        if goal in inferred:
            print("Goal reached:", goal)
            return True
        if not added:
            print("No more changes")
            return False
        
        
def main():
    rules1=[
        (["P"], "Q"),
        (["L","M"], "P"),
        (["A","B"], "L")
    ]

    facts1=["A","B","M"]

    rules2=[
        (["A"], "B"),
        (["B"], "C"),
        (["C"], "D"),
        (["D","E"], "F")
    ]

    facts2=["A","E"]

    print("\n--- Forward Chaining Set 1 ---")
    forward(rules1, facts1, "Q")

    print("\n--- Forward Chaining Set 2 ---")
    forward(rules2, facts2, "F")

if __name__=='__main__':
    main()