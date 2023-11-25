import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import mysql
import pandas as pd
import matplotlib.pyplot as plt
import TESTOFRENDO as next
from PIL import Image


#Configuraciones
ctk.set_appearance_mode("Sytem")

# -> rutas
#Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
#Carpeta Imagenes
ImageFile = os.path.join(HomeFile,"images")

class MenuPrincipal():
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal        
    def actualizacionDeventana(self):
        # Configuracion de la ventana secundaria
        self.ventana_secundaria = ctk.CTk()
        self.ventana_secundaria.title("Menu de Opciones")
        self.ventana_secundaria.geometry("600x600+350+20")
        self.ventana_secundaria.minsize(480, 500)
        self.ventana_secundaria.iconbitmap(os.path.join(ImageFile, "icono.ico"))

        # Frame principal
        frame_secundario = ctk.CTkFrame(self.ventana_secundaria, fg_color='#91a398', bg_color='#C0D9AF')
        frame_secundario.pack(fill='both', expand=True)

        # Etiqueta para el titulo 
        ctk.CTkLabel(frame_secundario, text='Menu de Opciones', 
                     font=('Helvetica', 24, 'bold'), fg_color='#91a398', 
                     bg_color='#C0D9AF').pack(pady=20)

        # Estilo comun para los botones 
        estilo_boton = {'font': ('Helvetica', 16),'fg_color': '#e9e0d1','border_color':'#68462b','hover_color': '#e7d9b4','corner_radius': 12,'border_width': 3,'width': 200,'text_color':'#213635'}

        # Configuracion del frame de los botones en columna
        frame_botones = ctk.CTkFrame(frame_secundario, fg_color='#91a398', bg_color='#91a398')
        frame_botones.pack(pady=20)

        # Modificar Usuario
        bt_modificar_usuario = ctk.CTkButton(frame_botones, text='Modificar Usuario', command=self.mod_usuario, **estilo_boton)
        bt_modificar_usuario.pack(pady=10, anchor='center')

        # Modificar Productos
        bt_modificar_productos = ctk.CTkButton(frame_botones, text='Modificar Productos', command=self.mod_productos, **estilo_boton)
        bt_modificar_productos.pack(pady=10, anchor='center')

        # Modificar Ubicaciones
        bt_modificar_ubicaciones = ctk.CTkButton(frame_botones, text='Modificar Ubicaciones', command=self.mod_ubicaciones, **estilo_boton)
        bt_modificar_ubicaciones.pack(pady=10, anchor='center')

        # Ver Estadisticas
        bt_ver_estadisticas = ctk.CTkButton(frame_botones, text='Ver Estadisticas', command=self.estadisticas, **estilo_boton)
        bt_ver_estadisticas.pack(pady=10, anchor='center')

        # Bucle de ejecucion de la Segunda Ventana
        self.ventana_secundaria.mainloop()

    def mod_usuario(self):
        #llamada a modificar usuario
        self.toplevel_window = MOD_Usuario()

    def mod_ubicaciones(self):
        # Logica para la opcion "Modificar Productos"
        # Puedes implementar la funcionalidad correspondiente aqui
        print("Modificar Productos")

    def mod_productos(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        print("Modificar Ubicaciones")

    def estadisticas(self):

        # Ejemplo de datos para estadisticas
        datos = {'Categoria': ['Enero', 'Febrero', 'Marzo', 'Abril'],
                 'Valor': [70, 75, 100, 87]}

        # Crear un DataFrame con los datos
        df = pd.DataFrame(datos)

        # Crear un grafico de barras
        plt.bar(df['Categoria'], df['Valor'])
        plt.xlabel('Mes Controlado')
        plt.ylabel('Cantidad')
        plt.title('Ventas Historicas')

        # Mostrar el grafico
        plt.show()
    
    
class ConfirmationWindow:
    def __init__(self):
         self.root=ctk.CTk()
         
    def prueba(self,correo,contraseña):
        
        ventana = ctk.CTk()
        ventana.title("Ventana Confirmación")
        ventana.iconbitmap(os.path.join(ImageFile,"icono.ico"))
        ventana.geometry("470x200")
        ventana.minsize(470,200)
        ventana.iconbitmap(os.path.join(ImageFile, "icono.ico"))

        # Frame Principal de la aplicación
        frame = ctk.CTkFrame(ventana, fg_color='#91a398',bg_color='#91a398')
        frame.pack(fill='both', expand=True)
                
        marco = ctk.CTkFrame(frame,bg_color='#91a398')
        marco.pack(fill='both',expand=True,padx=30,pady=20)
                
        resul_conexion = conexion(correo,contraseña)        

        ctk.CTkLabel(marco, text=resul_conexion,font=('sans serif',15)).pack(padx=25,pady=20)
        
        #Ventana emergente para la conexión ---------------------------------------------------------------------------------------------------------------------------------
        if resul_conexion == "Contraseña Incorrecta":
            pass
        else:
                # Boton Nuevo
            NewBt = ctk.CTkButton(frame, font = ('Helvetica',16), border_color='#68462b', fg_color='#e9e0d1',
                hover_color='#e7d9b4', corner_radius=12, border_width=3,text_color='#213635',
                text='Continuar', command=self.llamarActualizacion())
            NewBt.pack(pady=15)
        #NewBt.config(state=tk.DISABLED) <--- desactivar el boton al utilizarlo
        
            #Bucle de ejecución
        ventana.mainloop()

    def llamarActualizacion(self):
        self.root.destroy()
        menu_principal = MenuPrincipal(self.root)
        menu_principal.actualizacionDeventana()
            #NewBt.config(state=tk.DISABLED) <--- desactivar el boton al utilizarlo
            
        #Bucle de ejecución
        #self.ventana.mainloop()
#Conexion BD -----------------------------------------------------------------------------------------------------------------------------------------------------------
def conexion(gm,pss):
    #!                  AUN NO COMPUREBO EL CORREO Y LA CONTRASEÑA JUNTOS
    #Conecto mi BDD
    # Crear un cursor para ejecutar consultas
    try:
        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
            with conexion.cursor() as cursor:
                # Consulta SQL para obtener datos de la tabla
                consulta = "SELECT contraseña FROM usuarios"
                cursor.execute(consulta)
                
                # Obtener todos los resultados de la consulta
                resultados = cursor.fetchall()
                
                # Comparar la variable con los datos de la tabla

                valores_str = ', '.join(map(str, resultados))   

                conexion.close()

                if pss in valores_str:
                    return("Bienvenido a GreenHouse")    
                else:
                    return("Contraseña Incorrecta")
    except mysql.connector.Error as err:
        print(f"Error de MySQL: {err}")
    return "Error en la conexión a la base de datos para el LOGIN"
    
class MOD_Usuario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("900x420")
        self.iconbitmap(os.path.join(ImageFile, "icono.ico"))
        self.config(bg='#91a398')
        self.resizable(False,False)
        font1 = ('Helvetica',14,'bold')
        font2 = ('Helvetica',12,'bold')
        #BD connection
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            db = 'Jardineria'
        )
        cursor = conexion.cursor()
        def mostrar_data(event):
            selected_item = tree.focus()
            if selected_item:
                row = tree.item(selected_item)['values']
                clear_cells()
                Entrada_Correo.insert(0,row[0])
                Entrada_Modificación.insert(0,row[1])
                Entrada_Responsable.insert(0,row[2])
                variable1.set(row[3])
                Entrada_Status.insert(0,row[4])
            else:
                pass
        def eliminar_dato():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para eliminar')
            else:
                Correo = Entrada_Correo.get()
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "DELETE FROM jardineria.usuarios WHERE correo = %s"
                            valores = (Correo,)
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Usuario eliminado con éxito')
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar')
            else:
                Correo = Entrada_Correo.get()
                FechaMod = Entrada_Modificación.get()
                Rol = variable1.get()
                Responsable = Entrada_Responsable.get()
                Seña = Entrada_Status.get()
                if not (Correo and FechaMod and Rol and Responsable and Seña):
                    messagebox.showerror('Error', 'No pueden faltar campos')
                else:
                    try:
                        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE jardineria.usuarios SET fecha_modificacion = NOW(), contraseña = %s, responsable = %s, rol_usuarios = %s WHERE correo = %s"
                                valores = (Seña,Responsable,Rol,Correo)
                                cursor.execute(consulta,valores)
                                # Confirmar los cambios en la base de datos
                                conexion.commit()
                                # Mostrar mensaje de éxito
                                messagebox.showinfo('Éxito', 'Usuario actualizado correctamente')
                                # Actualizar la vista de Treeview
                                add_to_treeview()

                    except mysql.connector.Error as err:
                        print(f"Error de MySQL: {err}")

        def Correo_exist(Correo):
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT COUNT(*) FROM jardineria.usuarios WHERE correo = %s;"
                        cursor.execute(consulta, (Correo,))
                        resultado = cursor.fetchone()
                        print(resultado)
                return resultado[0] > 0
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
                return False
        #funciones
        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT correo,fecha_modificacion,responsable,rol_usuarios FROM jardineria.usuarios"
                        cursor.execute(consulta)
                        resultado = cursor.fetchall()
                        
                        # Borrar todos los elementos actuales en el Treeview
                        tree.delete(*tree.get_children())
                        
                        # Insertar los nuevos datos en el Treeview
                        for fila in resultado:
                            tree.insert('', END, values=fila)

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

        def insertar():
            Correo = Entrada_Correo.get()
            FechaMod = Entrada_Modificación.get()
            Rol = variable1.get()
            Responsable = Entrada_Responsable.get()
            Seña = Entrada_Status.get()
            print(Correo,' ',FechaMod,' ',Rol,' ',Responsable,' ',Seña)
            
            if not (Correo and FechaMod and Rol and Responsable and Seña):
                messagebox.showerror('Error', 'No pueden faltar campos')
            elif Correo_exist(Correo):
                messagebox.showerror('Error', 'El usuario ya existe')
            else:
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO jardineria.usuarios (fecha_modificacion, contraseña, correo, responsable, rol_usuarios) VALUES (NOW(),%s,%s,%s,%s)"
                            valores = (Seña,Correo,Responsable,Rol)
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Usuario agregado correctamente')
                            # Actualizar la vista de Treeview
                            add_to_treeview()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def clear_cells(*clicked):
            if clicked:
                tree.selection_remove(tree.focus())
            Entrada_Correo.delete(0,END)
            Entrada_Modificación.delete(0,END)
            Entrada_Responsable.delete(0,END)
            variable1.set('colaborador')
            Entrada_Status.delete(0,END)

        

        #Formato página
        Etiqueta_Correo = ctk.CTkLabel(self,font=font1,text='Correo:',text_color='#000',bg_color='#91a398')
        Etiqueta_Correo.place(x=20,y=20)
        Entrada_Correo = ctk.CTkEntry(self,placeholder_text='example@gmail.com',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Correo.place(x=120,y=20)
        Etiqueta_Modificación = ctk.CTkLabel(self,font=font1,text='Modificación:',text_color='#000',bg_color='#91a398')
        Etiqueta_Modificación.place(x=20,y=80)
        Entrada_Modificación = ctk.CTkEntry(self,placeholder_text='Fecha',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Modificación.place(x=120,y=80)
        Etiqueta_Responsable = ctk.CTkLabel(self,font=font1,text='Responsable:',text_color='#000',bg_color='#91a398')
        Etiqueta_Responsable.place(x=20,y=140)
        Entrada_Responsable = ctk.CTkEntry(self,placeholder_text='Usuario',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Responsable.place(x=120,y=140)
        Etiqueta_rol = ctk.CTkLabel(self,font=font1,text='Rol:',text_color='#000',bg_color='#91a398')
        Etiqueta_rol.place(x=20,y=200)
        options = ['admin','colaborador']
        variable1 = ctk.StringVar()
        OpcionesRol = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=variable1,values=options,state='readonly',bg_color='#91a398')
        OpcionesRol.set('colaborador')
        OpcionesRol.place(x=120,y=200)
        EtiquetaStatus = ctk.CTkLabel(self,font=font1,text='Contraseña:',text_color='#000',bg_color='#91a398')
        EtiquetaStatus.place(x=20,y=260)
        Entrada_Status = ctk.CTkEntry(self,show='*',placeholder_text='************',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Status.place(x=120,y=260)
        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Usuario',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(x=20,y=310)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(x=20,y=360)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(x=300,y=360)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(x=580,y=360)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Correo','Modificación','Responsable','Rol','Contraseña')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Correo',anchor=tk.CENTER,width=140)
        tree.column('Modificación',anchor=tk.CENTER,width=140)
        tree.column('Responsable',anchor=tk.CENTER,width=140)
        tree.column('Rol',anchor=tk.CENTER,width=140)
        tree.column('Contraseña',anchor=tk.CENTER,width=140)
        tree.heading('Correo',text='Correo')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.heading('Rol',text='Rol')
        tree.heading('Contraseña',text='Contraseña')
        tree.place(x=380,y=20)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        #cursor = conexion.cursor()
        #consulta = "SELECT correo,fecha_modificacion,responsable,rol_usuarios FROM jardineria.usuarios"
        #cursor.execute(consulta)

        # Cerrar el cursor y la conexión
        #cursor.close()
        conexion.close()