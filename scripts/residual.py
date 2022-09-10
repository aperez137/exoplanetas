import re

print("Convert from 'input/Residual.dat' to 'input/residual.csv'")

f = open("input/Residuals1.dat", 'r')
d = f.read()
f.close()

d = re.sub(" +", ',', d)
d = re.sub("^,", '', d, flags=re.MULTILINE)
d = d.split("\n")

param =""

for l in d:
    p = l.split(",")
    if(len(p) > 1):
        param = param + p[0] + ',' + p[1] + ',' + p[2] + "\n"

f = open("input/residual.csv", 'w')
f.write(param)
f.close()

print("\nReady!.")
