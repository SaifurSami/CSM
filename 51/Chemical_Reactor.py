import numpy as np
import matplotlib.pyplot as plt
def Main():
    a0 = float(100) #amount of a = 1 mol
    b0 = float(50) #amount of b = .5 mol
    c0 = float(0.00) #initial c = 0 mol
    T = float(3.0) #total time 100s
    dt = float(.1) # step size = 100/500 cause total time is 100s and 500 steps
    k1 = float(0.008) #rate constsnt = .05
    k2 = float(0.002) #rate constsnt = .05
    t = float(0.00) #initial time

    
    print(" Time\t\t A\t\t B\t\t C")
    print("-----\t\t-----\t\t-----\t\t-----")
    print(f"{t}\t\t{a0}\t\t{b0}\t\t{c0}")
    time_lime = [t]
    A = [a0]
    B = [b0]
    C = [c0]


    while(t<T):
        t=t+dt
        a = a0+((k2*c0-k1*a0*b0))*dt
        b = b0+((k2*c0-k1*a0*b0))*dt
        c = c0+((2*k1*a0*b0)-(2*k2*c0))*dt
        print(f"{t:.2f}\t\t{a:.2f}\t\t{b:.2f}\t\t{c:.2f}")
        time_lime.append(t)
        A.append(a)
        B.append(b)
        C.append(c)
        a0 = a
        b0 = b
        c0 = c
            
    plt.plot(time_lime,A,label='A',color='blue')
    plt.plot(time_lime,B,label='B',color='red')
    plt.plot(time_lime,C,label='C',color='green')
    plt.xlabel("Time")
    plt.ylabel("Amount of A,B,C")
    plt.legend()
    plt.show()



Main()