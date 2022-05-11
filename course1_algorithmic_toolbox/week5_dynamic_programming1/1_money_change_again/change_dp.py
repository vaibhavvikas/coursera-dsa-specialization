# Uses python3
import sys


dp = [-1] * 1001
coin_array = [1, 3, 4]


def get_change(m):
    global dp, coin_array

    if m == 0:
        return 0
    if dp[m] > 0:
        return dp[m]
    
    for coin in coin_array:
        if coin <= m:
            nextTry = get_change(m - coin)
        if dp[m] <= 0 or dp[m] > nextTry + 1:
            dp[m] = nextTry + 1
    return dp[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
