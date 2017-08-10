p = [0.2, 0.2, 0.2, 0.2, 0.2]
# p = [1, 0 ,0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s += pUndershoot * p[(i - U - 1) % len(p)]
        s += pOvershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q

# for j in range(1000):
#     p = move(p, 1)
#
# print p

# p = sense(p, 'red')
# p = move(p, 1)
# p = sense(p, 'green')
# p = move(p, 1)

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print p

from math import *

# gaussian
def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print f(10.,4.,10.) #Change the 8. to something else!

def update(mean1, var1, mean2, var2):
    new_mean = ((var2 * mean1) + (var1 * mean2)) / (var1 + var2)
    new_var = 1 / ((1/var1 ) + (1/var2))
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

# print predict(10., 4., 12., 4.)
#
# print update(10., 4., 12., 4.)
#
# print update(10., 8., 13., 2.)

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for mes, mot in zip(measurements, motion):
    [mu, sig] = update(mu, sig, mes, measurement_sig)
    print('update   ', mu, sig)
    [mu, sig] = predict(mu, sig, mot, motion_sig)
    print('predict  ', mu, sig)

print [mu, sig]