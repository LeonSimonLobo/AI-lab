import random


def read_csv(filename):
    points=[]
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            x, y=map(float, line.strip().split(','))
            points.append([x, y])
    return points


def distance_sq(p, c):
    return (p[0] - c[0])**2 + (p[1] - c[1])**2


def assign_clusters(points, airports):
    labels=[]
    for p in points:
        distances=[distance_sq(p, c) for c in airports]
        labels.append(distances.index(min(distances)))
    return labels


def update_airports(points, labels, k, airports, lr=0.01):
    new_airports=[a[:] for a in airports]

    for i in range(k):
        cluster_points=[points[j] for j in range(len(points)) if labels[j]==i]

        if cluster_points:
            grad_x=0
            grad_y=0

            for p in cluster_points:
                grad_x +=(p[0] - airports[i][0])
                grad_y +=(p[1] - airports[i][1])

            grad_x *=-2
            grad_y *=-2

            new_airports[i][0]=airports[i][0] - lr * grad_x
            new_airports[i][1]=airports[i][1] - lr * grad_y

    return new_airports


def newton_update(points, labels, k, airports):
    new_airports=[a[:] for a in airports]

    for i in range(k):
        cluster_points=[points[j] for j in range(len(points)) if labels[j]==i]

        if cluster_points:
            n=len(cluster_points)

            grad_x=0
            grad_y=0

            for p in cluster_points:
                grad_x +=(p[0] - airports[i][0])
                grad_y +=(p[1] - airports[i][1])

            grad_x *=-2
            grad_y *=-2

            new_airports[i][0]=airports[i][0] - (1/(2*n)) * grad_x
            new_airports[i][1]=airports[i][1] - (1/(2*n)) * grad_y
        else:
            new_airports[i]=points[random.randint(0, len(points)-1)]

    return new_airports


def first_order(points, airports, k):
    for _ in range(100):
        labels=assign_clusters(points, airports)
        new_airports=update_airports(points, labels, k, airports)

        if new_airports==airports:
            print(f"Found close enough after {_} iterations")
            break

        airports=new_airports

    return airports, labels


def second_order(points, airports, k):
    for _ in range(10):
        labels=assign_clusters(points, airports)
        new_airports=newton_update(points, labels, k, airports)

        if new_airports==airports:
            print(f"\n\nFound close enough after {_} iterations")
            break

        airports=new_airports

    return airports, labels


def compute_cost(points, airports, labels):
    cost=0
    for i in range(len(points)):
        c=airports[labels[i]]
        cost +=distance_sq(points[i], c)
    return cost


def main():
    points=read_csv( "c:\Education\SVNIT\Coding\AI\Lab_10\cities.csv")

    k=3
    airports=random.sample(points, k)

    print("Starting airport locations:\n", airports)

    airports_first_order, labels_first_order=first_order(points, airports, k)

    print("=====First Order Derivatives=====")
    for i in range(3):
        airport=airports_first_order[i]
        print(f"Airport {i+1} at location: {airport}\n has following cities closest to it:-")
        print("City \t\t Distance")
        for j in range(len(points)):
            if labels_first_order[j]==i:
                print(f"{points[j]}\t{distance_sq(points[j], airport)}")

    airports_second_order, labels_second_order=second_order(points, airports, k)

    print("\n=====Second Order Derivatives=====")
    for i in range(3):
        airport=airports_second_order[i]
        print(f"Airport {i+1} at location: {airport}\n has following cities closest to it:-")
        print("City \t\t Square of Distance")
        for j in range(len(points)):
            if labels_second_order[j]==i:
                print(f"{points[j]}\t{distance_sq(points[j], airport)}")

    cost_first=compute_cost(points, airports_first_order, labels_first_order)
    cost_second=compute_cost(points, airports_second_order, labels_second_order)

    print("Gradient Descent Cost:", cost_first)
    print("Newton Method Cost:", cost_second)


if __name__=='__main__':
    main()