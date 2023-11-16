import customtkinter as ctk
import os
import tkinter as tk
from tkinter import Tk, Label, Entry, Text, Scrollbar
from PIL import Image, ImageTk
from mysql.connector import Error
from pruebaconexion import prueba

# Configuraciones
ctk.set_appearance_mode("Sytem")
# -> rutas
# Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
# Carpeta Imagenes
ImageFile = os.path.join(HomeFile, "images")

class Login:
    def __init__(self):

        # Ventana Principal
        self.root = ctk.CTk()
        self.root.title("Iniciar Sesión")
        self.root.iconbitmap(os.path.join(ImageFile, "icono.ico"))
        self.root.geometry("600x600+350+20")
        self.root.minsize(480, 500)

        # Contenido de la Ventana Login
        # Frame Principal de la aplicación
        frame = ctk.CTkFrame(self.root, fg_color='#010101')
        frame.pack(fill='both', expand=True)

        # logo
        logo = ctk.CTkImage(
            Image.open(os.path.join(ImageFile, "logo2.0.png")),
            size=(250, 250))
        # Etiqueta para imagen principal
        etiqueta = ctk.CTkLabel(frame,
                                image=logo,
                                text="", )
        etiqueta.pack(pady=15)

        # Casilla Correo Electronico
        self.correo = ctk.CTkEntry(frame, font=('sans serif', 12),
                                   border_color='#2cb67d', fg_color='#010101', width=220,
                                   height=40, text_color='#D5D5D5')
        self.correo.pack(pady=15)

        # Casilla Contraseña
        self.contrasenna = ctk.CTkEntry(frame, show="*", font=('sans serif', 12),
                                        border_color='#2cb67d', fg_color='#010101', width=220, height=40,
                                        text_color='#D5D5D5')
        self.contrasenna.pack(pady=15)
        
        # Boton Iniciar Sesión
        bt_iniciar = ctk.CTkButton(frame, font=('sans serif', 12), border_color='#2cb67d', fg_color='#010101',
                                   hover_color='#2cb67d', corner_radius=12, border_width=2,
                                   text='INICIAR SESIÓN', command=lambda:self.abrir_nueva_ventana(self.correo.get(),self.contrasenna.get()))
        bt_iniciar.pack(pady=15)

        # Bucle de ejecución
        self.root.mainloop()

    def abrir_nueva_ventana(self,correo, contraseña):
        try:
            prueba(self,correo,contraseña)    
            pass
        except Exception as ex:
            print("Error", ex)
        
        
        
    