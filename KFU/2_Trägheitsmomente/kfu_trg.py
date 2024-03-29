from math import pi
from math import sin
from math import log
from math import sqrt
import matplotlib.pyplot as plt


def get_direktionsmoment(Iprime,Delta_Iprime,k,Delta_k):
    D_r = 4.0*pi*Iprime/k
    Delta_D_r = 4*pi*(Delta_Iprime/k + Iprime/k**2 * Delta_k)
    print("Direktionsmoment: ")
    print(str(round(D_r * 10**6,2)) + " +- " + str(round(Delta_D_r * 10**6,2)) + str(" microNm"))
    return D_r, Delta_D_r

def get_traegheitsmoment(k,Delta_k, d,Delta_d, Iprime, Delta_Iprime):
    I = d/k*Iprime
    Delta_I = Delta_d/k*Iprime  + d/k**2 *Iprime*Delta_k + d/k*Delta_Iprime
    print("Traegheitsmoment: ")
    print(str(round(I*10**6,2)) + " +- " + str(round(10**6 *Delta_I,2)) + " mg m^2")
    return I, Delta_I

def get_daempfung(A0,A1,t,delta_A,delta_t):
    gamma = log(A0/A1)/t
    delta_gamma = delta_A/t * (1/A0 + 1/A1) + gamma/t*delta_t
    print("Daempfung: " + str(round(gamma*1000,8)) + " +- " + str(round(delta_gamma*1000,8)) +" ms^-1")
    return gamma

def get_kennfrequenz(D_r, I, Delta_D_r, Delta_I):
    omega0 = sqrt(D_r/I)
    Delta_omega_0 = 0.5/(omega0*I)  * ( Delta_D_r + D_r/I * Delta_I)
    print("Kennfrequenz: " + str(omega0) + " +- " + str(Delta_omega_0) + " s^-1")
    print(D_r)

def regression(x,y):
    d, k = regression_algo(x,y)
    Delta_d, Delta_k = regression_fehler(x,y)
    return d,k,Delta_d,Delta_k

def regression_algo(x,y):
    xd = sum(x)/len(x)
    yd = sum(y)/len(y)
    zaehler = 0
    nenner = 0
    for i in range(len(x)):
        zaehler += (x[i] - xd) * (y[i] - yd)
        nenner += (x[i] - xd)**2
    k = zaehler / (1.0 * nenner)
    d = yd - k * xd
    return d, k

def regression_fehler(x,y):
    d = [0,0,0]
    k = [0,0,0]
    d[0], k[0] = regression_algo( [x[0],x[1]], [y[0],y[1]] )
    d[1], k[1] = regression_algo( [x[0],x[2]], [y[0],y[2]] )
    d[2], k[2] = regression_algo( [x[1],x[2]], [y[1],y[2]] )
    return spannweite(d)/2, spannweite(k)/2

def spannweite(data):
    return max(data) - min(data)

def plot_regression(n, t):
    t2 = [var**2 for var in t]
    d,k, Delta_d, Delta_k = regression(n,t2)

    x = [n[0],n[2]]
    y = [d,d+4*k]

    plt.scatter(n,t2)
    plt.plot(x,y)
    plt.xlabel("Anzahl Batterien")
    plt.ylabel("Quadrierte Zeit / s^2")
    #plt.show()
    plt.savefig("regression.png")
    plt.close()
    return d,k,Delta_d,Delta_k



def show_plot(t, omega):
    plt.plot(t,omega)
    plt.xlabel("Zeit / t")
    plt.ylabel("")
    plt.show()
    #plt.savefig("regression.png")
    plt.close()
    return d,k,Delta_d,Delta_k



#die mittlere Seite schaut in Drehrichtung
a_iphone = 7.7/1000.0 #kuerzeste seite
b_iphone = 157.5/1000.0 #laengste seite
m_iphone = 0.208


h_batterie = 44.5/1000.0
r_batterie = 5.25/1000.0
m_batterie = 11/1000.0

delta_l = 0.1/1000
delta_r = delta_l
delta_b = delta_l
delta_m = 0.1/1000

delta_A = 2*pi/360.0 * 5 #amplitude
delta_t = 1/1000.0

print("Traegheitsmoment der nach aussen verschobenen Batterie: ")
Iprime = 0.25 * m_batterie * (6*r_batterie**2 + 4*b_iphone*r_batterie + b_iphone**2)
Delta_Iprime = 0.25* (delta_m * (6*r_batterie**2 + 4*b_iphone*r_batterie + b_iphone**2)  + m_batterie*(12*r_batterie + 4*b_iphone)*delta_r + m_batterie*(4*r_batterie + 2*b_iphone)*delta_b)
print(str(round(Iprime*10**6,2)) + " +- " + str(round(Delta_Iprime*10**6,2)) + " mg m^2")



n = [0,2,4] # 0, 2 und 4 Batterien
t = [17.6, 27.8, 32.5]
d,k,Delta_d,Delta_k = plot_regression(n,t)

#Amplitude
A_0 = 10 * 2 * pi
A_1 = 8.4 * 2 * pi
t_daempfung = 17.7



print("")
print("Regression:")
print("k: " +str(k))
print("d: " +str(d))

print("")
print("Regression Fehler:")
print("Delta k: " + str(Delta_k))
print("Delta d: " + str(Delta_d))


print("")
D_r, Delta_D_r = get_direktionsmoment(Iprime,Delta_Iprime,k,Delta_k)

print("")
I, Delta_I = get_traegheitsmoment(k, Delta_k, d, Delta_d,Iprime, Delta_Iprime)

print("")
gamma = get_daempfung(A_0,A_1,t_daempfung,delta_A,delta_t)

print("")
print("Direkte Berechnung des Traegheitsmoments eines iPhones:")
I_direkt = 1/12.0 * m_iphone * (a_iphone**2 + b_iphone**2)
Delta_I_direkt = 1/12.0 * ( delta_m * (a_iphone**2 + b_iphone**2) + 2*m_iphone*(a_iphone*delta_l + b_iphone*delta_l)  )
print(str(round(I_direkt*10**6,2)) + " +- " + str(round(Delta_I_direkt*10**6,2)) + " mg m^2")

print("")
get_kennfrequenz(D_r, I, Delta_D_r, Delta_I)


t = [1.0/1000 * i for i in range(150000)]
