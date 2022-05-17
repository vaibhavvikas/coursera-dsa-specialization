# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if len(opening_brackets_stack) < 1:
                return str(i + 1)
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return str(i + 1)

    if len(opening_brackets_stack) > 0:
        return str(opening_brackets_stack[-1].position + 1)

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

def unittest():
    loc = "course2_data_structures\\week1_basic_data_structures\\1_brackets_in_code\\tests\\"
    files = os.listdir(loc)
    files = [each for each in files if not each.endswith(".a")]
    input, output = None, None
    for each in files:
        with open(loc + each, "r") as f:
            input = f.readline().rstrip()
        
        with open(loc + each + ".a", "r") as f:
            output = f.readline().rstrip()

        assert(find_mismatch(input)) == (output)
    
    print("All test cases passed")


if __name__ == "__main__":
    main()
    #unittest()
