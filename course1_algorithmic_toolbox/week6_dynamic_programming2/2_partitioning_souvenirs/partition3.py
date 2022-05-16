import sys

dp = {}

def checkEqualSumUtil(arr, N, sm1, sm2, sm3, j):
    s = str(sm1) + "_" + str(sm2) + str(j)
    if j == N:
        if sm1 == sm2 and sm2 == sm3:
            return 1
        else:
            return 0

    if s in dp:
        return dp[s]

    l = checkEqualSumUtil(arr, N, sm1 + arr[j], sm2, sm3, j + 1)
    m = checkEqualSumUtil(arr, N, sm1, sm2 + arr[j], sm3, j + 1)
    r = checkEqualSumUtil(arr, N, sm1, sm2, sm3 + arr[j], j + 1)
    dp[s] = max(l, m, r)
    return dp[s]
 

def partition3(arr, N):
    sum1 = sum2 = sum3 = 0
    if checkEqualSumUtil(arr, N, sum1, sum2, sum3, 0) == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A, n))
