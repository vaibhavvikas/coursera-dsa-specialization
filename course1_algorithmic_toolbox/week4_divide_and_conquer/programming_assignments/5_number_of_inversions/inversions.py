# python3
import sys

def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    final = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]

    return final, inversion_counter

def merge_sort(arr):
    global inv_count

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    inv_count += temp

    return sorted_arr

inv_count = 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    merge_sort(a)
    print(inv_count)
