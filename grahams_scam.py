import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def distance(p, q):
    return math.sqrt((q[1] - p[1])**2 + (q[0] - p[0])**2)

def bottommost_point(points):
    return min(points, key=lambda p: (p[1], p[0]))

def graham_scan(points):
    p0 = bottommost_point(points)
    points.sort(key=lambda p: (math.atan2(p[1] - p0[1], p[0] - p0[0]), distance(p0, p)))
    hull = [p0, points[0], points[1]]
    for i in range(2, len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    return hull

points = [(0, 0), (4, 4), (1, 1), (3, 1), (5, 0), (3, 3), (2, 4)]
hull = graham_scan(points)
print(hull)
