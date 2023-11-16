import customtkinter as ctk
import os
from tkinter import Tk, Label, Entry, Text, Scrollbar
from PIL import Image, ImageTk
import mysql
from mysql.connector import Error

#Configuraciones
ctk.set_appearance_mode("Sytem")
# -> rutas
#Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
#Carpeta Imagenes
ImageFile = os.path.join(HomeFile,"images")



def prueba(self,correo,contraseña):
        #Destruir ventana anterior
        #self.root.destroy()#!<------- genera un comando invalido invalid command name "1843648977280_click_animation"
        try:    
            ventana = ctk.CTk()
            ventana.title("BDD")
            ventana.iconbitmap(os.path.join(ImageFile,"icono.ico"))
            ventana.geometry("600x600+350+20")
            ventana.minsize(480,500)
            
            marco = ctk.CTkFrame(ventana)
            marco.pack(padx=50, pady=50)
            
            ctk.CTkLabel(marco, text=conexion(correo,contraseña),font=('sans serif',15)
                         ).pack(padx=25,pady=20)
            
            #Bucle de ejecución
            ventana.mainloop()
        except Error as ex:
            print('No se puede abrir la ventana',ex)
          


def conexion(gm,pss):
    #Conecto mi BDD
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='fldsmdfr',
        db = 'Jardineria'
    )
    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()
    
    # Consulta SQL para obtener datos de la tabla
    consulta = "SELECT contraseña FROM usuarios"
    cursor.execute(consulta)
    
    # Obtener todos los resultados de la consulta
    resultados = cursor.fetchall()
    
    # Comparar la variable con los datos de la tabla

    valores_str= ', '.join(map(str, resultados))   
    print("contraseña: ",pss)
    print(type)
    
    #!SI LA VARIABLE ES NULA IGUAL PUEDE PASAR
    if pss is not None:
    
        if pss in valores_str:
                return("LA CONEXION SE ESTABLECIO EXITOSAMENTE")
            
        else:
            return("CONEXION INTERRUMPIDA"), conexion.close()
    else:
        return("CONEXION INTERRUMPIDA"), conexion.close()

    
        