from decimal import *
import math

getcontext().prec = 30
FIX   = Decimal('0.0000000001')

def pi():
    
    getcontext().prec += 2  
    three = Decimal(3)      
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24

    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t

    getcontext().prec -= 2

    return +s              

def sin(x):
    
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1

    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign

    getcontext().prec -= 2
    return +s

def interna(ti, nu, a, phi, TWOPI):
    
    ti  = Decimal(ti)
    nu  = Decimal(nu * 0.000001)
    a   = Decimal(a)
    phi = Decimal(phi)

    v = (TWOPI * nu * ti) + phi
    v = Decimal(math.sin(v))
    v = a * v
    return v.quantize(FIX)

def sumatoria(ti, param, lim, TWOPI):

    S = Decimal(0)

    for i in range(lim):
        l   = param[i]
        nu  = l[0]
        a   = l[1]
        phi = l[2]

        z   = interna(ti, nu, a, phi, TWOPI)
        
        S   = S + z

    return S.quantize(FIX)

def ejecutar(flux, param, limit):
    
    TWOPI = Decimal(2*pi())

    res = "#time,flux,flux_err\n"

    i = 0
    for l in flux:

        ti = Decimal(l[0]).quantize(FIX)
        fi = Decimal(l[1])

        S = sumatoria(ti, param, limit, TWOPI)
        FI = fi - S
        FI = FI.quantize(FIX)

        res = res + str(ti) + ',' + str(FI) + ",0.0\n"
        
        i = i+1
        #print('...'+str(i))

    f = open("output/lc" + str(limit) + ".csv", 'w')
    f.write(res)
    f.close()

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

    ejecutar(mflux, mparam, int(args[1]))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
