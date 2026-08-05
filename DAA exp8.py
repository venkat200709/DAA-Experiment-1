from itertools import permutations

INF = float('inf')


def reduce_matrix(mat):
    """Reduce matrix and return reduction cost"""
    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min != INF and row_min != 0:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min != INF and col_min != 0:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_brute_force(cost, n):
    """Brute Force TSP"""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total_cost = 0
        for i in range(n):
            total_cost += cost[path[i]][path[i + 1]]

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# -------- Cost Matrix --------
cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

n = 5
cities = ['A', 'B', 'C', 'D', 'E']

best_path, best_cost = tsp_brute_force(cost, n)

print("5-City TSP - Cost Matrix:")
print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))

for i, row in enumerate(cost):
    values = ['INF' if x == INF else str(x) for x in row]
    print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in values))

print(f"\nOptimal Tour: {' -> '.join(cities[i] for i in best_path)}")
print(f"Minimum Cost: {best_cost}")

print("\nPath Verification:")
for i in range(n):
    u = best_path[i]
    v = best_path[i + 1]
    print(f"{cities[u]} -> {cities[v]} : Cost = {cost[u][v]}")
