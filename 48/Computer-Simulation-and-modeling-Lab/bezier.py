import matplotlib.pyplot as plt

def factorial(n):
    if(n):
        return factorial(n - 1) * n
    else:
        return 1
    
def ncr(n,k):
    return factorial(n) / float(factorial(k) * factorial(n - k))
def Bez(k,n,u):
    ans = (u ** k) * ncr(n,k) * ((1 - u) ** (n - k))
    return ans

def draw_bezier(x_control_points, y_control_points):
    n = len(x_control_points) - 1
    eps = 0.01
    x_curve_points = []
    y_curve_points = []
    u = 0
    while(u < 1.01):
        x = 0
        y = 0
        for k in range(0,len(x_control_points)):
            bz = Bez(k,n,u);
            x = x + bz * x_control_points[k];
            y = y + bz * y_control_points[k];
        x_curve_points.append(x)
        y_curve_points.append(y)
        u += eps
        
        plt.clf()
        plt.title("Bezier curve")
        plt.plot(x_control_points,y_control_points,label = "Control graph")
        plt.plot(x_curve_points,y_curve_points, label = "Bezier curve")
        plt.legend(frameon=True, framealpha=1, edgecolor='red', facecolor='white')
        plt.grid()
        plt.pause(0.001)
    plt.show()    


def main():
    x_control_points = [1, 7, 15, 21]
    y_control_points = [5, 10, 5, 10]
    draw_bezier(x_control_points, y_control_points)

if __name__ == "__main__":
    main()