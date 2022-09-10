import numpy as np

def fix(v):
    return np.around(v, decimals=10)


def main(args):
    
    FACTOR = 0.000001

    f = open('post/lc'+str(args[1])+'.csv', 'r')
    d = f.read()
    f.close()
       
    f = open('post/lc1697.csv', 'r')
    z = f.read()
    f.close()

    d = d.split('\n')
    z = z.split('\n')

    for i in range(1, len(d)-1):
        lo = d[i].split(',')
        lf = z[i].split(',')
        
        vo = np.double(lo[1])
        vf = np.double(lf[1])
        
        vo = fix((vo * FACTOR)) + 1
        vf = fix(vf * FACTOR)

        lo[1] = str(vo)
        lo[2] = str(vf)

        d[i] = ','.join(lo)
    
    d = "\n".join(d)

    f = open('post/post_lc'+str(args[1])+'.csv', 'w')
    f.write(d)
    f.close()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
