import random

def generate_letters(k):
    letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(letters)
    return letters[:k]

nodes=list({
    "Kachchh","Banaskantha","Patan","Mehsana","Sabarkantha","Gandhinagar",
    "Ahmedabad","Kheda","Panchmahal","Dahod","Vadodara","Anand","Bharuch",
    "Narmada","Surat","Navsari","Valsad","Dang","Surendranagar","Rajkot",
    "Jamnagar","Amreli","Bhavnagar","Junaghad","Porbandar"
})

index={nodes[i]: i for i in range(len(nodes))}
n=len(nodes)

matrix=[[0]*n for _ in range(n)]

edges=[
    ("Kachchh","Banaskantha"),("Kachchh","Patan"),("Kachchh","Surendranagar"),
    ("Banaskantha","Patan"),("Banaskantha","Sabarkantha"),
    ("Patan","Mehsana"),("Patan","Surendranagar"),
    ("Mehsana","Sabarkantha"),("Mehsana","Gandhinagar"),("Mehsana","Ahmedabad"),
    ("Sabarkantha","Gandhinagar"),("Sabarkantha","Panchmahal"),
    ("Gandhinagar","Ahmedabad"),("Gandhinagar","Kheda"),
    ("Ahmedabad","Kheda"),("Ahmedabad","Anand"),("Ahmedabad","Surendranagar"),
    ("Kheda","Anand"),("Kheda","Panchmahal"),
    ("Panchmahal","Dahod"),("Panchmahal","Vadodara"),
    ("Vadodara","Anand"),("Vadodara","Bharuch"),("Vadodara","Narmada"),
    ("Anand","Bharuch"),
    ("Bharuch","Narmada"),("Bharuch","Surat"),
    ("Narmada","Surat"),
    ("Surat","Navsari"),("Surat","Dang"),
    ("Navsari","Valsad"),("Navsari","Dang"),
    ("Surendranagar","Rajkot"),
    ("Rajkot","Jamnagar"),("Rajkot","Amreli"),("Rajkot","Bhavnagar"),("Rajkot","Porbandar"),("Rajkot","Junaghad"),
    ("Amreli","Bhavnagar"),("Amreli","Junaghad"),
    ("Porbandar","Junaghad"),
    ("Bhavnagar","Ahmedabad")
]

for u,v in edges:
    i,j=index[u], index[v]
    matrix[i][j]=1
    matrix[j][i]=1


def is_valid(node, color, assignment):
    i=index[node]
    for j in range(n):
        if matrix[i][j]==1:
            neighbor=nodes[j]
            if neighbor in assignment and assignment[neighbor]==color:
                return False
    return True

def backtrack(assignment,colors):
    result=False
    if len(assignment)==n:
        return assignment
    for node in nodes:
        if node not in assignment:
            break
    for color in colors:
        if is_valid(node, color, assignment):
            assignment[node]=color
            result=backtrack(assignment,colors)
            if result:
                return result
            del assignment[node]
    return None

def main(): 
    solution=False
    num_color=1
    while not solution:
        colors=generate_letters(num_color)
        solution=backtrack({},colors)
        num_color+=1

    print("Solution Found:\n")
    for district in solution:
        print(f"{district} → {solution[district]}")
    print("Number of colours used:",num_color-1)

if __name__=='__main__':
    main()