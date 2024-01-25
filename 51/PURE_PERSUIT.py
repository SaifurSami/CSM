import matplotlib.pyplot as plt
import numpy as np

def pure_persuit(xb,yb,xf,yf,vf):
    T = 0
    XF = []
    YF = []
    caught_distance = 10

    while(True):
        XF.append(xf)
        YF.append(yf)

        plt.clf()
        plt.title("Pure Persuit Problem")
        plt.plot(XF, YF, marker = "o", label = "Fighter")
        plt.plot(xb[0:T+1], yb[0:T+1], marker = "o", label = "Bomber")
        plt.xlim(0,200)
        plt.ylim(-100,200)
        plt.legend()
        plt.pause(1)

        distance = (((xf-xb[T])**2) +((yf-yb[T])**2) )**.5
        if(distance<caught_distance):
            print(f"The bomber is caught at time {T}")
            break
        elif(T>=len(xb)):
            print(f"The bomber is escaped!!!")
            break
        sin = (yb[T] - yf) / distance
        cos = (xb[T] - xf) / distance
        T+=1
        xf+= vf*cos
        yf+= vf*sin

    plt.show()




def main():
    x_bomber = []
    y_bomber = []
    x_fighter = 0
    y_fighter = 0
    velocity = 20
    with open("./bomberInp.txt") as file:
        for line in file:
            x,y = line.strip().split(',')
            x = int(x)
            y = int(y)
            x_bomber.append(x)
            y_bomber.append(y)
    pure_persuit(x_bomber,y_bomber,x_fighter,y_fighter,velocity)

if __name__=="__main__":
    main()