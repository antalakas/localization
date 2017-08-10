#Program a function that returns a new distribution
#q, shifted to the right by U units. If U=0, q should
#be the same as p.

p=[0, 1, 0, 0, 0]

def move(p, U):
    q = []
    for i in range(len(p)):
        print('U: {}, len(p): {}, i: {}, i-U: {}, index: {}'.format(U, len(p), i, i-U, (i-U) % len(p)))
        q.append(p[(i-U) % len(p)])
    return q

print(move(p, 1))
print(move(p, 2))
print(move(p, 3))
print(move(p, 4))
print(move(p, 5))
