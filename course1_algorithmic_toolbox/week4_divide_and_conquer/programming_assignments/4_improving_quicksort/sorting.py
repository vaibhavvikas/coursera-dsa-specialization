# Uses python3
import sys
import random

def partition3(a, l, r):
    x, j, k = a[l], l, r
    i = l

    while i <= k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
            i += 1
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
        else:
            i += 1
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    z = random.randint(l, r)
    a[l], a[z] = a[z], a[l]
    j, k = partition3(a, l, r)
    randomized_quick_sort(a, l, j - 1);
    randomized_quick_sort(a, k + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
