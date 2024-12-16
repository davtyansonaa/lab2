def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []

    leftmost = min(points, key=lambda p: p[0])

    hull = []
    p = leftmost

    while True:
        hull.append(p)
        next_point = points[0]
        for q in points[1:]:
            if next_point == p or orientation(p, next_point, q) == 2:
                next_point = q
        p = next_point
        if p == leftmost:
            break

    return hull

