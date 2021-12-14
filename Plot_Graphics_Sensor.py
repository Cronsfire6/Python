import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

if __name__ == '__main__':#Verifico que estoy corriendo el programa desde main
    print("Ingrese el puerto COM")
    com= input()
    print("Ingrese el baudrate")
    br = input()
    ad=serial.Serial(com, br)
    if not ad.isOpen():
        print("No se puede abrir el puerto, reinicie")
        while 1:
            pass
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = []
    """
    accx = [] #Creo lista que contendran los diferentes datos del sensor
    accy = [] 
    gyrox = []
    gyroy = []
    """
    fcx = []
    fcy = []
    fkx = []
    fky = []
    
#def animate(i, xs, accx, accy, gyrox, gyroy, fcx, fcy, fkx, fky):
def animate(i, xs, fcx, fcy, fkx, fky):
    #Adquiero y separo datos enviados por el puerto serie
    line=ad.readline()      #ascii
    line=str(line,'utf-8')
    line_as_list = line.split(',')
    i = int(line_as_list[0])
    """
    dAccx = float(line_as_list[1])
    dAccy = float(line_as_list[2])
    dGyrox = float(line_as_list[3])
    dGyroy = float(line_as_list[4])
    """
    dFcx = float(line_as_list[1])
    dFcy = float(line_as_list[2])
    dFkx = float(line_as_list[3])
    temporalFky = line_as_list[4]
    temporalFkyAsList= temporalFky.split('\n')
    dFky = float(temporalFkyAsList[0])
    # Agrego valores enviados a sus listas
    xs.append(i)
    """
    accx.append(dAccx)
    accy.append(dAccy)
    gyrox.append(dGyrox)
    gyroy.append(dGyroy)
    """
    fcx.append(dFcx)
    fcy.append(dFcy)
    fkx.append(dFkx)
    fky.append(dFky)

    #Dibujo todos los datos en sus graficas
    ax.clear()
    """
    ax.plot(xs, accx, label="Acelerometro X")
    ax.plot(xs, accy, label="Acelerometro Y")
    ax.plot(xs, gyrox, label="Giroscopo X")
    ax.plot(xs, gyrox, label="Giroscopo Y")
    """
    ax.plot(xs, fcx, label="Filtro Comp. X")
    ax.plot(xs, fcx, label="Filtro Comp. Y")
    ax.plot(xs, fkx, label="Filtro Kalman X")
    ax.plot(xs, fky, label="Filtro Kalman Y")

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('This is how I roll...')
    plt.ylabel('Relative frequency')
    plt.legend()
    plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
    #plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

    # Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, fcx, fcy, fkx, fky), interval=1000)
plt.show()
