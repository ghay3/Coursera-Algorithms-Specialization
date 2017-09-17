from collections import namedtuple

Point = namedtuple('Point', 'x y')


def distance(pair):
    p1, p2 = pair
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2


# https://en.wikipedia.org/wiki/Closest_pair_of_points_problem
def closest_pair(points):
    Px = sorted(points, key=lambda p: p.x)
    Py = sorted(points, key=lambda p: p.y)
    return _closest_pair(Px, Py)


def _closest_pair(Px, Py):
    if len(Px) <= 3:
        return solve_pair_for_base_case(Px)

    Lx, Ly, Rx, Ry = split_points(Px, Py)
    pair1 = _closest_pair(Lx, Ly)
    pair2 = _closest_pair(Rx, Ry)

    x_mid = Lx[-1].x
    delta = min(distance(pair1), distance(pair2))
    pair3 = closest_split_pair(Px, Py, x_mid, delta)

    candidate_pairs = [pair1, pair2] + ([pair3] if pair3 else [])
    return sorted(candidate_pairs, key=distance)[0]


def split_points(Px, Py):
    """split P into 2 parts L(left) and R(right), each part with two sorted version by x and y"""
    n = len(Px) // 2
    Lx = Px[:n]
    Rx = Px[n:]

    L_set = set(Lx)
    Ly = [p for p in Py if p in Lx]
    Ry = [p for p in Py if p not in Lx]
    return Lx, Ly, Rx, Ry


def closest_split_pair(Px, Py, x_mid, delta):
    Sy = [p for p in Py if x_mid - delta <= p.x <= x_mid + delta]
    n = len(Sy)
    if n <= 1:
        return None

    min_pair = Sy[0], Sy[1]
    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            if distance((Sy[i], Sy[j])) < distance(min_pair):
                min_pair = Sy[i], Sy[j]

    return min_pair


def solve_pair_for_base_case(points):
    min_pair = points[0], points[1]
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            if distance((points[i], points[j])) < distance(min_pair):
                min_pair = points[i], points[j]

    return min_pair


if __name__ == '__main__':
    import numpy as np
    for _ in range(10):
        x_axis = np.random.randint(-1000, 1000, size=20).tolist()
        y_axis = np.random.randint(-1000, 1000, size=20).tolist()
        points = [Point(x=x, y=y) for x in x_axis for y in y_axis]

        algorithm_result = closest_pair(points)
        correct_result = solve_pair_for_base_case(points)
        if distance(algorithm_result) != distance(correct_result):  # doesn't handle tie case
            print('result mismtach for ', points)
            break
