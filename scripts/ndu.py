import numpy as np
import math
import time

BUFFER = []

def fix(v):
    return np.around(v, decimals=10)

def interna(ti, nu, a, phi, TWOPI):
    
    nu  = np.double(nu * 0.000001)
    a   = np.double(a)
    phi = np.double(phi)

    v = (TWOPI * nu * ti) + phi
    v = np.sin(v)
    v = a * v
    return fix(v)

def sumatoria(param, TWOPI):
    
    j = 0
    for l in param:
        FT = time.time()
        
        j = j+1 
        nu  = l[0]
        a   = l[1]
        phi = l[2]
    
        res = "#time,flux,flux_err\n"
        for i in range(len(BUFFER)):
            z   = interna(BUFFER[i][0], nu, a, phi, TWOPI)
            BUFFER[i][2] = fix(BUFFER[i][2] + z)
            FI = BUFFER[i][1] - BUFFER[i][2]
            res = res + str(BUFFER[i][0]) + ',' + str(fix(FI)) + ",0.0\n"
        
        makeFile(j, res)
        print(j, time.time()-FT)
        
def makeFile(j, res):
    
    f = open("output/lc" + str(j) + ".csv", 'w')
    f.write(res)
    f.close()

def ejecutar(flux, param):
    
    TWOPI = np.pi * 2

    i = 0
    for l in flux:

        ti = np.double(l[0])
        fi = np.double(l[1])
        BUFFER.append([ti, fi, np.double(0)])

    sumatoria(param, TWOPI)

    return 0

def main(args):
    f = open("input/flux.csv", 'r')
    flux = f.read()
    f.read()

    f = open("input/param.csv", 'r')
    param = f.read()
    f.close()

    flux = flux.split("\n")
    mflux = []
    for l in flux:
        if(l != ''):
            tmp = []
            for p in l.split(','):
                tmp.append(float(p))
            mflux.append(tmp)
    del(flux)

    param = param.split("\n")
    mparam = []
    for l in param:
        if(l != ''):
            tmp = []
            for p in l.split(','):
                tmp.append(float(p))
            mparam.append(tmp)
    del(param)

    ejecutar(mflux, mparam)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
