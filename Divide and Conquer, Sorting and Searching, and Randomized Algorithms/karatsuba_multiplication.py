import random


# https://en.wikipedia.org/wiki/Karatsuba_algorithm
def karatsuba(num1, num2):
    # deal with negative numbers
    if num1 < 0:
        return -1 * karatsuba(-num1, num2)
    if num2 < 0:
        return -1 * karatsuba(num1, -num2)

    # naive multiplication
    if num1 < 10 or num2 < 10:
        return num1 * num2

    # calculate the max length of digits
    m = max(len(str(num1)), len(str(num2)))
    m2 = m // 2

    # split the digit sequences about the middle
    high1, low1 = split_at(num1, m2)
    high2, low2 = split_at(num2, m2)

    # 3 calls made to numbers approximately half the size
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return z2*10**(2*m2) + (z1 - z2 - z0)*10**m2 + z0


def split_at(num, m):
    s = str(num)
    if len(s) > m:
        return int(s[:-m]), int(s[-m:])
    else:
        return 0, num


if __name__ == '__main__':
    for _ in range(1000):
        a = random.randint(-10000, 10000)
        b = random.randint(-10000, 10000)
        karatsuba_result = karatsuba(a, b)
        correct_result = a * b
        if karatsuba_result != correct_result:
            print('mismatch for %s and %s' % (a, b))
            break
