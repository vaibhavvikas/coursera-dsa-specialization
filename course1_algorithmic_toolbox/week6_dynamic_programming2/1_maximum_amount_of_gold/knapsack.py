# python3
import numpy

def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    value = numpy.zeros((capacity + 1, len(weights) + 1))
    
    for i in range(1, len(weights) + 1):
        for w in range(1, capacity + 1):
            value[w][i] = value[w][i-1]
            if weights[i-1] <= w:
                value[w][i] = max(value[w][i], value[w-weights[i-1]][i-1] + weights[i-1])

    return int(value[-1][-1])


if __name__ == '__main__':
    input_capacity, n = map(int, input().split())
    input_weights = list(map(int, input().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
