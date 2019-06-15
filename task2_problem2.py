from time import sleep
import numpy as np

if __name__ == "__main__":
    size = long(raw_input())
    n = long(raw_input())
    s = []
    t = [1]*size
    z = [0]*size
    for i in range(size):
        s.append(i+1)
    a = np.array(s)
    for i in range(n):
         s1 = raw_input().rstrip().split()
         L, R, v = s1
         L, R, v =int(L), int(R), int(v)
         a+= np.array(z[:L-1]+t[L-1:R]+z[R:])*v
    s = list(a)
    print max(s)
    sleep(5)
