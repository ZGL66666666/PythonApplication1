import matplotlib.pyplot as plt
import numpy as np


for a in range(11):        #  t = 2*n - 1 = m*m   
    for b in range(21):
        for c in range(21):
            if a != 0 and b != 0 and c != 0 and a + b > c and b + c > a and a + c > b and  a ** 2 + b ** 2 == c ** 2： # Pythagoras
                 p = ( a + b + c ) * ( 1 / 2 ) ; s = ( p * ( p - a ) * ( p - b ) * ( p - c ) ) ** ( 1 / 2 ) ;        # Heron of Alexandria
                 print('{:10}{:10}{:10}{:10}'.format(a,b,c,s)) ;
                 print("."*40)

for n in range(2,50):  #  s != 0  t != m*m*m  Any cube  and Any number of cubes   n**q = [(n**3)*(n)**(q-3)]*1**3   # Pierre de Fermat
    t = (n**3 - (n-1)**3)  #t = (3*n*n - 3*n + 1)                                              # integer    odd number    prime number
    s = (n-1)**3 - (n**3 - (n-1)**3)
    #if s > 0:
    print(n,n**3,(n-1)**3,t,s)
    
n=np.arange(0.0,6.0,0.001)
t=np.sqrt(2*n-1) #(2*n-1)**(1/2)
t1=(3*n*n-3*n+1)**(1/3)
#s=n*n*n-6*n*n+6*n-2
#plt.plot(n,s)
plt.plot(n,t)
plt.plot(n,t1)
plt.plot([0,6],[0,0])
plt.grid()
plt.show()




