import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse 
ellipse=Ellipse(xy=(1,1),width=2*2,height=1.4142*2,angle=45,fill=False,color='r')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(1,1),width=2*2,height=2*2,angle=45,fill=False,color='g')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(1,1),width=1.4142*2,height=1.4142*2,angle=45,fill=False,color='g')
plt.gcf().gca().add_artist(ellipse)
plt.plot([0,2,2,0],[0,0,2,0])
plt.plot([-2,0,],[-2,0],'--g')
plt.plot([2,4],[2,4],'--g')
plt.plot([0,1,2,2.4138],[0,1,2,2.4138],'go')
plt.plot([0,0,-2,2],[0,4,2,2],'--')
plt.plot([2,2,-2,-2,0],[2,4,4,0,0],'--')
plt.plot([2,0,-2,0],[2,4,2,0],'--')
plt.text(-0.3,-0.3,'A(0,0)')
plt.text(2.2,-0.2,'C(2,0)')
plt.text(2.2,2,'B(2,2)')
plt.text(1.2,1,"O(1,1)")
plt.text(2.6138,2.4138,'D(2.4138,2.4138)')
plt.text(-5,-3,r'$a^2+b^2=c^2,n<=2$',fontsize=14,color='g')
plt.text(-5,-4,r'$a^n+b^n≠c^n,n>2$',fontsize=14,color='g')
plt.title('Hugo zhusixian ploting ')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.axis('equal')
plt.axis([-15,15,-15,15])
plt.show()

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
