import matplotlib.pyplot as plt

def react(a,b,c,k1,k2,end_time,dt):
    substance_a = []
    substance_b = []
    substance_c = []
    time_points = []
    time = 0
    while time <= end_time :
        substance_a.append(a)
        substance_b.append(b)
        substance_c.append(c)
        time_points.append(time)
        time += dt
        
        a += (k2 * c - k1 * a * b) * dt
        b += (k2 * c - k1 * a * b) * dt
        c += (2 * k1 * a * b - 2 * k2 * c) * dt
        
        plt.clf()
        plt.title("Chemical reactor simulation")
        plt.plot(time_points, substance_a, label = "Substance A")
        plt.plot(time_points, substance_c, label = "Substance C")
        plt.plot(time_points,substance_b,label = "Substance B")
        
        plt.grid()
        plt.legend()
        plt.xlabel("Time (s)")
        plt.ylabel("Quantity (gm)")
        plt.pause(0.01)
    plt.show()


def main():
    react(100,50,0,0.008,0.002,10,0.1)
    
if __name__ == "__main__":
    main()