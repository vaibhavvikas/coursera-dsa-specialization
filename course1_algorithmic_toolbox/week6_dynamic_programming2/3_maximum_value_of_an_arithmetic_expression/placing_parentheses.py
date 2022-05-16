# Uses python3
import math, re


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def MinAndMax(M, m, i, j, operators):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(operands, operators):
    n = len(operands)
    m = [[None for _ in range(n)] for _ in range(n)]
    M = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)

    return M[0][n-1]


if __name__ == "__main__":
    expression = input()
    operands = re.split("\s|[\+\-\*]", expression)
    operators = [each for each in expression if each in ["+", "-", "*"]]
    operands = [int(each) for each in operands]
    print(get_maximum_value(operands, operators))
