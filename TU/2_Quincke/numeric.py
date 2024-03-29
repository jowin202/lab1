t = [x/1000 for x in [0.825, 0.585, 0.805, 0.605]]
rho = [8635, 2700, 8900, 7800]

delta_l = 0.004

delta_t = 10**-4

for i in t:
    print(str(3/i) + "  " + str(delta_l/i + delta_t* 3/i**2))
    
    
print("")

for i in range(4):
    time = t[i]
    c = 3/time
    delta_c = delta_l/time + delta_t* 3/time**2
    print(str(c**2 * rho[i]/10**9) + "  " + str(2*c*delta_c*rho[i]/10**9))
