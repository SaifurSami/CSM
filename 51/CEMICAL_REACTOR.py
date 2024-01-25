import matplotlib.pyplot as plt

def chemical_reactor(A,B,C,dt,k1,k2,T):
    substance_A = []
    substance_B = []
    substance_C = []
    time_slot = []
    time = 0

    while(time<=T):
        substance_A.append(A)
        substance_B.append(B)
        substance_C.append(C)
        time_slot.append(time)

        plt.clf()
        plt.title("Chemical Reactor")
        plt.xlabel("Time(s)")
        plt.ylabel("Quantity(mol)")
        plt.plot(time_slot,substance_A,label = "Substance A")
        plt.plot(time_slot,substance_B,label = "Substance B")
        plt.plot(time_slot,substance_C,label = "Substance C")
        plt.xlim(0,T+1)
        plt.legend()
        plt.pause(.01)

        temp = A*B
        A += (k2 * C - k1 * temp) * dt
        B += (k2 * C - k1 * temp) * dt
        C += (2 * k1 * temp - 2 * k2 * C) * dt
        time+=dt
    plt.show()

def main():
    A = 100
    B = 50
    C = 0
    dt = .1
    T = 5
    k1 = .008
    k2 = .002
    chemical_reactor(A,B,C,dt,k1,k2,T)

if __name__ == "__main__":
    main()