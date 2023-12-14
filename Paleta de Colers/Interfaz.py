import customtkinter as ctk
import os
from tkinter import messagebox
from PIL import Image
from mysql.connector import Error
from App import ConfirmationWindow

# Configuraciones-----------------------------------------------------------------------------------------------------------------------------------------------
ctk.set_appearance_mode("Sytem")
# -> rutas
# Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
# Carpeta Imagenes
ImageFile = os.path.join(HomeFile, "images")
#Login----------------------------------------------------------------------------------------------------------------------------------------------------------
class Login:
    def __init__(self):
        # Ventana Principal
        self.root = ctk.CTk()
        self.root.title("Iniciar Sesión")
        #evita que se haga la pantalla completa
        self.root.resizable(0, 0)
        self.root.iconbitmap(os.path.join(ImageFile, "icono.ico"))
        self.root.geometry("600x600+350+20")
        self.root.minsize(480, 500)

        # Contenido de la Ventana Login----------------------------------------------------------------------------------------------------
        # Frame Principal de la aplicación
        frame = ctk.CTkFrame(self.root, fg_color='#D1F2EB')
        frame.pack(fill='both', expand=True)
        # logo
        logo = ctk.CTkImage(Image.open(os.path.join(ImageFile, "logo.png")),size=(250, 250))
        # Etiqueta para imagen principal
        etiqueta = ctk.CTkLabel(frame,image=logo,text="", )
        etiqueta.pack(pady=15)

        #Casilla Correo Electronico
        self.correo = ctk.CTkEntry(frame,  font = ('Helvetica',16), placeholder_text= 'Correo electronico', placeholder_text_color='#516d7d',
            border_color='#85C1E9', border_width=3, fg_color= '#CDEBFF',width =220,height=40,text_color='#070001')
        self.correo.pack(pady = 15)

        #Casilla Contraseña
        self.contrasenna = ctk.CTkEntry(frame,show="*", font = ('Helvetica',16), placeholder_text= 'Contraseña', placeholder_text_color='#516d7d',
            border_color='#85C1E9', fg_color= '#CDEBFF', border_width=3, width =220,height=40,text_color='#070001')
        self.contrasenna.pack(pady = 15)
            
        # Boton Iniciar Sesión
        
        bt_iniciar = ctk.CTkButton(frame, font = ('Helvetica',16), border_color='#68462b', fg_color='#e9e0d1',
            hover_color='#e7d9b4', corner_radius=12, border_width=3,text_color='#213635',
            text='Iniciar Sesión', command=lambda:self.comprobacion(self.correo.get(),self.contrasenna.get()))
        bt_iniciar.pack(pady=15)
        
        self.root.bind('<Return>', lambda event: self.comprobacion(self.correo.get(),self.contrasenna.get()))

        # Bucle de ejecución --------------------------------------------------------------------------------------------------------------
        self.root.mainloop()
        
    #NOS ASEGURAMOS QUE ESTEN TODOS LOS CAMPOS ESCRITOS    
    def comprobacion(self,correo,contrasenna):
            #genero un nself para mandarlo y destruir la ventana anterior FUNCIONA FALTA TESTEO
            nself=self
            if not contrasenna or not correo:
                messagebox.showwarning("¡Advertencia!", "¡No pueden faltar campos!")        
            else:
                
                #self.comprobar_credenciales(correo,contrasenna)
                nself.comprobar_credenciales(correo,contrasenna)
    #------------------------------------------------------Funcion para comprobar las credenciales--------------------------------
    def comprobar_credenciales(nself,correo,contraseña):
        try:
            nueva_ventana=ConfirmationWindow(nself)
            nueva_ventana.prueba(correo,contraseña)    
            pass
        except Exception as ex:
            print("Error", ex)
        
        
        
