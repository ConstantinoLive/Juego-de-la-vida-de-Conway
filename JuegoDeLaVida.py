from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def inicializar_tablero(filas, columnas):
    # Crea un tablero inicial aleatorio con 0 y 1
    return np.random.choice([0, 1], size=(filas, columnas))

def actualizar_tablero(tablero):
    # Aplica las reglas del juego para actualizar el tablero
    filas, columnas = tablero.shape
    nuevo_tablero = np.zeros_like(tablero)

    for i in range(filas):
        for j in range(columnas):
            vecinos = tablero[i-1:i+2, j-1:j+2].sum() - tablero[i, j]
            if tablero[i, j] == 1:
                # Célula viva
                if vecinos == 2 or vecinos == 3:
                    nuevo_tablero[i, j] = 1
            else:
                # Célula muerta
                if vecinos == 3:
                    nuevo_tablero[i, j] = 1

    return nuevo_tablero

def actualizar(frameNum, img, tablero, filas, columnas):
    # Función de actualización para la animación
    nuevo_tablero = actualizar_tablero(tablero)
    img.set_array(nuevo_tablero)
    tablero[:,:] = nuevo_tablero[:,:]
    return img,

fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

def juego():
    global anim
    img = ax.imshow(tablero, interpolation='nearest', cmap='binary_r')  # Cambiar 'viridis' al mapa de colores 
    anim = animation.FuncAnimation(fig, actualizar, fargs=(img, tablero, filas, columnas),
                               frames=generaciones, interval=300, save_count=70)
    Canvas.draw()

def pausar():
    anim.event_source.stop()

def reanudar():
    anim.event_source.start()


# Parámetros del juego
filas, columnas = 100, 100 #250
generaciones = 20 #200

# Inicializar el tablero
tablero = inicializar_tablero(filas, columnas)


wds=Tk()

wds.title("Juego de la vida de Conway")
wds.iconbitmap("iconjdlv.ico")
wds.geometry("860x780")

frame1 = Frame(wds,bg="grey")
frame1.pack(expand=True,fill="both")

button_quit = Button(frame1,text="Salir",command=wds.quit) 
button_quit.place(relx=.02,rely=.02,relwidth=.1,relheight=.07)

button_start = Button(frame1,text="Iniciar",command=juego) 
button_start.place(relx=.17,rely=.02,relwidth=.1,relheight=.07)

button_stop = Button(frame1,text="Pausar",command=pausar) 
button_stop.place(relx=.32,rely=.02,relwidth=.1,relheight=.07)

button_reanudar = Button(frame1,text="Reanudar",command=reanudar) 
button_reanudar.place(relx=.47,rely=.02,relwidth=.1,relheight=.07)

Canvas=FigureCanvasTkAgg(fig, master=frame1)
Canvas.get_tk_widget().place(relx=.02,rely=.1)

wds.mainloop()