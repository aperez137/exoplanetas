from decimal import *
import re

getcontext().prec = 30

FIX = Decimal('0.0000000001')
SEC = Decimal('86400')

print("Convert from 'input/flux_in.dat' to 'input/flux.csv'")

f = open("input/flux_in.dat", 'r')
d = f.read()
f.close()

d = re.sub(" +", ',', d)
d = re.sub("^,", '', d, flags=re.MULTILINE)
d = d.split("\n")

flux =""

for l in d:
    p = l.split(",")
    if(len(p) > 1):
        seg = Decimal(p[0]) * SEC
        seg = seg.quantize(FIX)
        flux = flux + str(seg) + ',' + p[1] + ',0.0\n'

f = open("input/flux.csv", 'w')
f.write(flux)
f.close()

print("\nReady!.")
