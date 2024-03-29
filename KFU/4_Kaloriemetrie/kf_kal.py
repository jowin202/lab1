from math import pi

def get_c_A(m_A,m_B,T_A,T_B,T_M,C_th):
    global c
    return (c*m_B + C_th)*(T_M-T_B)/(m_A*(T_A-T_M))

def get_delta_c_A(m_A,m_B,T_A,T_B,T_M,C_th,Delta_C_th,c_A):
    global c_B
    global Delta_c
    global delta_m
    global delta_T
    res = 0

    res += Delta_C_th*abs(T_M-T_B)/(m_A*abs(T_A-T_M)) # C_th
    res += c_B*delta_m * abs(T_M-T_B)/(m_A*abs(T_A-T_M)) # m_B
    res += (c_B*m_B +C_th)*delta_T/(m_A * abs(T_A-T_M)) # T_MB
    res += (c_B*m_B +C_th)*abs(T_M-T_B)*delta_T/(m_A * abs(T_A-T_M)**2) # T_AM
    res += (c_B*m_B +C_th)*abs(T_M-T_B)*delta_m/(m_A**2 * abs(T_A-T_M)) # m_A
    res += Delta_c*m_B*abs(T_M-T_B)/(m_A*abs(T_A-T_M))

    return res



c = 4200 # J / (kg K)
Delta_c = 0.5

c_A = c
c_B = c

m_A = 0.5
m_B = 0.5

T_A = 54
T_B = 82
T_M = 71

delta_m = 1/1000 # 1g
delta_T = 1/2 # 1K


C_th = (c_A*m_A*(T_A-T_M) + c_B*m_B*(T_B-T_M))/(T_M-T_B)


print("Kapazitaet Thermoskanne: " + str(C_th))

Delta_C_th = 0
Delta_C_th += c*delta_m*abs(T_A-T_M)/abs(T_M-T_B) #m_A
Delta_C_th += c*delta_m #m_B
Delta_C_th += c*delta_T*m_A/abs(T_M-T_B) #T_AM
Delta_C_th += c*delta_T* m_A*abs(T_A-T_B)/abs(T_M-T_B)**2
Delta_C_th += Delta_c*m_B + Delta_c*m_A*abs(T_A-T_M)/abs(T_B-T_M)


print("Unsicherheit: " + str(Delta_C_th))





m_A1 = 87/1000
m_A2 = 39/1000
m_B = 100/1000

T_A1 = 4
T_A2 = 4

T_B1 = 85
T_B2 = 88

T_M1 = 83
T_M2 = 87

c_A1 = get_c_A(m_A1,m_B,T_A1,T_B1,T_M1,C_th)
c_A1_delta = get_delta_c_A(m_A1,m_B,T_A1,T_B1,T_M1,C_th, Delta_C_th, c_A1)

print("Kapazitaet A1: " + str(c_A1))
print("Unsicherheit A1: " + str(c_A1_delta))


c_A2 = get_c_A(m_A2,m_B,T_A2,T_B2,T_M2,C_th)
c_A2_delta = get_delta_c_A(m_A1,m_B,T_A2,T_B2,T_M1,C_th, Delta_C_th, c_A2)

print("Kapazitaet A2: " + str(c_A2))
print("Unsicherheit A2: " + str(c_A2_delta))

print("")
print("")
print("")




r = 2.5/100
h = 26.0/100
wandstaerke = 2.0/10000
oberflaeche = 2*r*pi*h + 2*r**2*pi
volumen = oberflaeche*wandstaerke
dichte = 7874 # wikipedia # si-einheiten
masse = volumen * dichte
c_eisen = 449 # wikipedia # si-einheiten
wkap_eisen = masse * c_eisen


print("Oberflaeche der Thermoskanne: " + str(oberflaeche*10000) + " cm^2")
print("Volumen des Materials der Thermoskanne: " + str(volumen*1000000) + " cm^3")
print("Masse der Thermoskanne: " + str(masse*1000) + " g")
print("Theoretische Kapazitaet der Thermoskanne: " + str(wkap_eisen))
