from producto import Producto
from cola import ListaCircularDoble
from email.mime import image
from glob import glob
from re import A
from socket import NI_NUMERICHOST
import tkinter
import os 
import graphviz
import customtkinter
import webbrowser

lista = ListaCircularDoble()

##METODOS

def info():
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Información del Desarrollador")   
    ancho_cargar_archivo= 500
    alto_cargar_archivo= 600
    x_cargar_archivo = ventana.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = ventana.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)

    #LABELS
    a=150

    #IMAGEN

    #LABEL IMG

    ima = tkinter.Label(nueva_ventana, image=perfil, width=150,height=150, bg="#17202A")
    ima.place(x=125,y=105, anchor=tkinter.CENTER)

    #nombres


    nombre = tkinter.Label(nueva_ventana, text="Geovanny Sebastián", font=("Helvetica", 28, "bold"))
    nombre.config(bg="#17202A", fg="white",anchor=tkinter.W)
    nombre.place(x=40,y=50+a)

    #apellidos

    apellidos = tkinter.Label(nueva_ventana, text="Herrera Claudio", font=("Helvetica", 28, "bold"))
    apellidos.config(bg="#17202A", fg="white",anchor=tkinter.W)
    apellidos.place(x=40,y=100+a)

    #carne

    carne = tkinter.Label(nueva_ventana, text="Carné: 202110588", font=("Helvetica", 14, "bold"))
    carne.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    carne.place(x=40,y=160+a)

    #cui

    cui = tkinter.Label(nueva_ventana, text="CUI: 3556794340101", font=("Helvetica", 14, "bold"))
    cui.config(bg="#17202A", fg="#D0D3D4",anchor=tkinter.W)
    cui.place(x=40,y=195+a)

    #curso

    cui = tkinter.Label(nueva_ventana, text="Lab. Introducción a la Programación y Computación 2", font=("Helvetica", 11, "bold"))
    cui.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
    cui.place(x=40,y=230+a)

    #github

    def github():
        webbrowser.open_new_tab("https://github.com/SebastianHerrera")

    button = customtkinter.CTkButton(master=nueva_ventana, text="GitHub", command=github)
    button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    nueva_ventana.geometry(posicion)
    nueva_ventana.config(bg="#17202A")
    nueva_ventana.resizable(0,0)

def cerrar():
    exit()

def ordenes():
    nueva_ventana = tkinter.Toplevel(ventana) 
    nueva_ventana.title("Órdenes")   
    ancho_cargar_archivo= 800
    alto_cargar_archivo= 500
    x_cargar_archivo = ventana.winfo_screenwidth()//2-ancho_cargar_archivo//2
    y_cargar_archivo = ventana.winfo_screenheight()//2-alto_cargar_archivo//2
    posicion=str(ancho_cargar_archivo)+"x"+str(alto_cargar_archivo)+"+"+str(x_cargar_archivo)+"+"+str(y_cargar_archivo)
    nueva_ventana.geometry(posicion)
    
    global min
    min=0

    #LABEL DE TIEMPO
    def label_tiempo():

        text = tkinter.Label(nueva_ventana,text="El tiempo de espera es de:",font=("Helvetica", 18, "bold"))
        text.config(bg="#17202A", fg="#B3B6B7",anchor=tkinter.W)
        text.place(relx=0.5,rely=0.6, anchor=tkinter.CENTER)

        time = tkinter.Label(nueva_ventana,text=str(min)+" minutos",font=("Helvetica", 32, "bold"))
        time.config(bg="#17202A", fg="white",anchor=tkinter.W)
        time.place(relx=0.5,rely=0.7, anchor=tkinter.CENTER)

    #METODOS BOTONES

    label_tiempo()

    def Salchicha():
        print("HotDog de Salchicha")
        global min
        min = min+2
        lista.agregar_final("Salchicha","Hot dog de Salchicha", 2)
        lista.crearReporte
        label_tiempo()

    def Chorizo():
        print("HotDog de Chorizo")
        global min
        min = min+3
        lista.agregar_final("Chorizo","Hot dog de Chorizo", 1)
        lista.crearReporte()
        label_tiempo()

    def Salami():
        print("HotDog de Salami")
        global min
        min = min+1.5
        lista.agregar_final("Salami","Hot dog de Salami", 1.5)
        lista.crearReporte()
        label_tiempo()

    def Longaniza():
        print("HotDog de Longaniza")
        global min
        min = min+4
        lista.agregar_final("Longaniza","Hot dog de Longaniza", 4)
        lista.crearReporte()
        label_tiempo()

    def Costilla():
        print("HotDog de Costilla")
        global min
        min = min+6
        lista.agregar_final("Costilla","Hot dog de Costilla", 6)
        lista.crearReporte()
        label_tiempo()


    #BOTON SALCHICHA

    button = customtkinter.CTkButton(master=nueva_ventana, text="Salchicha", command=Salchicha)
    button.place(relx=0.25, rely=0.2, anchor=tkinter.CENTER)

    #BOTON CHORIZO

    button = customtkinter.CTkButton(master=nueva_ventana, text="Chorizo", command=Chorizo)
    button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    #BOTON SALAMI

    button = customtkinter.CTkButton(master=nueva_ventana, text="Salami", command=Salami)
    button.place(relx=0.75, rely=0.2, anchor=tkinter.CENTER)

    #BOTON LONGANIZA

    button = customtkinter.CTkButton(master=nueva_ventana, text="Longaniza", command=Longaniza)
    button.place(relx=0.38, rely=0.35, anchor=tkinter.CENTER)

    #BOTON COSTILLA

    button = customtkinter.CTkButton(master=nueva_ventana, text="Costilla", command=Costilla)
    button.place(relx=0.62, rely=0.35, anchor=tkinter.CENTER)

    nueva_ventana.config(bg="#17202A")
    nueva_ventana.resizable(0,0)

##VENTANA

ventana = tkinter.Tk()
ventana.title("Práctica 1")
ventana.resizable(0,0)
ventana.iconbitmap("C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab Lenguajes Formales y de Programación/Práctica 1/Programa/logo.ico")
ventana.config(bg="#17202A")



##FRAME

frame = tkinter.Frame(ventana, width=800, height=500)
ancho_frame= 800
alto_frame= 500
x_frame = ventana.winfo_screenwidth()//2-ancho_frame//2
y_frame = ventana.winfo_screenheight()//2-alto_frame//2
posicion=str(ancho_frame)+"x"+str(alto_frame)+"+"+str(x_frame)+"+"+str(y_frame)
ventana.geometry(posicion)
frame.config(bg="#17202A")

#LABEL IMG
logo = tkinter.PhotoImage(file="C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Prac 1/descarga.png")
img = tkinter.Label(frame, image=logo, width=200,height=147, bg="#17202A")
img.place(relx=0.5,y=140, anchor=tkinter.CENTER)

perfil = tkinter.PhotoImage(file="C:/Users/sebas/Documents/USAC/Segundo Semestre 2022/Lab IPC2/Prac 1/perfil.png")

frame.pack()

##BOTONES DEL FRAME

#BOTON ORDENES

button = customtkinter.CTkButton(master=frame, text="Ordenes", command=ordenes)
button.place(relx=0.5, rely=0.60, anchor=tkinter.CENTER)


#BOTON INFO DEL DESARROLLADOR

button = customtkinter.CTkButton(master=frame, text="Información del Desarrollador", command=info)
button.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)

#BOTON CERRAR

button = customtkinter.CTkButton(master=frame, text="Cerrar", command=cerrar)
button.place(relx=0.5, rely=0.80, anchor=tkinter.CENTER)

##MAINLOOP

ventana.mainloop()