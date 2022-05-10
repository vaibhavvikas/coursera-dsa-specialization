# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return a[left]

    mid = left + (right - left)//2
    left_maj = get_majority_element(a, left, mid)
    right_maj = get_majority_element(a, mid + 1, right)

    c1, c2 = 0, 0

    for i in a[left:right+1]:
        if i == left_maj:
            c1 += 1
        elif i == right_maj:
            c2 += 1

    if c1 > (right - left + 1)//2 and left_maj != -1:
        return left_maj
    elif c2 > (right - left + 1)//2 and right_maj != -1:
        return right_maj

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
