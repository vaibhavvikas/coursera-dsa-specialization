known_loc = {}


def binary_search_algo(keys, low, high, query):
    if high >= low:
        mid = low + (high-low)//2

        if keys[mid] == query:
            if keys[mid-1] == query:
                return binary_search_algo(keys, low, mid-1, query)
            global known_loc
            known_loc[query] = mid
            return mid

        elif keys[mid] > query:
            return binary_search_algo(keys, low, mid - 1, query)

        else:
            return binary_search_algo(keys, mid + 1, high, query)

    known_loc[query] = -1
    return -1


def binary_search(n, keys, query):
    global known_loc
    if query in known_loc:
        return known_loc[query]
    return binary_search_algo(keys, 0, n, query)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(num_keys-1, input_keys, q), end=' ')
