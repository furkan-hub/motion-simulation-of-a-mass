import time
import os
import matplotlib.pyplot as plt

# Simulation time (second)
simulation_time = 100

# Simulation step in seconds
dt = 0.1

#Params

m = 10 # mass kg
g = 9.81#gravity N
f = 100 #force N

drag_confident = 0.1# drag

# Grafik için veri ve zaman düzenlemesi
x_data = []  # Zaman verilerini depolamak için boş bir liste
y_data = []  # Hızlanma verilerini depolamak için boş bir liste

# Grafik oluşturma
fig, ax = plt.subplots()
line, = ax.plot(x_data, y_data)

# Grafik güncelleme fonksiyonu
def update_grafik(zaman, hizlanma):
    x_data.append(zaman)
    y_data.append(hizlanma)

    # Grafik verilerini güncelleme
    line.set_xdata(x_data)
    line.set_ydata(y_data)

    # Grafik sınırlarını güncelleme
    ax.relim()
    ax.autoscale_view()

    # Grafik penceresini güncelleme
    plt.draw()
    plt.pause(0.01)  # Küçük bir bekleme süresi verme

# Simulation loop
for t in range(int(simulation_time/dt)):

    time_var =t*dt

    # Print current state
    
    #find friction force
    
    f_drag = g*m*drag_confident

    # find accelarition
    a = (f-f_drag)/m

    #find speed
    v = a*time_var

    update_grafik(v,time_var)
    os.system("cls")
    #print speed and time
    print("speed: ",v)
    print("Time: ", time_var)

    # Sleep for a while to match the real-time speed
    time.sleep(dt)
