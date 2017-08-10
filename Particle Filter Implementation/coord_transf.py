import math
from decimal import Decimal

def car_to_particle_frame(xp, yp, theta, x0, y0):
    xm = x0 + math.cos(theta) * xp + math.sin(theta) * yp
    ym = y0 - math.sin(theta) * xp + math.cos(theta) * yp

    return xm, ym

def multivariate_gaussian_distribution(x, y, mx, my, sigma_x, sigma_y):
    term1 = math.pow(x-mx, 2) / (2 * math.pow(sigma_x, 2))
    term2 = math.pow(y-my, 2) / (2 * math.pow(sigma_y, 2))

    return (1/(2 * math.pi * sigma_x * sigma_y)) * math.exp(-(term1 + term2))

def multivariate_gaussian_distribution2(x, y, mx, my, sigma_x, sigma_y):
    term1 = ((x-mx) * (x-mx)) / (2 * sigma_x * sigma_x)
    term2 = ((y-my) * (y-my)) / (2 * sigma_y * sigma_y)
    exp_term = math.exp(-(term1 + term2))
    return (1/(2 * math.pi * sigma_x * sigma_y)) * exp_term

theta = math.pi / 2

x0 = 4
y0 = 5
xp = 2
yp = 2
print(car_to_particle_frame(xp, yp, theta, x0, y0))

xp = 3
yp = -2
print(car_to_particle_frame(xp, yp, theta, x0, y0))

xp = 0
yp = -4
print(car_to_particle_frame(xp, yp, theta, x0, y0))

p_obs1 = multivariate_gaussian_distribution2(6, 3, 5, 3, 0.3, 0.3)
p_obs2 = multivariate_gaussian_distribution2(2, 2, 2, 1, 0.3, 0.3)
p_obs3 = multivariate_gaussian_distribution2(0, 5, 4, 7, 0.3, 0.3)

print(p_obs1)
print(p_obs2)
print(p_obs3)

print(p_obs1 * p_obs2 * p_obs3)




