import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import mysql
import pandas as pd
from datetime import datetime,timedelta
import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image, ImageTk

UsuarioRes = ''
RolSesion = ''
#Configuraciones
ctk.set_appearance_mode("Sytem")

# -> rutas
#Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
#Carpeta Imagenes
ImageFile = os.path.join(HomeFile,"images")


class ConfirmationWindow():
    def __init__(self,nself):
        self.nself = nself
        self.root = ctk.CTk()

    def prueba(self, correo, contraseña):
        global UsuarioRes,RolSesion
        self.ventana = ctk.CTk()
        self.ventana.title("Ventana Confirmación")
        self.ventana.iconbitmap(os.path.join(ImageFile, "icono.ico"))
        self.ventana.geometry("470x200")
        self.ventana.minsize(470, 200)
        self.ventana.iconbitmap(os.path.join(ImageFile, "icono.ico"))

        # Frame Principal de la aplicación
        self.frame = ctk.CTkFrame(self.ventana, fg_color='#D1F2EB', bg_color='#D1F2EB')
        self.frame.pack(fill='both', expand=True)

        marco = ctk.CTkFrame(self.frame, bg_color='#D1F2EB')
        marco.pack(fill='both', expand=True, padx=30, pady=20)

        resul_conexion = self.conexion(correo, contraseña)


        ctk.CTkLabel(marco, text=resul_conexion, font=('sans serif', 15)).pack(padx=25, pady=20)


        # Ventana emergente para la conexión ---------------------------------------------------------------------------------------------------------------------------------
        if resul_conexion == "Datos Incorrectos":
            pass
        else:
            # Boton Nuevo
            self.nself.root.destroy()
            NewBt = ctk.CTkButton(self.frame, font=('Helvetica', 16), border_color='#68462b', fg_color='#e9e0d1',
                                  hover_color='#e7d9b4', corner_radius=12, border_width=3, text_color='#213635',
                                  text='Continuar', command=self.llamarActualizacion)
            NewBt.pack(pady=15)
            
            UsuarioRes = correo
            RolSesion = self.Retorno(correo)

        # Bucle de ejecución
        self.ventana.mainloop()

    def llamarActualizacion(self):
        self.ventana.destroy()
        if RolSesion[0] == 'admin':
            menu_principal = MenuPrincipal(self.root)
        else:
            menu_principal = MenuPrincipalCol(self.root)
        menu_principal.actualizacionDeventana()

    def conexion(self, correo, pss):
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT contraseña FROM usuarios WHERE correo = %s"
                        cursor.execute(consulta, (correo,))
                        resultado = cursor.fetchone()
                        if resultado and pss == resultado[0]:
                            return "Bienvenido a GreenHouse"
                        else:
                            return "Datos Incorrectos"
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
            return "Error en la conexión a la base de datos para el LOGIN"
    
    def Retorno(self,correo):
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:

                        cons="SELECT rol_usuarios FROM usuarios WHERE correo = %s"   #<--- consulta para obtener el responsable

                        cursor.execute(cons, (correo,))

                        resultado = cursor.fetchone()   #<--- resultado de la consulta
                        return(resultado) #!<--- retorno del responsable


            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

class MenuPrincipal():
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal        
    def actualizacionDeventana(self):
        # Configuracion de la ventana secundaria
        self.ventana_secundaria = ctk.CTk()
        self.ventana_secundaria.title("Menu de Opciones")
        self.ventana_secundaria.geometry("600x600+350+20")
        self.ventana_secundaria.attributes('-topmost', False)
        self.ventana_secundaria.minsize(480, 500)
        self.ventana_secundaria.iconbitmap(os.path.join(ImageFile, "icono.ico"))
        # Frame principal
        frame_secundario = ctk.CTkFrame(self.ventana_secundaria, fg_color='#D1F2EB',  bg_color='#D1F2EB')
        frame_secundario.pack(fill='both', expand=True)
        # Etiqueta para el titulo 
        ctk.CTkLabel(frame_secundario, text='Menu de Opciones', 
                     font=('Helvetica', 24, 'bold'), fg_color='#D1F2EB', text_color='#070A05',
                      bg_color='#D1F2EB').pack(pady=20)
        # Estilo comun para los botones 
        estilo_boton = {'font': ('Helvetica', 16),'fg_color': '#e9e0d1','border_color':'#68462b','hover_color': '#e7d9b4','corner_radius': 12,'border_width': 3,'width': 200,'text_color':'#213635'}
        # Configuracion del frame de los botones en columna
        frame_botones = ctk.CTkFrame(frame_secundario, fg_color='#D1F2EB', bg_color='#D1F2EB')
        frame_botones.pack(pady=20)
        # Modificar Usuario
        bt_modificar_usuario = ctk.CTkButton(frame_botones, text='Maestro de Usuarios', command=self.mod_usuario, **estilo_boton)
        bt_modificar_usuario.pack(pady=10, anchor='center',fill = X)
        # Modificar Productos
        bt_modificar_productos = ctk.CTkButton(frame_botones, text='Maestro de Productos', command=self.mod_productos, **estilo_boton)
        bt_modificar_productos.pack(pady=10, anchor='center',fill = X)
        # Modificar Ubicaciones
        bt_modificar_ubicaciones = ctk.CTkButton(frame_botones, text='Maestro de Ubicaciones', command=self.mod_ubicaciones, **estilo_boton)
        bt_modificar_ubicaciones.pack(pady=10, anchor='center',fill = X)
        # Modificar Inventario
        bt_modificar_inventario = ctk.CTkButton(frame_botones, text='Maestro de Inventario', command=self.mod_inventario, **estilo_boton)
        bt_modificar_inventario.pack(pady=10, anchor='center',fill = X)
        # Modificar Movimiento
        bt_modificar_moviemientos = ctk.CTkButton(frame_botones, text='Maestro de Movimientos', command=self.mod_movimiento, **estilo_boton)
        bt_modificar_moviemientos.pack(pady=10, anchor='center',fill = X)
        # Ingresar MOVIMIENTO
        bt_movimientos = ctk.CTkButton(frame_botones, text='Ingresar Movimiento', command=self.Ingreso_Movimiento, **estilo_boton)
        bt_movimientos.pack(pady=20, anchor='center',fill = X)
        # Estadísticas
        bt_estadistica = ctk.CTkButton(frame_botones, text='Mostrar Estadísticas', command=self.estadisticas_show, **estilo_boton)
        bt_estadistica.pack(pady=10, anchor='center',fill = X)

        try:
            with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                with conexion.cursor() as cursor:
                    consulta = "SELECT tp.nombre AS nombre_producto, SUM(CASE WHEN m.razon IN ('Venta', 'Baja', 'Merma') THEN m.cantidad ELSE 0 END) / NULLIF(SUM(CASE WHEN m.razon IN ('Compra', 'Repuesto') THEN m.cantidad ELSE 0 END), 0) AS division_resultado FROM tipo_producto tp JOIN movimiento m ON tp.sku = m.sku GROUP BY tp.nombre HAVING division_resultado >= 0.85"
                    cursor.execute(consulta)
                    resultado = cursor.fetchall()
                    print(resultado)
                    if resultado:
                        mensaje = "ALERTA: Productos con stock inferior al 15%:\n\n"
                        for producto, division in resultado:
                            mensaje += f"{producto}: {division:.2f}\n"
                        messagebox.showinfo("ALERTA!", mensaje)
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
            return

        # Bucle de ejecucion de la Segunda Ventana
        self.ventana_secundaria.mainloop()
        
    def mod_usuario(self):
        self.toplevel_window = MOD_Usuario()
        self.toplevel_window.grab_set()
    
    def mod_ubicaciones(self):
        self.toplevel_window = MOD_Ubicaciones()
        self.toplevel_window.grab_set()
    
    def mod_productos(self):
        self.toplevel_window = MOD_Producto()
        self.toplevel_window.grab_set()
    
    def mod_inventario(self):
        self.toplevel_window = MOD_Inventario()
        self.toplevel_window.grab_set()
    
    def mod_movimiento(self):
        self.toplevel_window = MOD_Movimiento()
        self.toplevel_window.grab_set() 
    
    def Ingreso_Movimiento(self):
        self.toplevel_window = Movimientos_Func()
        self.toplevel_window.grab_set()
    
    def estadisticas_show(self):
        self.toplevel_window = Show_Estadisticas()
        self.toplevel_window.grab_set()

class MenuPrincipalCol():
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal    
    def actualizacionDeventana(self):
        # Configuracion de la ventana secundaria
        self.ventana_secundaria = ctk.CTk()
        self.ventana_secundaria.title("Menu de Opciones")
        self.ventana_secundaria.attributes('-topmost', False)
        self.ventana_secundaria.geometry("600x600+350+20")
        self.ventana_secundaria.minsize(480, 500)
        self.ventana_secundaria.iconbitmap(os.path.join(ImageFile, "icono.ico"))
        # Frame principal
        frame_secundario = ctk.CTkFrame(self.ventana_secundaria, fg_color='#D1F2EB', bg_color='#D1F2EB')
        frame_secundario.pack(fill='both', expand=True)
        # Etiqueta para el titulo 
        ctk.CTkLabel(frame_secundario, text='Menu de Opciones', 
                     font=('Helvetica', 24, 'bold'), fg_color='#D1F2EB', text_color='#070A05',
                      bg_color='#D1F2EB').pack(pady=20)
        # Estilo comun para los botones 
        estilo_boton = {'font': ('Helvetica', 16),'fg_color': '#e9e0d1','border_color':'#68462b','hover_color': '#e7d9b4','corner_radius': 12,'border_width': 3,'width': 200,'text_color':'#213635'}
        # Configuracion del frame de los botones en columna
        frame_botones = ctk.CTkFrame(frame_secundario, fg_color='#D1F2EB', bg_color='#D1F2EB')
        frame_botones.pack(pady=20)
        # Modificar Usuario
        bt_modificar_usuario = ctk.CTkButton(frame_botones, text='Consultar Usuarios', command=self.ver_usuario, **estilo_boton)
        bt_modificar_usuario.pack(pady=10, anchor='center',fill = X)
        # Modificar Productos
        bt_modificar_productos = ctk.CTkButton(frame_botones, text='Consultar Productos', command=self.ver_productos, **estilo_boton)
        bt_modificar_productos.pack(pady=10, anchor='center',fill = X)
        # Modificar Ubicaciones
        bt_modificar_ubicaciones = ctk.CTkButton(frame_botones, text='Consultar Ubicaciones', command=self.ver_ubicaciones, **estilo_boton)
        bt_modificar_ubicaciones.pack(pady=10, anchor='center',fill = X)
        # Modificar Inventario
        bt_modificar_inventario = ctk.CTkButton(frame_botones, text='Consultar Inventario', command=self.ver_inventario, **estilo_boton)
        bt_modificar_inventario.pack(pady=10, anchor='center',fill = X)
        # Ingresar Movimiento
        bt_ingresar_movimientos = ctk.CTkButton(frame_botones, text='Ingresar Movimiento', command=self.Ingreso_Movimiento, **estilo_boton)
        bt_ingresar_movimientos.pack(pady=15, anchor='center',fill = X)
        # Estadísticas
        bt_estadistica = ctk.CTkButton(frame_botones, text='Mostrar Estadísticas', command=self.estadisticas_show, **estilo_boton)
        bt_estadistica.pack(pady=15, anchor='center',fill = X)   
        # Bucle de ejecucion de la Segunda Ventana

        try:
            with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                with conexion.cursor() as cursor:
                    consulta = "SELECT tp.nombre AS nombre_producto, SUM(CASE WHEN m.razon IN ('Venta', 'Baja', 'Merma') THEN m.cantidad ELSE 0 END) / NULLIF(SUM(CASE WHEN m.razon IN ('Compra', 'Repuesto') THEN m.cantidad ELSE 0 END), 0) AS division_resultado FROM tipo_producto tp JOIN movimiento m ON tp.sku = m.sku GROUP BY tp.nombre HAVING division_resultado >= 0.85"
                    cursor.execute(consulta)
                    resultado = cursor.fetchall()
                    print(resultado)
                    if resultado:
                        mensaje = "ALERTA: Productos con stock inferior al 15%:\n\n"
                        for producto, division in resultado:
                            mensaje += f"{producto}: {division:.2f}\n"
                        messagebox.showinfo("ALERTA!", mensaje)
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
            return


        self.ventana_secundaria.mainloop()
        
    def ver_usuario(self):
        self.toplevel_window = CON_Usuario()
        self.toplevel_window.grab_set() 
        
    def ver_ubicaciones(self):
        self.toplevel_window = CON_Ubicaciones()
        self.toplevel_window.grab_set() 
        
    def ver_productos(self):
        self.toplevel_window = CON_Producto()
        self.toplevel_window.grab_set() 
    
    def ver_inventario(self):
        self.toplevel_window = CON_Inventario()
        self.toplevel_window.grab_set() 
    
    def Ingreso_Movimiento(self):
        self.toplevel_window = Movimientos_Func()
        self.toplevel_window.grab_set() 
    
    def estadisticas_show(self):
        self.toplevel_window = Show_Estadisticas()
        self.toplevel_window.grab_set() 

class MOD_Usuario(ctk.CTkToplevel):    
    correo_control = ''
    
    def __init__(self):
        
        super().__init__()
        self.title("Usuarios")
        self.geometry("1000x550")
        self.minsize(1000,550)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
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
            global correo_control
            selected_item = tree.focus()
            if selected_item:
                row = tree.item(selected_item)['values']
                clear_cells()
                correo_control = (row[0])
                Entrada_Correo.insert(0,row[0])
                #Entrada_Responsable.insert(0,row[2])
                variable1.set(row[3])
            else:
                pass
        
        def eliminar_dato():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para eliminar', parent=self)
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
                            messagebox.showinfo('Éxito', 'Usuario eliminado con éxito', parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar', parent=self)
            else:
                Correo = Entrada_Correo.get()
                Rol = variable1.get()
                #Responsable = Entrada_Responsable.get()
                Seña = Entrada_Status.get()
                if not (Correo and Rol and Seña): #if not (Correo and Rol and Responsable and Seña):
                    messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
                else:
                    try:
                        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE jardineria.usuarios SET fecha_modificacion = NOW(), contraseña = %s, responsable = %s, rol_usuarios = %s, correo = %s WHERE correo = %s"
                                valores = (Seña,UsuarioRes,Rol,Correo,correo_control)
                                cursor.execute(consulta,valores)
                                # Confirmar los cambios en la base de datos
                                conexion.commit()
                                # Mostrar mensaje de éxito
                                messagebox.showinfo('Éxito', 'Usuario actualizado correctamente',parent=self)
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
            Rol = variable1.get()
            Responsable = UsuarioRes                                        #Entrada_Responsable.get()
            Seña = Entrada_Status.get()
            
            if not (Correo and Rol and Responsable and Seña):
                messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
            elif Correo_exist(Correo):
                messagebox.showerror('Error', 'El usuario ya existe', parent=self)
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
                            messagebox.showinfo('Éxito', 'Usuario agregado correctamente',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def clear_cells(*clicked):
            if clicked:
                tree.selection_remove(tree.focus())
            Entrada_Correo.delete(0,END)
            #Entrada_Responsable.delete(0,END)
            variable1.set('colaborador')
            Entrada_Status.delete(0,END)
            Entrada_Status.configure(self,show='*',placeholder_text='************',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        
        #Formato página
        Etiqueta_Correo = ctk.CTkLabel(self,font=font1,text='Correo:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Correo.place(relx=0.03, rely=0.05)
        Entrada_Correo = ctk.CTkEntry(self,placeholder_text='example@gmail.com',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        Entrada_Correo.place(relx=0.13, rely=0.05)
        Etiqueta_rol = ctk.CTkLabel(self,font=font1,text='Rol:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_rol.place(relx=0.03, rely=0.17)
        options = ['admin','colaborador']
        variable1 = ctk.StringVar()
        OpcionesRol = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=variable1,values=options,state='readonly',bg_color='#D1F2EB')
        OpcionesRol.set('colaborador')
        OpcionesRol.place(relx=0.13, rely=0.17)
        EtiquetaStatus = ctk.CTkLabel(self,font=font1,text='Contraseña:',text_color='#000',bg_color='#D1F2EB')
        EtiquetaStatus.place(relx=0.03, rely=0.29, anchor='nw')
        Entrada_Status = ctk.CTkEntry(self,show='*',placeholder_text='************',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        Entrada_Status.place(relx=0.13, rely=0.29, anchor='nw')
        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Usuario',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(relx=0.02, rely=0.58, relwidth=0.29, relheight=0.065)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(relx=0.02, rely=0.68, relwidth=0.29, relheight=0.065)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(relx=0.02, rely=0.78, relwidth=0.29, relheight=0.065)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(relx=0.02, rely=0.88, relwidth=0.29, relheight=0.065)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Correo','Modificación','Responsable','Rol')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Correo',anchor=tk.W,width=165)
        tree.column('Modificación',anchor=tk.W,width=165)
        tree.column('Responsable',anchor=tk.W,width=165)
        tree.column('Rol',anchor=tk.W,width=165)
        tree.heading('Correo',text='Correo')
        tree.heading('Modificación',text='Última Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.heading('Rol',text='Rol')
        tree.place(relx=0.36, rely=0.05, anchor='nw', relwidth=0.6, relheight=0.90)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()
        conexion.close()
        
class MOD_Producto(ctk.CTkToplevel):
    correo_control = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("1000x550")
        self.minsize(1000,550)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
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
            global sku_control
            selected_item = tree.focus()
            if selected_item:
                row = tree.item(selected_item)['values']
                clear_cells()
                #guardamos correo control para después
                sku_control = (row[0])
                Entrada_Nombre.insert(0,row[1])
                Entrada_Descripcion.insert(0,row[2])
                #Entrada_Responsable.insert(0,row[4])
                textoSKUC = row[0]
                textoSKU = textoSKUC.split('-')[0].strip()
                if textoSKU == 'ACC':
                    variableSKU.set('ACCESORIO')
                elif textoSKU == 'PLT':
                    variableSKU.set('PLANTA')
                elif textoSKU == 'DEC':
                    variableSKU.set('DECORACIÓN')
            else:
                pass
        def eliminar_dato():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para eliminar', parent=self)
            else:
                ElSku = sku_control
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "DELETE FROM jardineria.tipo_producto WHERE sku = %s"
                            valores = (ElSku,)
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Producto eliminado con éxito',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar', parent=self)
            else:
                ElSkuTipo = variableSKU.get()
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "SELECT * FROM jardineria.sku_dedicada"
                            cursor.execute(consulta)
                            obtenido = cursor.fetchall()
                            if ElSkuTipo == 'ACCESORIO':
                                CUALes='ACC'
                                DedicadaCual= 'ACCSKU'
                                cantidad = obtenido[0][0]
                            elif ElSkuTipo == 'PLANTA':
                                CUALes='PLT'
                                DedicadaCual='PLTSKU'
                                cantidad = obtenido[0][1]
                            elif ElSkuTipo == 'DECORACIÓN':
                                CUALes='DEC'
                                DedicadaCual='DECSKU'
                                cantidad = obtenido[0][2]
                            resultado = (int(cantidad)+1)
                            ElSku = (f"{CUALes}-{resultado}")
                            consulta = f"UPDATE jardineria.sku_dedicada SET {DedicadaCual} = {resultado} LIMIT 1"
                            cursor.execute(consulta)
                            conexion.commit()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")     

                Nombre = Entrada_Nombre.get()
                Responsable = UsuarioRes#Entrada_Responsable.get()
                Descripcion = Entrada_Descripcion.get()
                if not (ElSku and Nombre and Responsable and Descripcion):
                    messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
                else:
                    try:
                        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE jardineria.tipo_producto SET fecha_modificacion = NOW(), sku = %s, responsable = %s, descripcion = %s, nombre = %s WHERE sku = %s"
                                valores = (ElSku,Responsable,Descripcion,Nombre,sku_control)
                                cursor.execute(consulta,valores)
                                # Confirmar los cambios en la base de datos
                                conexion.commit()
                                # Mostrar mensaje de éxito
                                messagebox.showinfo('Éxito', 'Producto actualizado correctamente',parent=self)
                                # Actualizar la vista de Treeview
                                add_to_treeview()

                    except mysql.connector.Error as err:
                        print(f"Error de MySQL: {err}")

        def sku_exist(sku):
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT COUNT(*) FROM jardineria.tipo_producto WHERE sku = %s;"
                        cursor.execute(consulta, (sku,))
                        resultado = cursor.fetchone()
                return resultado[0] > 0
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
                return False
        #funciones
        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT sku,nombre,descripcion,fecha_modificacion,responsable FROM jardineria.tipo_producto"
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
            ElSkuTipo = variableSKU.get()
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT * FROM jardineria.sku_dedicada"
                        cursor.execute(consulta)
                        obtenido = cursor.fetchall()
                        if ElSkuTipo == 'ACCESORIO':
                            CUALes='ACC'
                            DedicadaCual= 'ACCSKU'
                            cantidad = obtenido[0][0]
                        elif ElSkuTipo == 'PLANTA':
                            CUALes='PLT'
                            DedicadaCual='PLTSKU'
                            cantidad = obtenido[0][1]
                        elif ElSkuTipo == 'DECORACIÓN':
                            CUALes='DEC'
                            DedicadaCual='DECSKU'
                            cantidad = obtenido[0][2]
                        resultado = (int(cantidad)+1)
                        ElSku = (f"{CUALes}-{resultado}")

                        consulta = f"UPDATE jardineria.sku_dedicada SET {DedicadaCual} = {resultado} LIMIT 1"
                        cursor.execute(consulta)
                        conexion.commit()

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
            Nombre = Entrada_Nombre.get()
            Responsable = UsuarioRes#Entrada_Responsable.get()
            Descripcion = Entrada_Descripcion.get()
            
            if not (ElSku and Nombre and Responsable and Descripcion):
                messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
            elif sku_exist(ElSku):
                messagebox.showerror('Error', 'El producto ya existe', parent=self)
            else:
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO jardineria.tipo_producto (sku, nombre, fecha_modificacion, responsable, descripcion) VALUES (%s,%s,NOW(),%s,%s)"
                            valores = (ElSku,Nombre,Responsable,Descripcion)
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Producto agregado correctamente',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def clear_cells(*clicked):
            if clicked:
                tree.selection_remove(tree.focus())
            variableSKU.set('PLANTA')
            #Entrada_Responsable.delete(0,END)
            Entrada_Nombre.delete(0,END)
            Entrada_Descripcion.delete(0,END)
        
        #Formato página
        Etiqueta_SKU = ctk.CTkLabel(self,font=font1,text='Tipo:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_SKU.place(relx=0.03, rely=0.05)
        optionsSKU = ['PLANTA','ACCESORIO','DECORACIÓN']
        variableSKU = ctk.StringVar()
        OpcionesSKU = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=variableSKU,values=optionsSKU,state='readonly',bg_color='#D1F2EB')
        OpcionesSKU.set('PLANTA')
        OpcionesSKU.place(relx=0.13, rely=0.05)
        Etiqueta_Nombre = ctk.CTkLabel(self,font=font1,text='Nombre:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Nombre.place(relx=0.03, rely=0.17)
        Entrada_Nombre = ctk.CTkEntry(self,placeholder_text='Producto...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        Entrada_Nombre.place(relx=0.13, rely=0.17)
        Etiqueta_Descripcion = ctk.CTkLabel(self,font=font1,text='Descripción:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Descripcion.place(relx=0.03, rely=0.29)
        Entrada_Descripcion = ctk.CTkEntry(self,placeholder_text='Descripción...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        Entrada_Descripcion.place(relx=0.13, rely=0.29)

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Producto',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(relx=0.02, rely=0.58, relwidth=0.29, relheight=0.065)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(relx=0.02, rely=0.68, relwidth=0.29, relheight=0.065)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(relx=0.02, rely=0.78, relwidth=0.29, relheight=0.065)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(relx=0.02, rely=0.88, relwidth=0.29, relheight=0.065)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('SKU','Nombre','Descripcion','Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('SKU',anchor=tk.W,width=80)
        tree.column('Nombre',anchor=tk.W,width=130)
        tree.column('Descripcion',anchor=tk.W,width=240)
        tree.column('Modificación',anchor=tk.W,width=140)
        tree.column('Responsable',anchor=tk.W,width=100)
        tree.heading('SKU',text='SKU')
        tree.heading('Nombre',text='Nombre Producto')
        tree.heading('Descripcion',text='Descripcion')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(relx=0.36, rely=0.05, anchor='nw', relwidth=0.6, relheight=0.90)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()

class MOD_Ubicaciones(ctk.CTkToplevel):
    cod_control = 0
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.title("Ubicaciones")
        self.geometry("1000x550")
        self.minsize(1000,550)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
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
            global cod_control
            selected_item = tree.focus()
            row = tree.item(selected_item)['values']
            clear_cells()
            if selected_item:
                nombre = (row[1])
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "SELECT * FROM jardineria.ubicaciones WHERE nombre = %s"
                            valores = (nombre,)
                            cursor.execute(consulta,valores)
                            restulado = cursor.fetchall()
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")
                cod_control = (int(restulado[0][0]))
                Entrada_Nombre.insert(0,row[1])
                #Entrada_Responsable.insert(0,row[4])
                Entrada_Descripcion.insert(0,row[2])
            else:
                pass
        def eliminar_dato():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para eliminar', parent=self)
            else:
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            nombre = Entrada_Nombre.get()
                            consulta = "SELECT * FROM jardineria.ubicaciones WHERE nombre = %s"
                            valores = (nombre,)
                            cursor.execute(consulta,valores)
                            restulado = cursor.fetchall()
                            ID_Ubi = restulado[0][0]
                            consulta = "DELETE FROM jardineria.ubicaciones WHERE cod_ubi = %s"
                            valores = (ID_Ubi,)
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Ubicación eliminada con éxito',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar', parent=self)
            else:
                Nombre = Entrada_Nombre.get()
                Descripcion = Entrada_Descripcion.get()
                Responsable = UsuarioRes#Entrada_Responsable.get()
                if not (Nombre and Descripcion and Responsable):
                    messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
                else:
                    try:
                        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                            with conexion.cursor() as cursor:
                                consulta = "UPDATE jardineria.ubicaciones SET fecha_modificacion = NOW(), nombre = %s, responsable = %s, descripcion = %s WHERE cod_ubi = %s"
                                valores = (Nombre,Responsable,Descripcion,cod_control)
                                cursor.execute(consulta,valores)
                                # Confirmar los cambios en la base de datos
                                conexion.commit()
                                # Mostrar mensaje de éxito
                                messagebox.showinfo('Éxito', 'Ubicación actualizada correctamente',parent=self)
                                # Actualizar la vista de Treeview
                                add_to_treeview()

                    except mysql.connector.Error as err:
                        print(f"Error de MySQL: {err}")

        def ID_exist(nombre):
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT COUNT(*) FROM jardineria.ubicaciones WHERE nombre = %s;"
                        cursor.execute(consulta, (nombre,))
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
                        consulta = "SELECT cod_ubi,nombre,descripcion,fecha_modificacion,responsable FROM jardineria.ubicaciones"
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
            Nombre = Entrada_Nombre.get()
            Descripcion = Entrada_Descripcion.get()
            Responsable = UsuarioRes#Entrada_Responsable.get()
            
            if not (Descripcion and Nombre and Responsable):
                messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
            elif ID_exist(Nombre):
                messagebox.showerror('Error', 'La ubicación ya existe', parent=self)
            else:
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "INSERT INTO jardineria.ubicaciones (descripcion,fecha_modificacion,responsable,nombre) values (%s,NOW(),%s,%s)"
                            valores = (Descripcion,Responsable,Nombre)
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Ubicación agregada correctamente',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()

                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def clear_cells(*clicked):
            if clicked:
                tree.selection_remove(tree.focus())
            Entrada_Nombre.delete(0,END)
            #Entrada_Responsable.delete(0,END)
            Entrada_Descripcion.delete(0,END)

        Etiqueta_Nombre = ctk.CTkLabel(self,font=font1,text='Nombre:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Nombre.place(relx=0.03, rely=0.05)
        Entrada_Nombre = ctk.CTkEntry(self,placeholder_text='Nombre...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        Entrada_Nombre.place(relx=0.13, rely=0.05)
        Etiqueta_Descripcion = ctk.CTkLabel(self,font=font1,text='Descripcion:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Descripcion.place(relx=0.03, rely=0.17)
        Entrada_Descripcion = ctk.CTkEntry(self,placeholder_text='Descripcion...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#D1F2EB')
        Entrada_Descripcion.place(relx=0.13, rely=0.17)

        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Ubicación',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(relx=0.02, rely=0.58, relwidth=0.29, relheight=0.065)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(relx=0.02, rely=0.68, relwidth=0.29, relheight=0.065)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(relx=0.02, rely=0.78, relwidth=0.29, relheight=0.065)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(relx=0.02, rely=0.88, relwidth=0.29, relheight=0.065)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Orden Ubicación','Nombre','Descripción','Fecha Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Orden Ubicación',anchor=tk.W,width=120)
        tree.column('Nombre',anchor=tk.W,width=120)
        tree.column('Descripción',anchor=tk.W,width=120)
        tree.column('Fecha Modificación',anchor=tk.W,width=120)
        tree.column('Responsable',anchor=tk.W,width=120)
        tree.heading('Orden Ubicación',text='Orden Ubicación')
        tree.heading('Nombre',text='Nombre')
        tree.heading('Descripción',text='Descripción')
        tree.heading('Fecha Modificación',text='Fecha Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(relx=0.36, rely=0.05, anchor='nw', relwidth=0.6, relheight=0.90)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()

class MOD_Inventario(ctk.CTkToplevel):
    sku_control = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inventario")
        self.geometry("1000x550")
        self.minsize(1000,550)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
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
            global sku_control,ubi_control
            selected_item = tree.focus()
            if selected_item:
                row = tree.item(selected_item)['values']
                clear_cells()
                sku_control = (row[0])
                ubi_control = (row[2])
                Entrada_Cantidad.insert(0,row[1])
                #Entrada_Responsable.insert(0,row[4])
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "SELECT nombre FROM jardineria.tipo_producto WHERE sku = %s"
                            val = (sku_control,)
                            consulta2 = "SELECT nombre FROM jardineria.ubicaciones WHERE cod_ubi  = %s"
                            cursor.execute(consulta,val)
                            resultado = cursor.fetchall()
                            # Confirmar los cambios en la base de datos
                            val2 =(ubi_control,)
                            cursor.execute(consulta2,val2)
                            Ubiresultado = cursor.fetchall()
                            conexion.commit()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")
                VarProducto.set(resultado[0][0])
                VarUbicacion.set(Ubiresultado[0][0])
            else:
                pass
        def eliminar_dato():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para eliminar', parent=self)
            else:
                nombre = VarProducto.get()
                nombreubi = VarUbicacion.get()
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            getSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                            getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                            consulta = "DELETE FROM jardineria.inventario WHERE sku = %s AND cod_ubicacion = %s"
                            lista=(nombre,)
                            cursor.execute(getSKU,lista)
                            sku = cursor.fetchall()
                            lista=(nombreubi,)
                            cursor.execute(getUBI,lista)
                            ubi = cursor.fetchall()
                            valores = (sku[0][0],ubi[0][0])
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Segmento de Inventario eliminado con éxito',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar', parent=self)
            else:
                nombre = VarProducto.get()
                nombreubi = VarUbicacion.get()
                Responsable = UsuarioRes#Entrada_Responsable.get()
                cantidad = Entrada_Cantidad.get()
                if not (nombre and nombreubi and Responsable and cantidad):
                    messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
                else:
                    try:
                        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                            with conexion.cursor() as cursor:
                                getSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                                getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                                consulta = "DELETE FROM jardineria.inventario WHERE sku = %s AND cod_ubicacion = %s"
                                lista=(nombre,)
                                cursor.execute(getSKU,lista)
                                sku = cursor.fetchall()
                                lista=(nombreubi,)
                                cursor.execute(getUBI,lista)
                                ubi = cursor.fetchall()
                                consulta = "UPDATE jardineria.inventario SET fecha_modificacion = NOW(), sku = %s, responsable = %s, cod_ubicacion = %s, cantidad = %s WHERE sku = %s AND cod_ubicacion = %s"
                                valores = (sku[0][0],Responsable,ubi[0][0],cantidad,sku_control,ubi_control)
                                cursor.execute(consulta,valores)
                                # Confirmar los cambios en la base de datos
                                conexion.commit()
                                # Mostrar mensaje de éxito
                                messagebox.showinfo('Éxito', 'Segmento de Inventario actualizado correctamente',parent=self)
                                # Actualizar la vista de Treeview
                                add_to_treeview()
                    except mysql.connector.Error as err:
                        print(f"Error de MySQL: {err}")

        def sku_exist(sku,cod_ubi):
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT COUNT(*) FROM jardineria.inventario WHERE sku = %s AND cod_ubicacion = %s"
                        cursor.execute(consulta, (sku,cod_ubi))
                        resultado = cursor.fetchone()
                return resultado[0] > 0
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
                return False
        #funciones
        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT sku,cantidad,cod_ubicacion,fecha_modificacion,responsable FROM jardineria.inventario"
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
            sku = VarProducto.get()
            cantidad = Entrada_Cantidad.get()
            Responsable = UsuarioRes#Entrada_Responsable.get()
            cod_ubi = VarUbicacion.get()
            
            if not (sku and cantidad and Responsable and cod_ubi):
                messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
            elif sku_exist(sku,cod_ubi):
                messagebox.showerror('Error', 'El producto ya existe en esa ubicación', parent=self)
            else:
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            obtenerSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                            val = (sku,)
                            obtenerUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre  = %s"
                            cursor.execute(obtenerSKU,val)
                            SKUresultado = cursor.fetchall()
                            # Confirmar los cambios en la base de datos
                            val2 =(cod_ubi,)
                            cursor.execute(obtenerUBI,val2)
                            Ubiresultado = cursor.fetchall()
                            consulta = "INSERT INTO jardineria.inventario (fecha_modificacion, sku, cantidad, responsable, cod_ubicacion) VALUES (NOW(),%s,%s,%s,%s)"
                            valores = (SKUresultado[0][0],cantidad,Responsable,Ubiresultado[0][0])
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Segmento de Inventario agregado correctamente',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def clear_cells(*clicked):
            if clicked:
                tree.selection_remove(tree.focus())
            Entrada_Cantidad.delete(0,END)
            #Entrada_Responsable.delete(0,END)
            VarProducto.set('Producto')
            VarUbicacion.set('Ubicación')

        #Formato página
        Etiqueta_Producto = ctk.CTkLabel(self,font=font1,text='Producto:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Producto.place(relx=0.03, rely=0.05, anchor='nw')
        try:
            with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                with conexion.cursor() as cursor:
                    consulta = "SELECT nombre FROM jardineria.tipo_producto"
                    consulta2 = "SELECT nombre FROM jardineria.ubicaciones"
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    # Confirmar los cambios en la base de datos
                    cursor.execute(consulta2)
                    Ubiresultados = cursor.fetchall()
                    conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
        OptProducto = [resultado[0] for resultado in resultados]
        VarProducto = ctk.StringVar()
        OpcionesProducto = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarProducto,values=OptProducto,state='readonly',bg_color='#D1F2EB')
        OpcionesProducto.set('Productos')
        OpcionesProducto.place(relx=0.13, rely=0.05, anchor='nw')
        Etiqueta_Cantidad = ctk.CTkLabel(self,font=font1,text='Cantidad:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Cantidad.place(relx=0.03, rely=0.17, anchor='nw')
        Entrada_Cantidad = tk.Spinbox(self, from_=0, to=9999, font=font1,borderwidth=3,width=18)
        Entrada_Cantidad.place(relx=0.13, rely=0.17, anchor='nw')
        Etiqueta_Ubicacion = ctk.CTkLabel(self,font=font1,text='Ubicación:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Ubicacion.place(relx=0.03, rely=0.29, anchor='nw')
        OptUbicacion = [resultado[0] for resultado in Ubiresultados]
        VarUbicacion = ctk.StringVar()
        OpcionesUbicaciones = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarUbicacion,values=OptUbicacion,state='readonly',bg_color='#D1F2EB')
        OpcionesUbicaciones.set('Ubicación')
        OpcionesUbicaciones.place(relx=0.13, rely=0.29, anchor='nw')

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Segmento',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(relx=0.02, rely=0.58, anchor='nw', relwidth=0.29, relheight=0.065)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(relx=0.02, rely=0.68, anchor='nw', relwidth=0.29, relheight=0.065)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(relx=0.02, rely=0.78, anchor='nw', relwidth=0.29, relheight=0.065)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(relx=0.02, rely=0.88, anchor='nw', relwidth=0.29, relheight=0.065)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Codigo','Cantidad','Ubicación','Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Codigo',anchor=tk.W,width=120)
        tree.column('Cantidad',anchor=tk.W,width=120)
        tree.column('Ubicación',anchor=tk.W,width=120)
        tree.column('Modificación',anchor=tk.W,width=160)
        tree.column('Responsable',anchor=tk.W,width=120)
        tree.heading('Codigo',text='Codigo')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(relx=0.36, rely=0.05, anchor='nw', relwidth=0.6, relheight=0.90)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()

class MOD_Movimiento(ctk.CTkToplevel):
    sku_control = ''
    fecha_control = ''
    ubi_control = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Movimientos")
        self.geometry("1000x550")
        self.minsize(1000,550)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
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
            global sku_control,fecha_control,ubi_control
            selected_item = tree.focus()
            if selected_item:
                row = tree.item(selected_item)['values']
                clear_cells()
                sku_control = (row[0])
                ubi_control = (row[4])
                fecha_control = (row[1])
                Entrada_Cantidad.insert(0,row[2])
                VarRazon.set(row[3])
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            consulta = "SELECT nombre FROM jardineria.tipo_producto WHERE sku = %s"
                            val = (sku_control,)
                            cursor.execute(consulta,val)
                            resultado = cursor.fetchall()
                            consulta2 = "SELECT nombre FROM jardineria.ubicaciones WHERE cod_ubi  = %s"
                            val2 =(ubi_control,)
                            cursor.execute(consulta2,val2)
                            Ubiresultado = cursor.fetchall()
                            # Confirmar los cambios en la base de datos
                            VarProducto.set(resultado[0][0])
                            VarUbicacion.set(Ubiresultado[0][0])
                            conexion.commit()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")
            else:
                pass
        def eliminar_dato():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para eliminar', parent=self)
            else:
                nombre = VarProducto.get()
                ubiname = VarUbicacion.get()
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            getSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                            getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                            consulta = "DELETE FROM jardineria.movimiento WHERE sku = %s AND ubicacion = %s AND fecha = %s"
                            cursor.execute(getSKU,(nombre,))
                            sku = cursor.fetchall()
                            cursor.execute(getUBI,(ubiname,))
                            ubi = cursor.fetchall()
                            cursor.execute(consulta,(sku[0][0],ubi[0][0],fecha_control))
                            # Confirmar los cambios en la base de datos
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Movimiento eliminado con éxito',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar', parent=self)
            else:
                nombre = VarProducto.get()
                nombreubi = VarUbicacion.get()
                Razon = VarRazon.get()
                Ubicacion = VarUbicacion.get()
                cantidad = Entrada_Cantidad.get()
                Responsable = UsuarioRes
                Fecha = fecha_control
                if not (nombre and nombreubi and Ubicacion and cantidad):
                    messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
                else:
                    try:
                        with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                            with conexion.cursor() as cursor:
                                getSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                                getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                                lista=(nombre,)
                                cursor.execute(getSKU,lista)
                                sku = cursor.fetchall()
                                lista=(nombreubi,)
                                cursor.execute(getUBI,lista)
                                ubi = cursor.fetchall()
                                consulta = "UPDATE jardineria.movimiento SET razon = %s, fecha_modificacion = NOW(), sku = %s, responsable = %s, ubicacion = %s, cantidad = %s WHERE sku = %s AND ubicacion = %s AND fecha = %s"
                                valores = (Razon,sku[0][0],Responsable,ubi[0][0],cantidad,sku_control,ubi_control,Fecha)
                                cursor.execute(consulta,valores)
                                # Confirmar los cambios en la base de datos
                                conexion.commit()
                                # Mostrar mensaje de éxito
                                messagebox.showinfo('Éxito', 'Movimiento actualizado correctamente',parent=self)
                                # Actualizar la vista de Treeview
                                add_to_treeview()
                    except mysql.connector.Error as err:
                        print(f"Error de MySQL: {err}")
        #funciones
        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT sku,fecha,cantidad,razon,ubicacion,fecha_modificacion,responsable FROM jardineria.movimiento"
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
            sku = VarProducto.get()
            ubi = VarUbicacion.get()
            cantidad = Entrada_Cantidad.get()
            Responsable = UsuarioRes
            Razon = VarRazon.get()
            if not (sku and cantidad and Responsable and Razon):
                messagebox.showerror('Error', 'No pueden faltar campos', parent=self)
            else:
                try:
                    with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                        with conexion.cursor() as cursor:
                            obtenerSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                            val = (sku,)
                            cursor.execute(obtenerSKU,val)
                            SKUresultado = cursor.fetchall()

                            getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                            valores = (ubi,)
                            cursor.execute(getUBI,valores)
                            Ubires = cursor.fetchall()

                            # Confirmar los cambios en la base de datos
                            consulta = "INSERT INTO jardineria.movimiento (fecha,fecha_modificacion, sku, cantidad, responsable, razon, ubicacion) VALUES (NOW(),NOW(),%s,%s,%s,%s,%s)"
                            valores = (SKUresultado[0][0],cantidad,Responsable,Razon,Ubires[0][0])
                            cursor.execute(consulta,valores)
                            # Confirmar los cambios en la base de datos
                            #inicializar inventario
                            inicializa = "INSERT INTO inventario (cantidad, sku, cod_ubicacion) SELECT 0, %s, %s FROM dual WHERE NOT EXISTS( SELECT 1 FROM inventario WHERE sku = %s AND cod_ubicacion = %s)"
                            ponefecha = "UPDATE inventario SET fecha_modificacion = NOW(), responsable = %s WHERE sku = %s AND cod_ubicacion = %s"
                            valinicia = (SKUresultado[0][0],Ubires[0][0],SKUresultado[0][0],Ubires[0][0])
                            cursor.execute(inicializa,valinicia)
                            cursor.execute(ponefecha,(Responsable,SKUresultado[0][0],Ubires[0][0]))
                            #cambiar inventario
                            obtenerInventario = "SELECT cantidad FROM jardineria.inventario WHERE sku = %s AND cod_ubicacion = %s"
                            cursor.execute(obtenerInventario, (SKUresultado[0][0], Ubires[0][0]))
                            InventarioAnterior=cursor.fetchall()
                            modificarInventario = "UPDATE inventario SET cantidad = %s WHERE sku = %s AND cod_ubicacion = %s"
                            if(Razon == 'Compra' or Razon == 'Repuesto'):
                                cambio = int(InventarioAnterior[0][0])+int(cantidad)
                            else:
                                cambio = int(InventarioAnterior[0][0])-int(cantidad)
                            lista = (cambio,SKUresultado[0][0],Ubires[0][0])
                            cursor.execute(modificarInventario,lista)
                            conexion.commit()
                            # Mostrar mensaje de éxito
                            messagebox.showinfo('Éxito', 'Movimiento agregado correctamente',parent=self)
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")

        def clear_cells(*clicked):
            if clicked:
                tree.selection_remove(tree.focus())
            Entrada_Cantidad.delete(0,END)
            VarUbicacion.set('Ubicación')
            VarProducto.set('Producto')
            VarRazon.set('Compra Proveedor')

        #Formato página
        Etiqueta_Producto = ctk.CTkLabel(self,font=font1,text='Producto:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Producto.place(relx=0.03, rely=0.05, anchor='nw')
        try:
            with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                with conexion.cursor() as cursor:
                    consulta = "SELECT nombre FROM jardineria.tipo_producto"
                    consulta2 = "SELECT nombre FROM jardineria.ubicaciones"
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    # Confirmar los cambios en la base de datos
                    cursor.execute(consulta2)
                    Ubiresultados = cursor.fetchall()
                    conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
        OptProducto = [resultado[0] for resultado in resultados]
        VarProducto = ctk.StringVar()
        OpcionesProducto = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarProducto,values=OptProducto,state='readonly',bg_color='#D1F2EB')
        OpcionesProducto.set('Productos')
        OpcionesProducto.place(relx=0.13, rely=0.05, anchor='nw')
        Etiqueta_Cantidad = ctk.CTkLabel(self,font=font1,text='Cantidad:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Cantidad.place(relx=0.03, rely=0.17, anchor='nw')
        Entrada_Cantidad = tk.Spinbox(self, from_=0, to=9999, font=font1,borderwidth=3,width=18)
        Entrada_Cantidad.place(relx=0.13, rely=0.17, anchor='nw')
        Etiqueta_razon = ctk.CTkLabel(self,font=font1,text='Motivo:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_razon.place(relx=0.03, rely=0.29, anchor='nw')
        razones = ['Compra','Venta','Merma','Baja','Repuesto']
        VarRazon = ctk.StringVar()
        OpcionesRazon = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarRazon,values=razones,state='readonly',bg_color='#D1F2EB')
        OpcionesRazon.set('Compra')
        OpcionesRazon.place(relx=0.13, rely=0.29, anchor='nw')
        Etiqueta_Ubicacion = ctk.CTkLabel(self,font=font1,text='Ubicación:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_Ubicacion.place(relx=0.03, rely=0.42, anchor='nw')
        OptUbicacion = [resultado[0] for resultado in Ubiresultados]
        VarUbicacion = ctk.StringVar()
        OpcionesUbicaciones = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarUbicacion,values=OptUbicacion,state='readonly',bg_color='#D1F2EB')
        OpcionesUbicaciones.set('Ubicación')
        OpcionesUbicaciones.place(relx=0.13, rely=0.42, anchor='nw')

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Movimiento',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(relx=0.02, rely=0.58, anchor='nw', relwidth=0.29, relheight=0.065)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(relx=0.02, rely=0.68, anchor='nw', relwidth=0.29, relheight=0.065)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(relx=0.02, rely=0.78, anchor='nw', relwidth=0.29, relheight=0.065)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(relx=0.02, rely=0.88, anchor='nw', relwidth=0.29, relheight=0.065)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Producto','Fecha Movimiento','Cantidad','Motivo','Ubicación','Ultima Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Producto',anchor=tk.W,width=80)
        tree.column('Fecha Movimiento',anchor=tk.W,width=160)
        tree.column('Cantidad',anchor=tk.W,width=60)
        tree.column('Motivo',anchor=tk.W,width=80)
        tree.column('Ubicación',anchor=tk.W,width=70)
        tree.column('Ultima Modificación',anchor=tk.W,width=160)
        tree.column('Responsable',anchor=tk.W,width=90)
        tree.heading('Producto',text='Producto')
        tree.heading('Fecha Movimiento',text='Fecha Movimiento')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Motivo',text='Motivo')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Ultima Modificación',text='Ultima Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(relx=0.36, rely=0.05, anchor='nw', relwidth=0.6, relheight=0.90)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()

class CON_Usuario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("600x400")
        self.minsize(600, 400)
        self.config(bg='#D1F2EB')
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        font1 = ('Helvetica', 14, 'bold')
        font2 = ('Helvetica', 12, 'bold')

        # BD connection
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            db='Jardineria'
        )

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
                            tree.insert('', tk.END, values=fila)

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

        def sort_treeview(col, reverse):
            # Obtener todos los elementos del Treeview
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # Ordenar los elementos según el tipo de dato de la columna
            if col == 'Modificación':
                # Ordenar por fecha
                data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=reverse)
            else:
                # Ordenar alfabéticamente
                data.sort(key=lambda x: (x[0], x[1]), reverse=reverse)

            # Reiniciar el Treeview con los elementos ordenados
            for index, item in enumerate(data):
                tree.move(item[1], '', index)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview', font=font2, foreground='#000', background='#D6D6D6', fieldbackground='#E9E0D1')
        style.map('Treeview', background=[('selected', '#B97E11')])

        tree = ttk.Treeview(self, height=19)
        tree['columns'] = ('Correo', 'Modificación', 'Responsable', 'Rol')
        tree.column('#0', width=0, stretch=tk.NO)  # esconde la primera
        tree.column('Correo', anchor=tk.W, width=165)
        tree.column('Modificación', anchor=tk.W, width=165)
        tree.column('Responsable', anchor=tk.W, width=165)
        tree.column('Rol', anchor=tk.W, width=165)
        tree.heading('Correo', text='Correo', command=lambda: sort_treeview('Correo', False))
        tree.heading('Modificación', text='Última Modificación', command=lambda: sort_treeview('Modificación', False))
        tree.heading('Responsable', text='Responsable', command=lambda: sort_treeview('Responsable', False))
        tree.heading('Rol', text='Rol', command=lambda: sort_treeview('Rol', False))
        tree.place(relx=0.05, rely=0.05, anchor='nw', relwidth=0.9, relheight=0.9)
        add_to_treeview()
        conexion.close()
     
class CON_Producto(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Productos")
        self.geometry("700x400")
        self.minsize(700, 400)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
        font1 = ('Helvetica', 14, 'bold')
        font2 = ('Helvetica', 12, 'bold')

        # BD connection
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            db='Jardineria'
        )

        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT sku,nombre,descripcion,fecha_modificacion,responsable FROM jardineria.tipo_producto"
                        cursor.execute(consulta)
                        resultado = cursor.fetchall()

                        # Borrar todos los elementos actuales en el Treeview
                        tree.delete(*tree.get_children())

                        # Insertar los nuevos datos en el Treeview
                        for fila in resultado:
                            tree.insert('', tk.END, values=fila)
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

        def sort_treeview(col, reverse):
            # Obtener todos los elementos del Treeview
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # Ordenar los elementos según el tipo de dato de la columna
            if col == 'Modificación':
                # Ordenar por fecha
                data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=reverse)
            else:
                # Ordenar alfabéticamente
                data.sort(key=lambda x: (x[0], x[1]), reverse=reverse)

            # Reiniciar el Treeview con los elementos ordenados
            for index, item in enumerate(data):
                tree.move(item[1], '', index)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview', font=font2, foreground='#000', background='#D6D6D6', fieldbackground='#E9E0D1')
        style.map('Treeview', background=[('selected', '#B97E11')])

        tree = ttk.Treeview(self, height=19)
        tree['columns'] = ('SKU', 'Nombre', 'Descripcion', 'Modificación', 'Responsable')
        tree.column('#0', width=0, stretch=tk.NO)  # esconde la primera
        tree.column('SKU', anchor=tk.W, width=80)
        tree.column('Nombre', anchor=tk.W, width=130)
        tree.column('Descripcion', anchor=tk.W, width=240)
        tree.column('Modificación', anchor=tk.W, width=140)
        tree.column('Responsable', anchor=tk.W, width=100)
        tree.heading('SKU', text='SKU', command=lambda: sort_treeview('SKU', False))
        tree.heading('Nombre', text='Nombre Producto', command=lambda: sort_treeview('Nombre', False))
        tree.heading('Descripcion', text='Descripcion', command=lambda: sort_treeview('Descripcion', False))
        tree.heading('Modificación', text='Modificación', command=lambda: sort_treeview('Modificación', False))
        tree.heading('Responsable', text='Responsable', command=lambda: sort_treeview('Responsable', False))
        tree.place(relx=0.05, rely=0.05, anchor='nw', relwidth=0.90, relheight=0.90)
        add_to_treeview()
        conexion.close()

class CON_Ubicaciones(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ubicaciones")
        self.geometry("700x400")
        self.minsize(700, 400)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
        font1 = ('Helvetica', 14, 'bold')
        font2 = ('Helvetica', 12, 'bold')

        # BD connection
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            db='Jardineria'
        )

        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT cod_ubi,nombre,descripcion,fecha_modificacion,responsable FROM jardineria.ubicaciones"
                        cursor.execute(consulta)
                        resultado = cursor.fetchall()

                        # Borrar todos los elementos actuales en el Treeview
                        tree.delete(*tree.get_children())

                        # Insertar los nuevos datos en el Treeview
                        for fila in resultado:
                            tree.insert('', tk.END, values=fila)

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

        def sort_treeview(col, reverse):
            # Obtener todos los elementos del Treeview
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # Ordenar los elementos según el tipo de dato de la columna
            if col == 'Fecha Modificación':
                # Ordenar por fecha
                data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=reverse)
            else:
                # Ordenar alfabéticamente
                data.sort(key=lambda x: (x[0], x[1]), reverse=reverse)

            # Reiniciar el Treeview con los elementos ordenados
            for index, item in enumerate(data):
                tree.move(item[1], '', index)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview', font=font2, foreground='#000', background='#D6D6D6', fieldbackground='#E9E0D1')
        style.map('Treeview', background=[('selected', '#B97E11')])

        tree = ttk.Treeview(self, height=19)
        tree['columns'] = ('Orden Ubicación', 'Nombre', 'Descripción', 'Fecha Modificación', 'Responsable')
        tree.column('#0', width=0, stretch=tk.NO)  # esconde la primera
        tree.column('Orden Ubicación', anchor=tk.W, width=120)
        tree.column('Nombre', anchor=tk.W, width=120)
        tree.column('Descripción', anchor=tk.W, width=120)
        tree.column('Fecha Modificación', anchor=tk.W, width=120)
        tree.column('Responsable', anchor=tk.W, width=120)
        tree.heading('Orden Ubicación', text='Orden Ubicación', command=lambda: sort_treeview('Orden Ubicación', False))
        tree.heading('Nombre', text='Nombre', command=lambda: sort_treeview('Nombre', False))
        tree.heading('Descripción', text='Descripción', command=lambda: sort_treeview('Descripción', False))
        tree.heading('Fecha Modificación', text='Fecha Modificación', command=lambda: sort_treeview('Fecha Modificación', False))
        tree.heading('Responsable', text='Responsable', command=lambda: sort_treeview('Responsable', False))
        tree.place(relx=0.05, rely=0.05, anchor='nw', relwidth=0.90, relheight=0.90)
        add_to_treeview()
        conexion.close()

class CON_Inventario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inventario")
        self.geometry("700x400")
        self.minsize(700, 400)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
        font1 = ('Helvetica', 14, 'bold')
        font2 = ('Helvetica', 12, 'bold')

        # BD connection
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            db='Jardineria'
        )

        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT tp.nombre AS nombre, i.cantidad, u.nombre AS ubicacion, i.fecha_modificacion, i.responsable FROM jardineria.tipo_producto tp JOIN jardineria.inventario i ON tp.sku = i.sku JOIN jardineria.ubicaciones u ON i.cod_ubicacion = u.cod_ubi"
                        cursor.execute(consulta)
                        resultado = cursor.fetchall()

                        # Borrar todos los elementos actuales en el Treeview
                        tree.delete(*tree.get_children())

                        # Insertar los nuevos datos en el Treeview
                        for fila in resultado:
                            tree.insert('', tk.END, values=fila)
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

        def sort_treeview(col, reverse):
            # Obtener todos los elementos del Treeview
            data = [(tree.set(child, col), child) for child in tree.get_children('')]

            # Ordenar los elementos según el tipo de dato de la columna
            if col == 'Modificación':
                # Ordenar por fecha
                data.sort(key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=reverse)
            else:
                # Ordenar alfabéticamente
                data.sort(key=lambda x: (x[0], x[1]), reverse=reverse)

            # Reiniciar el Treeview con los elementos ordenados
            for index, item in enumerate(data):
                tree.move(item[1], '', index)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview', font=font2, foreground='#000', background='#D6D6D6', fieldbackground='#E9E0D1')
        style.map('Treeview', background=[('selected', '#B97E11')])

        tree = ttk.Treeview(self, height=19)
        tree['columns'] = ('Producto', 'Cantidad', 'Ubicación', 'Modificación', 'Responsable')
        tree.column('#0', width=0, stretch=tk.NO)  # esconde la primera
        tree.column('Producto', anchor=tk.W, width=120)
        tree.column('Cantidad', anchor=tk.W, width=120)
        tree.column('Ubicación', anchor=tk.W, width=120)
        tree.column('Modificación', anchor=tk.W, width=160)
        tree.column('Responsable', anchor=tk.W, width=120)
        tree.heading('Producto', text='Producto', command=lambda: sort_treeview('Producto', False))
        tree.heading('Cantidad', text='Cantidad', command=lambda: sort_treeview('Cantidad', False))
        tree.heading('Ubicación', text='Ubicación', command=lambda: sort_treeview('Ubicación', False))
        tree.heading('Modificación', text='Modificación', command=lambda: sort_treeview('Modificación', False))
        tree.heading('Responsable', text='Responsable', command=lambda: sort_treeview('Responsable', False))
        tree.place(relx=0.05, rely=0.05, anchor='nw', relwidth=0.90, relheight=0.90)
        add_to_treeview()
        conexion.close()

class Movimientos_Func(ctk.CTkToplevel):
    sku_control = ''
    fecha_control = ''
    ubi_control = ''
    def add_row(self):
        try:
            with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                with conexion.cursor() as cursor:
                    Ubiresultados = []
                    consulta = "SELECT nombre FROM jardineria.tipo_producto"
                    consulta2 = "SELECT nombre FROM jardineria.ubicaciones"
                    cursor.execute(consulta)
                    resultados = cursor.fetchall()
                    # Confirmar los cambios en la base de datos
                    cursor.execute(consulta2)
                    Ubiresultados = cursor.fetchall()
                    conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")

        font1 = ('Helvetica',14,'bold')
        font2 = ('Helvetica',12,'bold')
        new_row = ctk.CTkFrame(self.scroll_frame,fg_color='#D0FCF6',bg_color='#D0FCF6')
        new_row.pack(pady=5, side='top', expand=True, fill='x')
        
        label = ctk.CTkLabel(new_row,font=font1, text=f"Producto:",text_color='#000',bg_color='#D0FCF6')
        label.pack(side='left', padx=1, expand=True, fill='x')
        
        OptProducto = [resultado[0] for resultado in resultados]
        VarProducto = ctk.StringVar()
        OpcionesProducto = ctk.CTkComboBox(new_row,font=font1,width=80,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',variable=VarProducto,values=OptProducto,state='readonly',bg_color='#D0FCF6')
        OpcionesProducto.set('Productos')
        OpcionesProducto.pack(side='left', padx=1, expand=True, fill='x')

        Etiqueta_Cantidad = ctk.CTkLabel(new_row,font=font1,text='Cantidad:',text_color='#000',bg_color='#D0FCF6')
        Etiqueta_Cantidad.pack(side='left', padx=5, expand=True, fill='x')
        Entrada_Cantidad = tk.Spinbox(new_row, from_=0, to=9999, font=font1,borderwidth=3,width=18)
        Entrada_Cantidad.pack(side='left', padx=1, expand=True, fill='x')

        Etiqueta_Ubicacion = ctk.CTkLabel(new_row,font=font1,text='Ubicación:',text_color='#000',bg_color='#D0FCF6')
        Etiqueta_Ubicacion.pack(side='left', padx=5, expand=True, fill='x')
        OptUbicacion = [resultado[0] for resultado in Ubiresultados]
        VarUbicacion = ctk.StringVar()
        OpcionesUbicaciones = ctk.CTkComboBox(new_row,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',variable=VarUbicacion,values=OptUbicacion,state='readonly',bg_color='#D0FCF6')
        OpcionesUbicaciones.set('Ubicación')
        OpcionesUbicaciones.pack(side='left', padx=1, expand=True, fill='x')
        delete_button = ctk.CTkButton(new_row,font=font1,text_color='#fff',border_color='#340A00',
                                      border_width=3,text='Eliminar',fg_color='#BA2400',
                                      hover_color='#752A18',bg_color='#D0FCF6',cursor='hand2',
                                      corner_radius=15,command=lambda: self.delete_row(new_row))
        delete_button.pack(side='left', padx=5, expand=True, fill='x')
        self.entries.append((new_row, VarProducto, Entrada_Cantidad, VarUbicacion))

    def delete_row(self, row):  # row es el marco que contiene los widgets
        row.destroy()
        # Marcar la entrada como eliminada
        row.deleted = True
        # Eliminar la entrada de la lista de entradas
        self.entries = [entry for entry in self.entries if entry[0] != row]

    def save_data(self): # Función para guardar los datos de las lineas puestas en la base de datos
        # Obtener datos de las filas activas (no eliminadas y cantidad diferente de 0)
        active_entries = [(entry[1].get(), entry[2].get(), entry[3].get()) for entry in self.entries if not getattr(entry[0], 'deleted', False)]
        # Verificar si el motivo es "Baja", "Merma" o "Compra"
        motivo = VarRazon.get()
        # Verificar la suma de compras en la base de datos del producto seleccionado
        for entry_data in active_entries:
            producto, cantidad, ubicacion = entry_data

            if producto == 'Productos' or ubicacion == 'Ubicación':
                messagebox.showwarning("Advertencia", f"Faltan datos del movimiento por completar",parent=self)
                return
            if int(cantidad) <= 0:
                messagebox.showwarning("Advertencia", f"No se pueden realizar movimientos con cantidades de producto iguales a cero.",parent=self)
                return
            elif int(cantidad) > 10000:
                messagebox.showwarning("Advertencia", f"No se pueden ingresar tantos productos a la vez, ingrese un número menor a 10000",parent=self)
                return
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        obtener_sku = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                        val = (producto,)
                        cursor.execute(obtener_sku, val)
                        sku = cursor.fetchone()[0]

                        getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                        valores = (ubicacion,)
                        cursor.execute(getUBI,valores)
                        ubi = cursor.fetchone()[0]

                        # Verificar la suma de compras
                        cursor.execute(f"SELECT cantidad FROM jardineria.inventario WHERE sku = '{sku}' AND cod_ubicacion = {ubi}")
                        inventario = cursor.fetchall()
                        Stock = inventario[0][0] if inventario else 0
                        if (int(cantidad) > Stock) and (motivo in ["Baja", "Merma", "Venta"]):
                            messagebox.showwarning("Advertencia", f"Se está intentando extraer más cantidad de '{producto}' de la disponible en {ubicacion}.",parent=self)
                            return

            except mysql.connector.Error as err:
                print(f"Error de22 MySQL: {err}")
                messagebox.showerror("Error", f"Error de22 MySQL: {err}", parent=self)
                return

        # Imprimir datos (puedes eliminar esta línea después de verificar que funciona)
        print("Datos guardados:", active_entries)

        # Llamar al método para guardar en la base de datos
        self.save_to_database(active_entries)

    def clear_rows(self):
        for entry in self.entries:
            entry[0].destroy()
        self.entries = []
        
    def save_to_database(self, data): # Función para guardar los datos en la base de datos (info del save_data a la BD)
        try:
            with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                with conexion.cursor() as cursor:
                    # Iterar sobre los datos y ejecutar las consultas SQL
                    for entry_data in data:
                        producto, cantidad, ubicacion = entry_data

                        obtenerSKU = "SELECT sku FROM jardineria.tipo_producto WHERE nombre = %s"
                        val = (producto,)
                        cursor.execute(obtenerSKU,val)
                        SKU = cursor.fetchall()

                        getUBI = "SELECT cod_ubi FROM jardineria.ubicaciones WHERE nombre = %s"
                        valores = (ubicacion,)
                        cursor.execute(getUBI,valores)
                        UBI = cursor.fetchall()

                        # Reemplaza esto con tu lógica de inserción SQL
                        consulta = f"INSERT INTO jardineria.movimiento (sku,fecha,cantidad,razon,fecha_modificacion,responsable,ubicacion) VALUES ('{SKU[0][0]}',NOW(),{cantidad},'{VarRazon.get()}',NOW(),'{UsuarioRes}',{UBI[0][0]})"
                        cursor.execute(consulta)

                        if VarRazon.get() == 'Compra' or VarRazon.get() == 'Repuesto':
                            cursor.execute(f"SELECT COUNT(*) FROM jardineria.inventario WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")
                            cuantos = cursor.fetchone()[0]
                            if int(cuantos) < 1:
                                cursor.execute(f"INSERT INTO jardineria.inventario (cantidad, sku, cod_ubicacion, fecha_modificacion, responsable) VALUES ({cantidad}, '{SKU[0][0]}', {UBI[0][0]},NOW(),'{UsuarioRes}')")
                            else:
                                cursor.execute(f"UPDATE jardineria.inventario SET cantidad = cantidad + {cantidad} WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")
                                cursor.execute(f"UPDATE jardineria.inventario SET fecha_modificacion = NOW() WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")
                                cursor.execute(f"UPDATE jardineria.inventario SET responsable = '{UsuarioRes}' WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")
                        else:
                            cursor.execute(f"UPDATE jardineria.inventario SET cantidad = cantidad - {cantidad} WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")
                            cursor.execute(f"UPDATE jardineria.inventario SET fecha_modificacion = NOW() WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")
                            cursor.execute(f"UPDATE jardineria.inventario SET responsable = '{UsuarioRes}' WHERE sku = '{SKU[0][0]}' AND cod_ubicacion = {UBI[0][0]}")

                    # Confirmar los cambios en la base de datos
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Datos guardados exitosamente",parent=self)
                    self.clear_rows()

        except mysql.connector.Error as err:
            print(f"Error de MySQL:SAVEBASEDATOS {err}")
            messagebox.showerror("Error", f"Error de MySQL: SAVEBASEDATO{err}", parent=self)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global VarRazon
        self.title("Movimientos")
        self.geometry("1120x600")
        self.minsize(1120,600)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
        self.entries = []
        self.data = []
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

        def add_to_treeview():
            try:
                with mysql.connector.connect(host='localhost', user='root', password='admin', db='Jardineria') as conexion:
                    with conexion.cursor() as cursor:
                        consulta = "SELECT tp.nombre AS nombre_producto, m.razon, m.cantidad, u.nombre AS nombre_ubicacion, m.fecha FROM movimiento m JOIN tipo_producto tp ON m.sku = tp.sku JOIN ubicaciones u ON m.ubicacion = u.cod_ubi WHERE m.fecha >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)"
                        cursor.execute(consulta)
                        resultado = cursor.fetchall()
                        
                        # Borrar todos los elementos actuales en el Treeview
                        tree.delete(*tree.get_children())
                        
                        # Insertar los nuevos datos en el Treeview
                        for fila in resultado:
                            tree.insert('', END, values=fila)

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
        
        # Crear un marco desplazable
        self.scroll_frame = ctk.CTkScrollableFrame(self,bg_color='#91a398',fg_color='#D0FCF6')
        self.scroll_frame.place(relx=0.05, rely=0.5, relwidth=0.90, relheight=0.38, anchor='nw')
        # Crear widgets
        self.add_button = ctk.CTkButton(self, text="Agregar Producto", command=self.add_row, font=font1,text_color='#fff',
                                        border_color='#68462b',border_width=3,fg_color='#74DCAE',hover_color='#5AA986',
                                        bg_color='#D1F2EB',cursor='hand2',corner_radius=15)
        self.add_button.place(relx=0.05, rely=0.42, anchor='nw', relwidth=0.2, relheight=0.05)
        # Agregar la primera fila
        self.add_row()
        # Botón para guardar datos
        self.save_button = ctk.CTkButton(self, text="Ingresar Movimiento",font=font1,command = lambda:[self.save_data(),add_to_treeview()],border_color='#68462b',border_width=3,text_color='#fff',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15)
        self.save_button.place(relx=0.05, rely=0.90, anchor='nw', relwidth=0.25, relheight=0.05)

        Etiqueta_razon = ctk.CTkLabel(self,font=font1,text='Motivo:',text_color='#000',bg_color='#D1F2EB')
        Etiqueta_razon.place(relx=0.3, rely=0.42, anchor='nw')
        razones = ['Compra','Venta','Merma','Baja','Repuesto']
        VarRazon = ctk.StringVar()
        OpcionesRazon = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarRazon,values=razones,state='readonly',bg_color='#D1F2EB')
        OpcionesRazon.set('Compra')
        OpcionesRazon.place(relx=0.42, rely=0.42, anchor='nw')

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1',border_width=3,border_color='#68462b')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Producto','Motivo','Cantidad','Ubicación','Fecha Movimiento')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Producto',anchor=tk.W)
        tree.column('Motivo',anchor=tk.W)
        tree.column('Cantidad',anchor=tk.W)
        tree.column('Ubicación',anchor=tk.W)
        tree.column('Fecha Movimiento',anchor=tk.W)
        tree.heading('Producto',text='Producto')
        tree.heading('Motivo',text='Motivo')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Fecha Movimiento',text='Fecha Movimiento')
        tree.place(relx=0.05, rely=0.05, anchor='nw', relwidth=0.90, relheight=0.36)
        add_to_treeview()

        conexion.close()
    
class Show_Estadisticas(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ubicaciones")
        self.geometry("600x100")
        self.minsize(600,200)
        self.maxsize(700,300)
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#D1F2EB')
        font1 = ('Helvetica',14,'bold')
        font2 = ('Helvetica',12,'bold')
        Metrica1 = ctk.CTkButton(self,command=lambda:estadistica6meses(),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Productos con relación Venta/Compra Inferior',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Metrica2 = ctk.CTkButton(self,command=lambda:estadistica6meses2(),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Productos con relación Venta/Compra Superior',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Metrica3 = ctk.CTkButton(self,command=lambda:estadisticabaja(),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Cantidad de Bajas por producto en los últimos 3 meses',fg_color='#8E6537',hover_color='#78552D',bg_color='#D1F2EB',cursor='hand2',corner_radius=15,width=260)
        Metrica1.place(rely=0.3, relx=0.5, anchor='center')
        Metrica2.place(rely=0.5, relx=0.5, anchor='center')
        Metrica3.place(rely=0.7, relx=0.5, anchor='center')

        def estadistica6meses(): #------------------------------------------------------------------------------------------------------------------------------------------------------------
            # Configuración de la conexión
            conexion_config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'admin',
                'database': 'jardineria',
                'auth_plugin': 'mysql_native_password'
            }

             # Calcular la fecha actual y la fecha de hace 6 meses
            fecha_actual = datetime.now()
            fecha_6_meses_atras = fecha_actual - timedelta(days=30*6)

            # Consultar datos de la base de datos para los últimos 6 meses
            try:
                conexion = mysql.connector.connect(**conexion_config)

                # Obtener datos de movimientos
                consulta_movimientos = "SELECT m.sku, m.fecha, m.cantidad, m.razon, t.nombre FROM jardineria.movimiento m LEFT JOIN jardineria.tipo_producto t ON m.sku = t.sku WHERE m.fecha >= %s"
                df_movimientos = pd.read_sql_query(consulta_movimientos, conexion, params=[fecha_6_meses_atras])

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
            finally:
                if conexion:
                    conexion.close()

            # Clasificar movimientos como compras o ventas
            df_movimientos['tipo'] = df_movimientos['razon'].apply(lambda x: 'Venta' if x in ['Venta', 'Baja', 'Merma'] else 'Compra')

            df_resumen = df_movimientos.groupby(['nombre', 'fecha', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            # Crear un DataFrame para cada tipo
            df_compras = df_resumen[df_resumen['tipo'] == 'Compra']
            df_ventas = df_resumen[df_resumen['tipo'] == 'Venta']

            # Combinar DataFrames
            df_resumen = pd.concat([df_compras.assign(tipo='Compra'), df_ventas.assign(tipo='Venta')])

            # Combinar los valores para los duplicados sumando las cantidades
            df_resumen_combinado = df_resumen.groupby(['nombre', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            # Crear un DataFrame pivote para tener las compras y ventas en columnas separadas
            df_pivote = df_resumen.pivot_table(index='nombre', columns='tipo', values='cantidad', aggfunc='sum', fill_value=0)

            # Calcular la diferencia entre compras y ventas
            df_pivote['Diferencia'] = df_pivote['Venta'] / df_pivote['Compra']

            # Ordenar de forma descendente por la diferencia
            df_pivote = df_pivote.sort_values(by='Diferencia', ascending=True)

            # Limitarlo a 15 datos máximo
            df_pivote = df_pivote.head(15)

            # Eliminar la columna de diferencia para la gráfica
            df_pivote = df_pivote.drop(columns=['Diferencia'])

            # Crear la figura y los ejes
            fig, ax = plt.subplots(figsize=(10, 8))
            plt.subplots_adjust(bottom=0.24, top=0.93)

            # Graficar barras superpuestas
            ax = df_pivote.plot(kind='bar', stacked=False, ax=ax)

            # Personalizar el gráfico
            ax.set_xlabel('Nombre del Producto')
            ax.set_ylabel('Cantidad')
            ax.set_title('Compras y Ventas por Producto en los últimos 6 meses')
            ax.legend(['Compras', 'Ventas'], loc='upper right')

            # Agregar etiquetas a cada barra con los valores correspondientes
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 10), textcoords='offset points')

            #-------------------------------------------------------------------------------------------------------------------------------------------------------------
            plt.style.use('ggplot')
            self.geometry("+{}+{}".format(int((self.winfo_screenwidth() - 600) / 2), int((self.winfo_screenheight() - 200) / 2)))
            ax.set_xlabel('Nombre del Producto', fontsize=12)
            ax.set_ylabel('Cantidad', fontsize=12)
            ax.set_title('Compras y Ventas por Producto en los últimos 6 meses', fontsize=14)
            #-------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            # Mostrar el gráfico
            plt.show()
            
        def estadisticabaja():
            conexion_config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'admin',
                'database': 'Jardineria',
                'auth_plugin': 'mysql_native_password'
            }
            # Calcular la fecha actual y la fecha de hace 3 meses
            fecha_actual = datetime.now()
            fecha_3_meses_atras = fecha_actual - timedelta(days=30 * 3)
            try:
                with mysql.connector.connect(**conexion_config) as conexion:
                    consulta_mermas = "SELECT t.nombre, m.fecha, m.cantidad FROM jardineria.movimiento m LEFT JOIN jardineria.tipo_producto t ON m.sku = t.sku WHERE m.fecha >= %s AND m.razon = 'Baja'"
                    df_mermas = pd.read_sql_query(consulta_mermas, conexion, params=[fecha_3_meses_atras])
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

            # Agrupar por Nombre de Producto y sumar la cantidad de mermas
            total_mermas = df_mermas.groupby('nombre')['cantidad'].sum()
            # Ordenar la gráfica por cantidad de bajas
            total_mermas = total_mermas.sort_values(ascending=False)

            #Limitar a 15 datos
            total_mermas = total_mermas.head(15)

            # Graficar
            plt.figure(figsize=(10, 6))
            plt.subplots_adjust(bottom=0.24,top=0.93)
            plt.style.use('seaborn-v0_8')
            total_mermas.plot(kind='bar', color='red')
            # Agregar etiquetas a cada barra con los valores correspondientes
            for i, v in enumerate(total_mermas):
                plt.text(i, v + 0.1, str(v), ha='center', va='bottom', color='black')
            # Mejorar el estilo del título y las etiquetas del eje
            plt.title('Cantidad de Bajas por Producto en los Últimos 3 Meses', fontsize=16)
            plt.xlabel('Nombre del Producto', fontsize=14)
            plt.ylabel('Cantidad', fontsize=14)
            plt.show()

        def estadistica6meses2(): #------------------------------------------------------------------------------------------------------------------------------------------------------------
            # Configuración de la conexión
            conexion_config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'admin',
                'database': 'jardineria',
                'auth_plugin': 'mysql_native_password'
            }

             # Calcular la fecha actual y la fecha de hace 6 meses
            fecha_actual = datetime.now()
            fecha_6_meses_atras = fecha_actual - timedelta(days=30*6)

            # Consultar datos de la base de datos para los últimos 6 meses
            try:
                conexion = mysql.connector.connect(**conexion_config)

                # Obtener datos de movimientos
                consulta_movimientos = "SELECT m.sku, m.fecha, m.cantidad, m.razon, t.nombre FROM jardineria.movimiento m LEFT JOIN jardineria.tipo_producto t ON m.sku = t.sku WHERE m.fecha >= %s"
                df_movimientos = pd.read_sql_query(consulta_movimientos, conexion, params=[fecha_6_meses_atras])

            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
            finally:
                if conexion:
                    conexion.close()

            # Clasificar movimientos como compras o ventas
            df_movimientos['tipo'] = df_movimientos['razon'].apply(lambda x: 'Venta' if x in ['Venta', 'Baja', 'Merma'] else 'Compra')

            df_resumen = df_movimientos.groupby(['nombre', 'fecha', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            # Crear un DataFrame para cada tipo
            df_compras = df_resumen[df_resumen['tipo'] == 'Compra']
            df_ventas = df_resumen[df_resumen['tipo'] == 'Venta']

            # Combinar DataFrames
            df_resumen = pd.concat([df_compras.assign(tipo='Compra'), df_ventas.assign(tipo='Venta')])

            # Combinar los valores para los duplicados sumando las cantidades
            df_resumen_combinado = df_resumen.groupby(['nombre', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            # Crear un DataFrame pivote para tener las compras y ventas en columnas separadas
            df_pivote = df_resumen.pivot_table(index='nombre', columns='tipo', values='cantidad', aggfunc='sum', fill_value=0)

            # Calcular la diferencia entre compras y ventas
            df_pivote['Diferencia'] = df_pivote['Venta'] / df_pivote['Compra']

            # Ordenar de forma descendente por la diferencia
            df_pivote = df_pivote.sort_values(by='Diferencia', ascending=False)

            # Limitarlo a 15 datos máximo
            df_pivote = df_pivote.head(15)

            # Eliminar la columna de diferencia para la gráfica
            df_pivote = df_pivote.drop(columns=['Diferencia'])

            # Crear la figura y los ejes
            fig, ax = plt.subplots(figsize=(10, 8))
            plt.subplots_adjust(bottom=0.24, top=0.93)

            # Graficar barras superpuestas
            ax = df_pivote.plot(kind='bar', stacked=False, ax=ax)

            # Personalizar el gráfico
            ax.set_xlabel('Nombre del Producto')
            ax.set_ylabel('Cantidad')
            ax.set_title('Compras y Ventas por Producto en los últimos 6 meses')
            ax.legend(['Compras', 'Ventas'], loc='upper left')

            # Agregar etiquetas a cada barra con los valores correspondientes
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 10), textcoords='offset points')

            #-------------------------------------------------------------------------------------------------------------------------------------------------------------
            plt.style.use('ggplot')
            self.geometry("+{}+{}".format(int((self.winfo_screenwidth() - 600) / 2), int((self.winfo_screenheight() - 200) / 2)))
            ax.set_xlabel('Nombre del Producto', fontsize=12)
            ax.set_ylabel('Cantidad', fontsize=12)
            ax.set_title('Compras y Ventas por Producto en los últimos 6 meses', fontsize=14)
            #-------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            # Mostrar el gráfico
            plt.show()