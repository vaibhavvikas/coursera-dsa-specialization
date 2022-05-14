# Uses python3


def edit_distance(a, b):
    dp_list = [[i if j == 0 else -1 for i in range(len(a) + 1) ] for j in range(len(b) + 1)]

    for i in range(len(b) + 1):
        dp_list[i][0] = i 
    
    for j in range(1, len(a)+1):
        for i in range(1, len(b)+1):
            if b[i - 1] == a[j - 1]:
                dp_list[i][j] = min(dp_list[i-1][j] + 1, dp_list[i][j-1] + 1, dp_list[i-1][j-1])
            else:
                dp_list[i][j] = min(dp_list[i-1][j] + 1, dp_list[i][j-1] + 1, dp_list[i-1][j-1] + 1)

    return dp_list[-1][-1]

if __name__ == "__main__":
    a, b = input(), input()
    print(edit_distance(a, b))
