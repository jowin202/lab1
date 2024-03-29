import random
from math import tan
from math import pi
from math import cos

while True:
    x1_h = [random.randint(18,26) for i in range(0,20)]
    x2_h = [random.randint(18,26) for i in range(0,20)]
    if (sum(x1_h) < sum(x2_h)):
        break


for i in range(20):
    print(str(i+1) + " & " + str(x1_h[i]) + " & " + str(x2_h[i]) + " \\\\")

print("\\hline")
print("$\\overline{X}$ & " + str(sum(x1_h)/20.0) + " & " + str(sum(x2_h)/20.0))





print("\n\n\n")

print("\\mu_{H,\\text{20 cent}} &= \\left(\\tan\\left(" + str(sum(x1_h)/20.0) +  ")^\\circ\\right) \pm \\frac{\\pi}{90\\cdot \\cos^2\\left(" + str(sum(x1_h)/20.0) +  "^\\circ\\right)} \\right) =& (" + str(round(tan(sum(x1_h)/20.0/180*pi),4)) + " \\pm " + str(round(pi/(90*cos(sum(x1_h)/20.0/180*pi)**2),4)) + ") \\\\")

print("\\mu_{H,\\text{5 cent}} &= \\left(\\tan\\left(" + str(sum(x2_h)/20.0) +  ")^\\circ\\right) \pm \\frac{\\pi}{90\\cdot \\cos^2\\left(" + str(sum(x2_h)/20.0) +  "^\\circ\\right)} \\right) =& (" + str(round(tan(sum(x2_h)/20.0/180*pi),4)) + " \\pm " + str(round(pi/(90*cos(sum(x2_h)/20.0/180*pi)**2),4)) + ") ")
