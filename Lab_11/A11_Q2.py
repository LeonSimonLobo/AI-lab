letters=["D","E","Y","N","R","O","S","M"]

def is_valid_partial(assign):
    if 'S' in assign and assign['S']==0:
        return False
    if 'M' in assign and assign['M']==0:
        return False

    if all(k in assign for k in ['D','E','Y']):
        if (assign['D'] + assign['E']) % 10 !=assign['Y']:
            return False

    if all(k in assign for k in ['N','R','E']):
        c1=(assign['D'] + assign['E']) // 10 if all(k in assign for k in ['D','E']) else 0
        if (assign['N'] + assign['R'] + c1) % 10 !=assign['E']:
            return False

    if all(k in assign for k in ['E','O','N']):
        c1=(assign['D'] + assign['E']) // 10 if all(k in assign for k in ['D','E']) else 0
        c2=(assign['N'] + assign['R'] + c1) // 10 if all(k in assign for k in ['N','R']) else 0
        if (assign['E'] + assign['O'] + c2) % 10 !=assign['N']:
            return False

    if all(k in assign for k in ['S','M','O']):
        c1=(assign['D'] + assign['E']) // 10 if all(k in assign for k in ['D','E']) else 0
        c2=(assign['N'] + assign['R'] + c1) // 10 if all(k in assign for k in ['N','R']) else 0
        c3=(assign['E'] + assign['O'] + c2) // 10 if all(k in assign for k in ['E','O']) else 0
        if (assign['S'] + assign['M'] + c3) % 10 !=assign['O'] or (assign['S'] + assign['M'] + c3) / 10 !=1:
            return False

    if 'M' in assign:
        if assign['M'] !=1:
            return False

    return True


def backtrack(assign, used):
    if len(assign)==8:
        return assign
    for var in letters:
        if var not in assign:
            break
    for d in range(10):
        if d not in used:
            assign[var]=d
            used.add(d)

            if is_valid_partial(assign):
                result=backtrack(assign, used)
                if result:
                    return result

            del assign[var]
            used.remove(d)

    return None


def main():
    assign={'M':1}
    solution=backtrack(assign, set([1]))

    print("Solution:", solution)

    D,E,Y,N,R,O,S,M=[solution[l] for l in letters]

    SEND=1000*S + 100*E + 10*N + D
    MORE=1000*M + 100*O + 10*R + E
    MONEY=10000*M + 1000*O + 100*N + 10*E + Y

    print("\n", SEND)
    print("+", MORE)
    print("------")
    print(MONEY)


if __name__=='__main__':
    main()