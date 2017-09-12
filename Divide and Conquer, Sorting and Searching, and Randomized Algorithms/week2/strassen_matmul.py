import numpy as np


def strassen_matmul(A, B):
    """only deals with two n*n matrix where n is 2^*"""
    n = A.shape[0]
    m = n // 2

    if n == 1:
        return A * B

    A11 = A[:m, :m]
    A12 = A[:m, m:]
    A21 = A[m:, :m]
    A22 = A[m:, m:]

    B11 = B[:m, :m]
    B12 = B[:m, m:]
    B21 = B[m:, :m]
    B22 = B[m:, m:]

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12

    P1 = strassen_matmul(A11, S1)
    P2 = strassen_matmul(S2, B22)
    P3 = strassen_matmul(S3, B11)
    P4 = strassen_matmul(A22, S4)
    P5 = strassen_matmul(S5, S6)
    P6 = strassen_matmul(S7, S8)
    P7 = strassen_matmul(S9, S10)

    C = np.zeros(A.shape)
    C[:m, :m] = P5 + P4 - P2 + P6
    C[:m, m:] = P1 + P2
    C[m:, :m] = P3 + P4
    C[m:, m:] = P5 + P1 - P3 - P7

    return C


if __name__ == '__main__':
    for n in 2 ** np.arange(0, 8):
        A = np.random.randint(-1000, 1000, size=(n, n))
        B = np.random.randint(-1000, 1000, size=(n, n))
        strassen_result = strassen_matmul(A, B)
        correct_result = np.dot(A, B)
        if not np.array_equal(strassen_result, correct_result):
            print('mismatch for matrix:')
            print(A)
            print(B)
            break
