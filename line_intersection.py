def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  
    return 1 if val > 0 else 2  

def do_intersect(p1, p2, q1, q2):
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0:
        return True
    if o2 == 0:
        return True
    if o3 == 0:
        return True
    if o4 == 0:
        return True

    return False
