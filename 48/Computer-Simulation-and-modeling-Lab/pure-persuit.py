import matplotlib.pyplot as plt


def pure_persuit(boomber_x_cor,boomber_y_cor,xf,yf,v):
    fighter_x_cor = []
    fighter_y_cor = []
    scape,catch = 900,10
    time = 0
    for k in range(0 , len(boomber_x_cor) - 1):
        fighter_x_cor.append(xf)
        fighter_y_cor.append(yf)
        
        plt.clf()
        plt.title("Pure persuit simulation")
        plt.plot(fighter_x_cor,fighter_y_cor, marker = "o",label ="fighter")
        plt.plot(boomber_x_cor[0 : time + 1], boomber_y_cor[0 : time + 1], marker = "o",label = "boomber")
        plt.xlim(-100,200)
        plt.ylim(-100,100)
        plt.legend()
        plt.grid()
        plt.pause(1)
        
        distance = ((boomber_x_cor[time] - xf) ** 2 + (boomber_y_cor[time] - yf) ** 2) ** 0.5
        if(distance <= catch):
            print(f"Target caught at {time} second")
            break
        if(distance >= scape):
            print("Target unfortunately scapped")
            break
        time += 1
        sin = (boomber_y_cor[time] - yf) / distance
        cos = (boomber_x_cor[time] - xf) / distance
        xf += v * cos
        yf += v * sin
    print("Target unfortunately scapped")     



def main():
    boomber_x_cor = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
    boomber_y_cor = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]
    xf,yf = 0,50
    v = 20
    pure_persuit(boomber_x_cor,boomber_y_cor,xf,yf,v)
if __name__ == "__main__":
    main()