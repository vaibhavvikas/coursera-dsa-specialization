def return_mid(low, high):
    return low + (high-low)//2

low, high = map(int, (input("Enter low and high with a space between them: ").split()))
mid = return_mid(low, high)
print(mid)

while high>low:
    n = int(input(f"Type 0 for less than {mid} and 1 for greater than {mid}: "))
    if n == 0:
        high = mid - 1
    else:
        low = mid + 1
    mid = return_mid(low, high)
    print(mid)
