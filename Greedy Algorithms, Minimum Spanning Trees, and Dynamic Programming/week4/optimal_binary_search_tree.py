class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def optimal_bst(key2freq):
    n = len(key2freq.keys())
    sorted_keys = [None] + sorted(key2freq.keys())
    s = [[(0, None)] * (n + 1) for _ in range(n + 1)]  # store pair of cost, node

    def get_s(i, j):
        return s[i][j] if i <= j else (0, None)

    for gap in range(n):
        for i in range(1, n - gap + 1):
            grow_sum = sum([key2freq[key] for key in sorted_keys[i: i + gap + 1]])
            possible_solutions = [
                (r,
                 grow_sum +
                 get_s(i, r - 1)[0] +
                 get_s(r + 1, i + gap)[0])
                for r in range(i, i + gap + 1)]
            best_r, cost = sorted(possible_solutions, key=lambda t: t[1])[0]
            s[i][i + gap] = (cost, Node(key=best_r, left=get_s(i, best_r - 1)[1], right=get_s(best_r + 1, i + gap)[1]))
    return s[1][n]


if __name__ == '__main__':
    key2freq = {
        1: .05,
        2: .4,
        3: .08,
        4: .04,
        5: .1,
        6: .1,
        7: .23
    }
    cost, root = optimal_bst(key2freq)
    print(cost)