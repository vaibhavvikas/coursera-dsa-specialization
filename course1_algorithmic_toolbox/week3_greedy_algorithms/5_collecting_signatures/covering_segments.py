# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda x: x[1])
    n = len(segments)
    while n>0:
        s = segments[0]
        points.append(s.end)
        segments = [Segment(x[0], x[1]) for x in segments if x[0] > s.end]
        n = len(segments)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
