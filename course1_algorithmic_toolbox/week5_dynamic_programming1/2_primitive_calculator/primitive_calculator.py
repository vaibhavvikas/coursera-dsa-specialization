# Uses python3
from audioop import reverse
import math
import sys


def fill_dp(n):
    for i in range(2, n+1):
        x = operations[i-1] + 1
        y, z =[math.inf]*2
        if i % 2 == 0:
            y = operations[i//2] + 1
        if i % 3 == 0:
            z = operations[i//3] + 1
        operations[i] = min(x, y, z)


def optimal_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 3 == 0 and operations[n] - 1 == operations[n//3]:
            sequence.append(n//3)
            n = n // 3
        elif n % 2 == 0 and operations[n] - 1 == operations[n//2]:
            sequence.append(n//2)
            n = n // 2
        else:
            sequence.append(n - 1)
            n = n - 1
    return sequence


if __name__ == "__main__":    
    input = sys.stdin.read()
    n = int(input)
    operations = [0, 0] + [math.inf]*(n-1)
    fill_dp(n)
    sequence = optimal_sequence(n)
    print(operations[n])
    print(" ".join([str(i) for i in reversed(sequence)]))
