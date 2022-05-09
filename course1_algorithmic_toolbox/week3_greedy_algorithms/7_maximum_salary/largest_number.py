#Uses python3

import sys

def largest_number(a):
    max_length = len(str(max(a)))
    temp_arr = [(str(each)*max_length, each) for each in a]
    temp_arr.sort(reverse=True)
    return "".join(str(each[1]) for each in temp_arr)

if __name__ == '__main__':
    input = list(map(int, sys.stdin.read().split()))
    a = input[1:]
    print(largest_number(a))
