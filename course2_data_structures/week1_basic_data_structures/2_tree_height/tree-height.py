# python3
import sys, os
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:

    def __init__(self, parent):
        self.create_tree(parent)

    def create_tree(self, parent):
        self.tree = {}
        for i, node in enumerate(parent):
            if node not in self.tree:
                self.tree[node] = [i]
            else:
                self.tree[node].append(i)

    def get_height(self):
        if -1 not in self.tree:
            return -1
        return self.compute_height(self.tree[-1][0])

    def compute_height(self, node) -> int:
        if node not in self.tree:
            return 0

        max_height = 0
        for each in self.tree[node]:
            max_height = max(max_height, self.compute_height(each))

        return 1 + max_height


def unittest():
    loc = "course2_data_structures\\week1_basic_data_structures\\2_tree_height\\tests\\"
    files = os.listdir(loc)
    files = [each for each in files if not each.endswith(".a")]
    input, output = None, None
    for each in files:
        with open(loc + each, "r") as f:
            next(f)
            input = f.readline().rstrip()
            parent = list(map(int, input.split()))

        with open(loc + each + ".a", "r") as f:
            output = f.readline().rstrip()

        assert(1 + TreeHeight(parent).get_height()) == int(output)

    print("All test cases passed")


def main():
    # unittest()
    _ = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    n_tree = TreeHeight(parent)
    print(1 + n_tree.get_height())


threading.Thread(target=main).start()
