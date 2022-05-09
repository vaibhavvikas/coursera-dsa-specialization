def max_pairwise_product(numbers):
    n = len(numbers)
    if n < 3:
        return numbers[0]*numbers[1]

    max_num, second_max_num = numbers[0], numbers[0]

    if numbers[1] > max_num:
        max_num = numbers[1]
    else:
        second_max_num = numbers[1]

    for i in range(2, n):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max_num:
            second_max_num = numbers[i]

    return max_num*second_max_num


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
