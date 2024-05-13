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

import matplotlib.pyplot as plt
import numpy
from matplotlib.patches import Ellipse 


plt.title("Euclidis Elementorum")
ellipse=Ellipse(xy=(-1,0),width=2*2,height=2*2,angle=0,fill=False,color='g')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(1,0),width=2*2,height=2*2,angle=0,fill=False,color='y')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(0,0),width=1*2,height=1.73205*2,angle=0,fill=False,color='r')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(0,0),width=0.866025*2,height=0.866025*2,angle=0,fill=False,color='r')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(0,1.73205),width=1.5*2,height=1.5*2,angle=0,fill=False,color='b')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(0,-1.73205),width=1.5*2,height=1.5*2,angle=0,fill=False,color='b')
plt.gcf().gca().add_artist(ellipse)
ellipse=Ellipse(xy=(0,1.73205),width=0.866025*2,height=0.866025*2,angle=0,fill=False,color='r')
plt.gcf().gca().add_artist(ellipse)
plt.plot([-1,1],[0,0])
plt.plot([-1,0],[0,1.73205])
plt.plot([1,0],[0,1.73205])
plt.plot([-1,0],[0,-1.73205])
plt.plot([1,0],[0,-1.73205])
plt.plot([0,0.75],[0,0.4330127])
plt.plot([0,0.75],[0,-0.4330127])
plt.plot([0,0],[-4,4])
plt.text(-1.5,0,"A")
plt.text(1.2,0,"B")
plt.text(0.1,2,"C")
plt.text(0.1,-2.2,"D")
plt.text(0.1,0.1,"E")
plt.text(0.75,0.4330127,"F")
plt.text(0.75,-0.4330127,"G")
plt.text(0.1,0.866025,"H")
plt.text(-3.5,0,"J")
plt.text(3.1,0,"K")
plt.annotate('proposition one', xy=(2,2), xytext=(3,3.5),arrowprops=dict(facecolor='yellow', shrink=0.05),)
plt.text(-3,-4,r'$a^2+b^2=c^2,a^n+b^n≠c^n,n>2$',fontsize=14,color='b')
plt.axis('equal')
plt.show()

#命题I.1已知一条线段可以作一个等边三角形。[插图]
#如果：AB为已知的线段。那么：以线段AB为边作一个等边三角形。
#以A为圆心、AB为半径作圆BCJ；再以B为圆心、以BA为半径作圆ACK；两圆相交于C点，连接CA、CB。
#因为：A点是圆BCJ的圆心，所以，CA等于AB（定义I.15）。又因为，点B是圆ACK的圆心，所以，CB等于BA（定义I.15）；
#因为：等于同量的量互相相等（公理I.1）；所以：线段CA等于CB等于AB。
#因为：三条线段CA、AB、CB相等。所以：三角形ABC是建立在线段AB上的等边三角形。证完
