import math
import random


def two_sat(n, clauses):
    """
    :param n: variable number
    :param clauses:
    a list of clause, each clause is represented by a 4-item tuple (idx1, negate?, idx2, negate?)
    "negate?" is either 0 or 1. For example, (2, 0, 5, 1) stands for  "v2 or (not v5)"
    index range is 1 ~ n
    :return: A list of variable values or None if not satisfiable
    """
    vars = [0 for n in range(n + 1)]

    def eval_clause(clause):
        idx1, neg1, idx2, neg2 = clause
        return vars[idx1] ^ neg1 or vars[idx2] ^ neg2

    # loop for log(2,n) times
    for _ in range(int(math.ceil(math.log2(n)))):

        # random initialize vars
        for i in range(n + 1):
            vars[i] = random.randint(0, 1)

        for clause in clauses:
            if not eval_clause(clause):
                idx1, idx2 = clause[0], clause[2]
                if random.randint(0, 1):
                    vars[idx1] = not vars[idx1]
                else:
                    vars[idx2] = not vars[idx2]
        else:
            return vars[1:]

    return None


if __name__ == '__main__':
    # example:  (x1 v x2) ^ (~x1 v x3) ^ (x3 v x4) ^ (~x2 v ~x4)
    clauses = [
        (1, 0, 2, 0),
        (1, 1, 3, 0),
        (3, 0, 4, 0),
        (2, 1, 4, 1)
    ]
    result = two_sat(4, clauses)
    print(result)
