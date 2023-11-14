import mysql.connector 
import customtkinter as ctk
import os
import tkinter as tk
from tkinter import Tk, Label, Entry, Text, Scrollbar
from PIL import Image, ImageTk
import sys
from mysql.connector import Error



#Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
#carpeta Imagenes
ImageFile = os.path.join(HomeFile,"images")
def prueba(self):
        # Cerrar la ventana actual
        
        self.root.destroy()
        self.root = ctk.CTk()
        self.root.title("BDD")
        self.root.iconbitmap(os.path.join(ImageFile,"icono.ico"))
        self.root.geometry("600x600+350+20")
        self.root.minsize(480,500)
            
        # Mostrar la nueva ventana
        self.root.mainloop()

def conexion():       
    #Conecto mi BDD
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='fldsmdfr',
        db = 'Jardineria'
    )
    if conexion.is_connected():
        print("conexion establecida")
    
        cursor = conexion.cursor()
        select_query = "SELECT correo FROM usuarios"
        cursor.execute(select_query)
        resultados =cursor.fetchall()
        print(type(resultados))

    
