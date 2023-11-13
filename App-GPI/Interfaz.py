#Importaciones
import customtkinter as ctk
import os
from PIL import Image, ImageTk

#Configuraciones
ctk.set_appearance_mode("Sytem")

# -> rutas
#Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
#Carpeta Imagenes
ImageFile = os.path.join(HomeFile,"images")

class Login:
    def __init__(self):
    #Ventana Principal
        self.root = ctk.CTk()
        self.root.title("Iniciar Sesión")
        self.root.iconbitmap(os.path.join(ImageFile,"icono.ico"))
        self.root.geometry("600x600+350+20")
        self.root.minsize(480,500)

    #Contenido de la Ventana Login

        #Frame Principal de la aplicación
        frame = ctk.CTkFrame(self.root, fg_color='#010101')
        frame.pack(fill='both', expand=True)

        #logo
        logo = ctk.CTkImage(
            Image.open(os.path.join(ImageFile,"logo.png")),
            size=(250,250))
        #Etiqueta para imagen principal
        etiqueta = ctk.CTkLabel(frame,
            image = logo,
            text="",)
        etiqueta.pack(pady = 15)
        
        #Casilla Correo Electronico
        correo = ctk.CTkEntry(frame,  font = ('sans serif',12), placeholder_text= 'Correo electronico', 
        border_color='#2cb67d', fg_color= '#010101',width =220,height=40,text_color='#D5D5D5')
        correo.pack(pady = 15)

        #Casilla Contraseña
        contrasenna = ctk.CTkEntry(frame,show="*", font = ('sans serif',12), placeholder_text= 'Contraseña',
        border_color='#2cb67d', fg_color= '#010101', width =220,height=40,text_color='#D5D5D5')
        contrasenna.bind("<Button-1>",lambda e: contrasenna.delete(0,'end'))
        contrasenna.pack(pady = 15)

        #Boton Iniciar Sesión
        bt_iniciar = ctk.CTkButton(frame, font = ('sans serif',12), border_color='#2cb67d', fg_color='#010101',
            hover_color='#2cb67d',corner_radius=12,border_width=2,
            text='INICIAR SESIÓN')#,command=)
        bt_iniciar.pack(pady = 15)

        #Bucle de ejecución
        self.root.mainloop()
        


