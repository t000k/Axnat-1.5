import cv2
import os
import imutils
import tkinter as tk
from tkinter import ttk
from tkinter import *



def persona():
   name = str(caja_usuarios.get())
   nametext = 'C:/Users/cisne/OneDrive/Escritorio/Reconocimiento Facial/Data'+'/' + name
   if not os.path.exists(nametext):
	#print('Carpeta creada: ',personPath)
    print('Carpeta creada: ', nametext)
    os.makedirs(nametext)
   
   cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4')

   faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
   count = 0

   while True:


    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite( nametext+ '/rotro_{}.jpg'.format(count),rostro)
        count = count + 1
    cv2.imshow('Captura de rostro',frame)

    k =  cv2.waitKey(1)
    if k == 27 or count >= 300:
        break

   cap.release()
   cv2.destroyAllWindows()
   os.system("python entrenandoRF.py")

def reconocimiento():
    ventana.destroy
    os.system("python ReconocimientoFacial.py")


ventana = tk.Tk()
ventana.title("AXNAT")
ventana.config(width=400, height=300)
ventana.configure(background='black')
etiqueta_titulo = ttk.Label(text="AXNAT", font="monospaced")
#imagen = PhotoImage(file= "candado2.png")
etiqueta_titulo.config(background= "black", foreground= "white")
etiqueta_descripcion = ttk.Label(text="Control de acceso", font="Arial")
etiqueta_descripcion.config(background="black", foreground= "white")
etiqueta_nombre = ttk.Label(text="Ingresa tu nombre: ")
etiqueta_nombre.config(background="black", foreground="white")
etiqueta_nombre.place(x=100, y=90)
etiqueta_titulo.place(x=170, y=10)
etiqueta_descripcion.place(x=100, y=40)
caja_usuarios = ttk.Entry()
caja_usuarios.place(x=100, y=110, width=200)
caja_usuarios.config(background="#351955", foreground="blue")
boton_agregar = ttk.Button(text="Agregar Alumno", command= persona)
boton_salir = ttk.Button(text="Iniciar Reconocimiento", command= reconocimiento)
boton_salir.place(x=130, y=270)
boton_agregar.place(x=142, y=140)
ventana.mainloop()

#pe =persona
#print(pe)
#personName = "josexual"
#dataPath = "C:/Users/cisne/Desktop/Reconocimiento Facial/Data" #Cambia a la ruta donde hayas almacenado Data
#personPath = dataPath + "/" + personName
#ruta = persona
#if not os.path.exists(ruta):
	#print('Carpeta creada: ',personPath)
#	print('Carpeta creada: ', ruta)
#	os.makedirs(ruta)

