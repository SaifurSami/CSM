import matplotlib.pyplot as plt 
import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def BEZ(k, n, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n - k))

def bazier_curve(X,Y):
    points_X = []
    points_Y = []
    u = 0
    e = 0.01
    new_x = X[0]
    new_y = Y[0]
    n = len(X)-1

    while(u<1.01):
        points_X.append(new_x)
        points_Y.append(new_y)

        plt.clf()
        plt.title("Bazier curve")
        plt.plot(X,Y,label = "COntrol poins")
        plt.plot(points_X,points_Y, label = "Bazier Curve")
        plt.legend()
        plt.pause(.01)

        new_x, new_y = 0,0
        u+=e

        for k in range(0,len(X)):
            new_x += X[k]*BEZ(k,n,u)
            new_y += Y[k]*BEZ(k,n,u)
        
    plt.show()

    
def main():
    control_points_X = [1,7,15,21]
    control_points_Y = [5,10,5,10]
    bazier_curve(control_points_X, control_points_Y)

if __name__ == "__main__":
    main()