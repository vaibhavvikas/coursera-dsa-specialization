# python3
import numpy

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    dp_list = numpy.zeros((len(first_sequence) + 1, len(second_sequence) + 1, len(third_sequence) + 1))

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            for k in range(1, len(third_sequence) + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    dp_list[i][j][k] = dp_list[i - 1][j - 1][k - 1] + 1
                else:
                    dp_list[i][j][k] = max(dp_list[i - 1][j][k], dp_list[i][j - 1][k], dp_list[i][j][k-1])

    return int(dp_list[-1][-1][-1])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
