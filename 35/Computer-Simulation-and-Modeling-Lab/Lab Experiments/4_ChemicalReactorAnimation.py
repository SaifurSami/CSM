#Parameters
import matplotlib.pyplot as plt 

k1 = 0.05
k2 = 0.05

a0 = 1 #Mole per volume
b0 = 0.5
c0 = 0

total_steps = 500
N = 100.00 #Total Time
dt = N/total_steps


# Simulation

# To hold A,B and C value
a = []
b = []
c = []
t = []

a.append(a0)
b.append(b0)
c.append(c0)
t.append(0.00)


print("Time(s)\tA\tB\tC")
print("_____________________________")
print(0.0,"\t",a0,"\t",b0,"\t",c0)

cur_time = 0.00

while cur_time <N:

    cur_time+=dt
    t.append(cur_time)
    new_a = a0 + (k2*c0 - k1*a0*b0)*dt
    new_b = b0 + (k2*c0 - k1*a0*b0)*dt
    new_c = c0 + (2*k1*a0*b0 - 2*k2*c0)*dt

    a.append(new_a)
    b.append(new_b)
    c.append(new_c)
    

    print(round(cur_time,2),"\t",round(new_a,2),"\t",round(new_b,2),"\t",round(new_c,2))

    a0 = new_a
    b0 = new_b
    c0 = new_c

for i in range (0,len(t)):
    plt.xlabel("Time")
    plt.ylabel("Reaction")
    plt.grid(True)
    plt.title(f"Chemical Reaction (upto {round(t[i],2)} sec)")

    plt.scatter(t[i],a[i],color='red',label='A')
    plt.scatter(t[i],b[i],color='blue',label='B')
    plt.scatter(t[i],c[i],color='green',label='C')

    if i%10==0:
        plt.pause(0.0001)

  