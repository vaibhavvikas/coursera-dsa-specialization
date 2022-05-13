# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = {}
    points_list = [[each, "l"] for each in starts]\
        + [[each, "r"] for each in ends]\
        + [[each, "p"] for each in points]

    points_list.sort()
    no_of_segments = 0
    for each in points_list:
        if each[1] == "l":
            no_of_segments += 1
        elif each[1] == "r":
            no_of_segments -= 1
        else:
            cnt[each[0]] = no_of_segments
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in points:
        print(cnt[x], end=' ')
