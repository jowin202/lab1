from math import exp
from math import pi


g = 9.81

V0 = 0.011

m = 16.73/1000
delta_m = 0.05/1000

d = 16.015/1000
delta_d = 0.002/1000

h = 353
delta_h = 10

p0 = 100800
delta_p0 = 20


p = p0*exp(-h/8000.0) + 4*m*g/(d**2 * pi)
delta_p = exp(-h/8000.0) * (delta_p0 + p0*delta_h/8000.0) + 4*g/(d**2 * pi)*(delta_m + 2*m*delta_d/d)


print(p)
print(delta_p)

A = 64*V0/(d**4 *p)
print(A)

B = delta_m + 4*m *delta_d/d + m*delta_p/p
print(B)

print(2*m)

C = A*2*m
print("C: " + str(C))

D = B/(2*m)
print("D: " +str(D))



delta_tau = 0.1/5
tau = 1.15
print("kappa: " + str(64 * m * V0/(d**4 * p * tau**2)))

print("delta kappa: " + str(C/tau**2 * (D + delta_tau/tau)))
