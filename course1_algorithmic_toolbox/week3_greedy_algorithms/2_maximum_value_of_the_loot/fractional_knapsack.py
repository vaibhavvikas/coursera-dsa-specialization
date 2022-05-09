# Uses python3
import sys

def get_optimal_value(capacity, weights, values, n):
    value, ind_ = 0, 0
    per_unit_weight = [[values[i]/weights[i], i] for i in range(n)]
    per_unit_weight.sort(key=lambda x: x[0], reverse=True)
    while capacity > 0 and ind_ < n:
        if weights[per_unit_weight[ind_][1]] > capacity:
            value += capacity*per_unit_weight[ind_][0]
            break
        else:
            value += values[per_unit_weight[ind_][1]]
            capacity -= weights[per_unit_weight[ind_][1]]
        ind_ += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values, n)
    print("{:.10f}".format(opt_value))
