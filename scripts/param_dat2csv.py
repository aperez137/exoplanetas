import re

print("Convert from 'input/param_in.dat' to 'input/param.csv'")

f = open("input/param_in.dat", 'r')
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

f = open("input/param.csv", 'w')
f.write(param)
f.close()

print("\nReady!.")