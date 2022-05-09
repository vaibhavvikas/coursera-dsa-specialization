# Uses python3
import sys

def optimal_summands(n):
    summands, an = [], 0
    while n:
        an += 1
        if 2 * an + 1 > n:
            summands.append(n)
            break
        summands.append(an)
        n-= an
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
