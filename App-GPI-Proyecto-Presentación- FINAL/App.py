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
        bt_modificar_usuario = ctk.CTkButton(frame_botones, text='Administrador Usuario', command=self.mod_usuario, **estilo_boton)
        bt_modificar_usuario.pack(pady=10, anchor='center')
        # Modificar Productos
        bt_modificar_productos = ctk.CTkButton(frame_botones, text='Administrador Productos', command=self.mod_productos, **estilo_boton)
        bt_modificar_productos.pack(pady=10, anchor='center')
        # Modificar Ubicaciones
        bt_modificar_ubicaciones = ctk.CTkButton(frame_botones, text='Administrador Ubicaciones', command=self.mod_ubicaciones, **estilo_boton)
        bt_modificar_ubicaciones.pack(pady=10, anchor='center')
        # Modificar Inventario
        bt_modificar_inventario = ctk.CTkButton(frame_botones, text='Administrador Inventario', command=self.mod_inventario, **estilo_boton)
        bt_modificar_inventario.pack(pady=10, anchor='center')
        # Ingresar Movimiento
        bt_modificar_moviemientos = ctk.CTkButton(frame_botones, text='Administrador Movimiento', command=self.mod_movimiento, **estilo_boton)
        bt_modificar_moviemientos.pack(pady=10, anchor='center')
        # Bucle de ejecucion de la Segunda Ventana
        self.ventana_secundaria.mainloop()
    def mod_usuario(self):
        #llamada a modificar usuario
        self.toplevel_window = MOD_Usuario()
    def mod_ubicaciones(self):
        # Llamada a modificar ubicaciones
        self.toplevel_window = MOD_Ubicaciones()
    def mod_productos(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        self.toplevel_window = MOD_Producto()
    def mod_inventario(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        self.toplevel_window = MOD_Inventario()
    def mod_movimiento(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        self.toplevel_window = MOD_Movimiento()

class MenuPrincipalCol():
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
        bt_modificar_usuario = ctk.CTkButton(frame_botones, text='Consulta Usuario', command=self.ver_usuario, **estilo_boton)
        bt_modificar_usuario.pack(pady=10, anchor='center')
        # Modificar Productos
        bt_modificar_productos = ctk.CTkButton(frame_botones, text='Consulta Productos', command=self.ver_productos, **estilo_boton)
        bt_modificar_productos.pack(pady=10, anchor='center')
        # Modificar Ubicaciones
        bt_modificar_ubicaciones = ctk.CTkButton(frame_botones, text='Consulta Ubicaciones', command=self.ver_ubicaciones, **estilo_boton)
        bt_modificar_ubicaciones.pack(pady=10, anchor='center')
        # Modificar Inventario
        bt_modificar_inventario = ctk.CTkButton(frame_botones, text='Consulta Inventario', command=self.ver_inventario, **estilo_boton)
        bt_modificar_inventario.pack(pady=10, anchor='center')
        # Ingresar Movimiento
        bt_modificar_moviemientos = ctk.CTkButton(frame_botones, text='Agregar Movimiento', command=self.ver_movimiento, **estilo_boton)
        bt_modificar_moviemientos.pack(pady=10, anchor='center')
        # Bucle de ejecucion de la Segunda Ventana
        self.ventana_secundaria.mainloop()
    def ver_usuario(self):
        #llamada a modificar usuario
        self.toplevel_window = CON_Usuario()
    def ver_ubicaciones(self):
        # Llamada a modificar ubicaciones
        self.toplevel_window = CON_Ubicaciones()
    def ver_productos(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        self.toplevel_window = CON_Producto()
    def ver_inventario(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        self.toplevel_window = CON_Inventario()
    def ver_movimiento(self):
        # Logica para la opcion "Modificar Ubicaciones"
        # Puedes implementar la funcionalidad correspondiente aqui
        self.toplevel_window = CON_Movimiento()

class ConfirmationWindow:
    def __init__(self):
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
        self.frame = ctk.CTkFrame(self.ventana, fg_color='#91a398', bg_color='#91a398')
        self.frame.pack(fill='both', expand=True)

        marco = ctk.CTkFrame(self.frame, bg_color='#91a398')
        marco.pack(fill='both', expand=True, padx=30, pady=20)

        resul_conexion = self.conexion(correo, contraseña)


        ctk.CTkLabel(marco, text=resul_conexion, font=('sans serif', 15)).pack(padx=25, pady=20)

        # Ventana emergente para la conexión ---------------------------------------------------------------------------------------------------------------------------------
        if resul_conexion == "Datos Incorrectos":
            pass
        else:
            # Boton Nuevo
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

class MOD_Usuario(ctk.CTkToplevel):
    correo_control = ''
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("900x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
                Rol = variable1.get()
                #Responsable = Entrada_Responsable.get()
                Seña = Entrada_Status.get()
                if not (Correo and Rol and Seña): #if not (Correo and Rol and Responsable and Seña):
                    messagebox.showerror('Error', 'No pueden faltar campos')
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
            Rol = variable1.get()
            Responsable = UsuarioRes#Entrada_Responsable.get()
            Seña = Entrada_Status.get()
            
            if not (Correo and Rol and Responsable and Seña):
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
            #Entrada_Responsable.delete(0,END)
            variable1.set('colaborador')
            Entrada_Status.delete(0,END)
            Entrada_Status.configure(self,show='*',placeholder_text='************',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        
        #Formato página
        Etiqueta_Correo = ctk.CTkLabel(self,font=font1,text='Correo:',text_color='#000',bg_color='#91a398')
        Etiqueta_Correo.place(x=20,y=20)
        Entrada_Correo = ctk.CTkEntry(self,placeholder_text='example@gmail.com',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Correo.place(x=120,y=20)
        #Etiqueta_Responsable = ctk.CTkLabel(self,font=font1,text='Responsable:',text_color='#000',bg_color='#91a398')
        #Etiqueta_Responsable.place(x=20,y=80)
        #Entrada_Responsable = ctk.CTkEntry(self,placeholder_text='Usuario',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        #Entrada_Responsable.place(x=120,y=80)
        Etiqueta_rol = ctk.CTkLabel(self,font=font1,text='Rol:',text_color='#000',bg_color='#91a398')
        Etiqueta_rol.place(x=20,y=80)
        options = ['admin','colaborador']
        variable1 = ctk.StringVar()
        OpcionesRol = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=variable1,values=options,state='readonly',bg_color='#91a398')
        OpcionesRol.set('colaborador')
        OpcionesRol.place(x=120,y=80)
        EtiquetaStatus = ctk.CTkLabel(self,font=font1,text='Contraseña:',text_color='#000',bg_color='#91a398')
        EtiquetaStatus.place(x=20,y=140)
        Entrada_Status = ctk.CTkEntry(self,show='*',placeholder_text='************',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Status.place(x=120,y=140)
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
        tree['columns']=('Correo','Modificación','Responsable','Rol')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Correo',anchor=tk.CENTER,width=165)
        tree.column('Modificación',anchor=tk.CENTER,width=165)
        tree.column('Responsable',anchor=tk.CENTER,width=165)
        tree.column('Rol',anchor=tk.CENTER,width=165)
        tree.heading('Correo',text='Correo')
        tree.heading('Modificación',text='Última Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.heading('Rol',text='Rol')
        tree.place(x=380,y=20)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        #cursor = conexion.cursor()
        #consulta = "SELECT correo,fecha_modificacion,responsable,rol_usuarios FROM jardineria.usuarios"
        #cursor.execute(consulta)

        # Cerrar el cursor y la conexión
        #cursor.close()
        conexion.close()

class MOD_Producto(ctk.CTkToplevel):
    correo_control = ''
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("900x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
                messagebox.showerror('Error','Elija un campo para eliminar')
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
                            messagebox.showinfo('Éxito', 'Producto eliminado con éxito')
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
                    messagebox.showerror('Error', 'No pueden faltar campos')
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
                                messagebox.showinfo('Éxito', 'Producto actualizado correctamente')
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
                messagebox.showerror('Error', 'No pueden faltar campos')
            elif sku_exist(ElSku):
                messagebox.showerror('Error', 'El producto ya existe')
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
                            messagebox.showinfo('Éxito', 'Producto agregado correctamente')
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
        Etiqueta_SKU = ctk.CTkLabel(self,font=font1,text='Tipo:',text_color='#000',bg_color='#91a398')
        Etiqueta_SKU.place(x=20,y=20)
        optionsSKU = ['PLANTA','ACCESORIO','DECORACIÓN']
        variableSKU = ctk.StringVar()
        OpcionesSKU = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=variableSKU,values=optionsSKU,state='readonly',bg_color='#91a398')
        OpcionesSKU.set('PLANTA')
        OpcionesSKU.place(x=120,y=20)
        Etiqueta_Nombre = ctk.CTkLabel(self,font=font1,text='Nombre:',text_color='#000',bg_color='#91a398')
        Etiqueta_Nombre.place(x=20,y=80)
        Entrada_Nombre = ctk.CTkEntry(self,placeholder_text='Producto...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Nombre.place(x=120,y=80)
        Etiqueta_Descripcion = ctk.CTkLabel(self,font=font1,text='Descripción:',text_color='#000',bg_color='#91a398')
        Etiqueta_Descripcion.place(x=20,y=140)
        Entrada_Descripcion = ctk.CTkEntry(self,placeholder_text='Descripción...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Descripcion.place(x=120,y=140)
        #Etiqueta_Responsable = ctk.CTkLabel(self,font=font1,text='Responsable:',text_color='#000',bg_color='#91a398')
        #Etiqueta_Responsable.place(x=20,y=200)
        #Entrada_Responsable = ctk.CTkEntry(self,placeholder_text='Usuario',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        #Entrada_Responsable.place(x=120,y=200)

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Producto',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
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
        tree['columns']=('SKU','Nombre','Descripcion','Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('SKU',anchor=tk.CENTER,width=80)
        tree.column('Nombre',anchor=tk.CENTER,width=130)
        tree.column('Descripcion',anchor=tk.CENTER,width=240)
        tree.column('Modificación',anchor=tk.CENTER,width=140)
        tree.column('Responsable',anchor=tk.CENTER,width=100)
        tree.heading('SKU',text='SKU')
        tree.heading('Nombre',text='Nombre Producto')
        tree.heading('Descripcion',text='Descripcion')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=380,y=20)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()

class MOD_Ubicaciones(ctk.CTkToplevel):
    cod_control = 0
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.title("Ubicaciones")
        self.geometry("900x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
                messagebox.showerror('Error','Elija un campo para eliminar')
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
                            messagebox.showinfo('Éxito', 'Ubicación eliminada con éxito')
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
                Nombre = Entrada_Nombre.get()
                Descripcion = Entrada_Descripcion.get()
                Responsable = UsuarioRes#Entrada_Responsable.get()
                if not (Nombre and Descripcion and Responsable):
                    messagebox.showerror('Error', 'No pueden faltar campos')
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
                                messagebox.showinfo('Éxito', 'Ubicación actualizada correctamente')
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
                messagebox.showerror('Error', 'No pueden faltar campos')
            elif ID_exist(Nombre):
                messagebox.showerror('Error', 'La ubicación ya existe')
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
                            messagebox.showinfo('Éxito', 'Ubicación agregada correctamente')
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

        #Insert into jardineria.ubicaciones (descripcion,fecha_modificacion,responsable,nombre) values ('Primer Patio Junto a la entrada noreste',NOW(),'owner','Patio-1')
        #Formato página
        Etiqueta_Nombre = ctk.CTkLabel(self,font=font1,text='Nombre:',text_color='#000',bg_color='#91a398')
        Etiqueta_Nombre.place(x=20,y=20)
        Entrada_Nombre = ctk.CTkEntry(self,placeholder_text='Nombre...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Nombre.place(x=120,y=20)
        Etiqueta_Descripcion = ctk.CTkLabel(self,font=font1,text='Descripcion:',text_color='#000',bg_color='#91a398')
        Etiqueta_Descripcion.place(x=20,y=80)
        Entrada_Descripcion = ctk.CTkEntry(self,placeholder_text='Descripcion...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        Entrada_Descripcion.place(x=120,y=80)
        #Etiqueta_Responsable = ctk.CTkLabel(self,font=font1,text='Responsable:',text_color='#000',bg_color='#91a398')
        #Etiqueta_Responsable.place(x=20,y=140)
        #Entrada_Responsable = ctk.CTkEntry(self,placeholder_text='Usuario...',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        #Entrada_Responsable.place(x=120,y=140)
        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Ubicación',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
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
        tree['columns']=('Orden Ubicación','Nombre','Descripción','Fecha Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Orden Ubicación',anchor=tk.CENTER,width=120)
        tree.column('Nombre',anchor=tk.CENTER,width=120)
        tree.column('Descripción',anchor=tk.CENTER,width=120)
        tree.column('Fecha Modificación',anchor=tk.CENTER,width=120)
        tree.column('Responsable',anchor=tk.CENTER,width=120)
        tree.heading('Orden Ubicación',text='Orden Ubicación')
        tree.heading('Nombre',text='Nombre')
        tree.heading('Descripción',text='Descripción')
        tree.heading('Fecha Modificación',text='Fecha Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=380,y=20)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()

class MOD_Inventario(ctk.CTkToplevel):
    sku_control = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inventario")
        self.geometry("900x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
                messagebox.showerror('Error','Elija un campo para eliminar')
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
                            messagebox.showinfo('Éxito', 'Segmento de Inventario eliminado con éxito')
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
                nombre = VarProducto.get()
                nombreubi = VarUbicacion.get()
                Responsable = UsuarioRes#Entrada_Responsable.get()
                cantidad = Entrada_Cantidad.get()
                if not (nombre and nombreubi and Responsable and cantidad):
                    messagebox.showerror('Error', 'No pueden faltar campos')
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
                                messagebox.showinfo('Éxito', 'Segmento de Inventario actualizado correctamente')
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
                messagebox.showerror('Error', 'No pueden faltar campos')
            elif sku_exist(sku,cod_ubi):
                messagebox.showerror('Error', 'El producto ya existe en esa ubicación')
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
                            messagebox.showinfo('Éxito', 'Segmento de Inventario agregado correctamente')
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
        Etiqueta_Producto = ctk.CTkLabel(self,font=font1,text='Producto:',text_color='#000',bg_color='#91a398')
        Etiqueta_Producto.place(x=20,y=20)
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
        OpcionesProducto = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarProducto,values=OptProducto,state='readonly',bg_color='#91a398')
        OpcionesProducto.set('Productos')
        OpcionesProducto.place(x=120,y=20)
        Etiqueta_Cantidad = ctk.CTkLabel(self,font=font1,text='Cantidad:',text_color='#000',bg_color='#91a398')
        Etiqueta_Cantidad.place(x=20,y=80)
        Entrada_Cantidad = tk.Spinbox(self, from_=0, to=9999, font=font1,borderwidth=3,width=18)
        Entrada_Cantidad.place(x=150,y=100)
        Etiqueta_Ubicacion = ctk.CTkLabel(self,font=font1,text='Ubicación:',text_color='#000',bg_color='#91a398')
        Etiqueta_Ubicacion.place(x=20,y=140)
        OptUbicacion = [resultado[0] for resultado in Ubiresultados]
        VarUbicacion = ctk.StringVar()
        OpcionesUbicaciones = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarUbicacion,values=OptUbicacion,state='readonly',bg_color='#91a398')
        OpcionesUbicaciones.set('Ubicación')
        OpcionesUbicaciones.place(x=120,y=140)
        #Etiqueta_Responsable = ctk.CTkLabel(self,font=font1,text='Responsable:',text_color='#000',bg_color='#91a398')
        #Etiqueta_Responsable.place(x=20,y=200)
        #Entrada_Responsable = ctk.CTkEntry(self,placeholder_text='Usuario',placeholder_text_color='#858585',font=font1,text_color='#000',fg_color='#fff',border_color='#68462b',border_width=3,width=180,bg_color='#91a398')
        #Entrada_Responsable.place(x=120,y=200)

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Segmento',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
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
        tree['columns']=('Codigo','Cantidad','Ubicación','Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Codigo',anchor=tk.CENTER,width=120)
        tree.column('Cantidad',anchor=tk.CENTER,width=120)
        tree.column('Ubicación',anchor=tk.CENTER,width=120)
        tree.column('Modificación',anchor=tk.CENTER,width=160)
        tree.column('Responsable',anchor=tk.CENTER,width=120)
        tree.heading('Codigo',text='Codigo')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=380,y=20)
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
        self.geometry("900x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
                messagebox.showerror('Error','Elija un campo para eliminar')
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
                            messagebox.showinfo('Éxito', 'Movimiento eliminado con éxito')
                            # Actualizar la vista de Treeview
                            add_to_treeview()
                            clear_cells()
                except mysql.connector.Error as err:
                    print(f"Error de MySQL: {err}")
        def estadistica6(): #------------------------------------------------------------------------------------------------------------------------------------------------------------
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
                consulta = "SELECT sku, fecha, cantidad, razon FROM jardineria.movimiento WHERE fecha >= %s"
                df_movimientos = pd.read_sql_query(consulta, conexion, params=[fecha_6_meses_atras])
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
            finally:
                if conexion:
                    conexion.close()
            # Clasificar movimientos como compras o ventas
            df_movimientos['tipo'] = df_movimientos['razon'].apply(lambda x: 'Venta' if x in ['Venta', 'Baja', 'Merma'] else 'Compra')

            df_resumen = df_movimientos.groupby(['sku', 'fecha', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            import matplotlib.pyplot as plt

            # Crear un DataFrame para cada tipo
            df_compras = df_resumen[df_resumen['tipo'] == 'Compra']
            df_ventas = df_resumen[df_resumen['tipo'] == 'Venta']

           # Combinar DataFrames
            df_resumen = pd.concat([df_compras.assign(tipo='Compra'), df_ventas.assign(tipo='Venta')])

            # Combinar los valores para los duplicados sumando las cantidades
            df_resumen_combinado = df_resumen.groupby(['sku', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            # Crear un DataFrame pivote para tener las compras y ventas en columnas separadas
            df_pivote = df_resumen_combinado.pivot(index='sku', columns='tipo', values='cantidad').fillna(0)

            # Invertir las columnas para que las ventas se superpongan en lugar de apilarse
            df_pivote = df_pivote[['Venta', 'Compra']]

            # Crear la figura y los ejes
            fig, ax = plt.subplots()

            # Graficar barras superpuestas
            df_pivote.plot(kind='bar', stacked=False, ax=ax)

            # Personalizar el gráfico
            ax.set_xlabel('SKU')
            ax.set_ylabel('Cantidad')
            ax.set_title('Compras y Ventas por SKU en los últimos 6 meses')
            ax.legend(['Ventas', 'Compras'], loc='upper left')

            # Mostrar el gráfico
            plt.show()

        def estadisticamerma():
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
            # Consultar datos de la base de datos para las mermas de los últimos 3 meses
            try:
                with mysql.connector.connect(**conexion_config) as conexion:
                    consulta_mermas = "SELECT sku, fecha, cantidad FROM movimiento WHERE fecha >= %s AND razon = 'Merma'"
                    df_mermas = pd.read_sql_query(consulta_mermas, conexion, params=[fecha_3_meses_atras])
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

            # Imprimir el DataFrame para verificar los datos
            print(df_mermas)

            # Agrupar por SKU y sumar la cantidad de mermas
            total_mermas = df_mermas.groupby('sku')['cantidad'].sum()

            # Graficar
            plt.figure(figsize=(10, 6))
            total_mermas.plot(kind='bar', color='red')
            plt.title('Cantidad de Mermas por Producto en los Últimos 3 Meses')
            plt.xlabel('SKU')
            plt.ylabel('Cantidad')
            plt.show()


        def actualizar():
            selected_item = tree.focus()
            if not selected_item:
                messagebox.showerror('Error','Elija un campo para editar')
            else:
                nombre = VarProducto.get()
                nombreubi = VarUbicacion.get()
                Razon = VarRazon.get()
                Ubicacion = VarUbicacion.get()
                cantidad = Entrada_Cantidad.get()
                Responsable = UsuarioRes
                Fecha = fecha_control
                if not (nombre and nombreubi and Ubicacion and cantidad):
                    messagebox.showerror('Error', 'No pueden faltar campos')
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
                                messagebox.showinfo('Éxito', 'Movimiento actualizado correctamente')
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
                messagebox.showerror('Error', 'No pueden faltar campos')
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
                            messagebox.showinfo('Éxito', 'Movimiento agregado correctamente')
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
        Etiqueta_Producto = ctk.CTkLabel(self,font=font1,text='Producto:',text_color='#000',bg_color='#91a398')
        Etiqueta_Producto.place(x=20,y=20)
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
        OpcionesProducto = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarProducto,values=OptProducto,state='readonly',bg_color='#91a398')
        OpcionesProducto.set('Productos')
        OpcionesProducto.place(x=120,y=20)
        Etiqueta_Cantidad = ctk.CTkLabel(self,font=font1,text='Cantidad:',text_color='#000',bg_color='#91a398')
        Etiqueta_Cantidad.place(x=20,y=80)
        Entrada_Cantidad = tk.Spinbox(self, from_=0, to=9999, font=font1,borderwidth=3,width=18)
        Entrada_Cantidad.place(x=150,y=100)
        Etiqueta_razon = ctk.CTkLabel(self,font=font1,text='Motivo:',text_color='#000',bg_color='#91a398')
        Etiqueta_razon.place(x=20,y=140)
        razones = ['Compra','Venta','Merma','Baja','Repuesto']
        VarRazon = ctk.StringVar()
        OpcionesRazon = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarRazon,values=razones,state='readonly',bg_color='#91a398')
        OpcionesRazon.set('Compra')
        OpcionesRazon.place(x=120,y=140)
        Etiqueta_Ubicacion = ctk.CTkLabel(self,font=font1,text='Ubicación:',text_color='#000',bg_color='#91a398')
        Etiqueta_Ubicacion.place(x=20,y=200)
        OptUbicacion = [resultado[0] for resultado in Ubiresultados]
        VarUbicacion = ctk.StringVar()
        OpcionesUbicaciones = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarUbicacion,values=OptUbicacion,state='readonly',bg_color='#91a398')
        OpcionesUbicaciones.set('Ubicación')
        OpcionesUbicaciones.place(x=120,y=200)

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Movimiento',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(x=20,y=260)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(x=20,y=310)
        Boton_Estadistica6 = ctk.CTkButton(self,command=estadistica6,font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Estadística 1',fg_color='#B964D9',hover_color='#9450AD',bg_color='#91a398',cursor='hand2',corner_radius=15,width=110)
        Boton_Estadistica6.place(x=20,y=360)
        Boton_Estadistica = ctk.CTkButton(self,command=estadisticamerma,font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Estadística 2',fg_color='#B94EA3',hover_color='#813672',bg_color='#91a398',cursor='hand2',corner_radius=15,width=110)
        Boton_Estadistica.place(x=160,y=360)
        Boton_modificar = ctk.CTkButton(self,command=actualizar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Modificar',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_modificar.place(x=300,y=360)
        Boton_borrar = ctk.CTkButton(self,command=eliminar_dato,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Eliminar',fg_color='#EC5B5B',hover_color='#A03D3D',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_borrar.place(x=580,y=360)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Producto','Fecha Movimiento','Cantidad','Motivo','Ubicación','Ultima Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Producto',anchor=tk.CENTER,width=80)
        tree.column('Fecha Movimiento',anchor=tk.CENTER,width=160)
        tree.column('Cantidad',anchor=tk.CENTER,width=60)
        tree.column('Motivo',anchor=tk.CENTER,width=80)
        tree.column('Ubicación',anchor=tk.CENTER,width=70)
        tree.column('Ultima Modificación',anchor=tk.CENTER,width=160)
        tree.column('Responsable',anchor=tk.CENTER,width=90)
        tree.heading('Producto',text='Producto')
        tree.heading('Fecha Movimiento',text='Fecha Movimiento')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Motivo',text='Motivo')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Ultima Modificación',text='Ultima Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=380,y=20)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()


class CON_Usuario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("565x400")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Correo','Modificación','Responsable','Rol')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Correo',anchor=tk.CENTER,width=165)
        tree.column('Modificación',anchor=tk.CENTER,width=165)
        tree.column('Responsable',anchor=tk.CENTER,width=165)
        tree.column('Rol',anchor=tk.CENTER,width=165)
        tree.heading('Correo',text='Correo')
        tree.heading('Modificación',text='Última Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.heading('Rol',text='Rol')
        tree.place(x=20,y=20)
        add_to_treeview()
        conexion.close()

class CON_Producto(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.title("Usuarios")
        self.geometry("590x400")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
        #Formato página
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('SKU','Nombre','Descripcion','Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('SKU',anchor=tk.CENTER,width=80)
        tree.column('Nombre',anchor=tk.CENTER,width=130)
        tree.column('Descripcion',anchor=tk.CENTER,width=240)
        tree.column('Modificación',anchor=tk.CENTER,width=140)
        tree.column('Responsable',anchor=tk.CENTER,width=100)
        tree.heading('SKU',text='SKU')
        tree.heading('Nombre',text='Nombre Producto')
        tree.heading('Descripcion',text='Descripcion')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=20,y=20)
        add_to_treeview()
        conexion.close()

class CON_Ubicaciones(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ubicaciones")
        self.geometry("530x400")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#91a398')
        self.resizable(False,False)
        font1 = ('Helvetica',14,'bold')
        font2 = ('Helvetica',12,'bold')
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

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Orden Ubicación','Nombre','Descripción','Fecha Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Orden Ubicación',anchor=tk.CENTER,width=120)
        tree.column('Nombre',anchor=tk.CENTER,width=120)
        tree.column('Descripción',anchor=tk.CENTER,width=120)
        tree.column('Fecha Modificación',anchor=tk.CENTER,width=120)
        tree.column('Responsable',anchor=tk.CENTER,width=120)
        tree.heading('Orden Ubicación',text='Orden Ubicación')
        tree.heading('Nombre',text='Nombre')
        tree.heading('Descripción',text='Descripción')
        tree.heading('Fecha Modificación',text='Fecha Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=20,y=20)
        add_to_treeview()

class CON_Inventario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inventario")
        self.geometry("560x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
        self.config(bg='#91a398')
        self.resizable(False,False)
        font1 = ('Helvetica',14,'bold')
        font2 = ('Helvetica',12,'bold')
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
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Codigo','Cantidad','Ubicación','Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Codigo',anchor=tk.CENTER,width=120)
        tree.column('Cantidad',anchor=tk.CENTER,width=120)
        tree.column('Ubicación',anchor=tk.CENTER,width=120)
        tree.column('Modificación',anchor=tk.CENTER,width=160)
        tree.column('Responsable',anchor=tk.CENTER,width=120)
        tree.heading('Codigo',text='Codigo')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Modificación',text='Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=20,y=20)
        add_to_treeview()

class CON_Movimiento(ctk.CTkToplevel):
    sku_control = ''
    fecha_control = ''
    ubi_control = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Movimientos")
        self.geometry("900x420")
        self.after(250, lambda: self.iconbitmap(os.path.join(ImageFile, "icono.ico")))
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
        #funciones
        def estadisticamerma():
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

            # Consultar datos de la base de datos para las mermas de los últimos 3 meses
            try:
                with mysql.connector.connect(**conexion_config) as conexion:
                    consulta_mermas = "SELECT sku, fecha, cantidad FROM movimiento WHERE fecha >= %s AND razon = 'Merma'"
                    df_mermas = pd.read_sql_query(consulta_mermas, conexion, params=[fecha_3_meses_atras])
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")

            # Agrupar por SKU y sumar la cantidad de mermas
            total_mermas = df_mermas.groupby('sku')['cantidad'].sum()

            # Graficar
            plt.figure(figsize=(10, 6))
            total_mermas.plot(kind='bar', color='red')
            plt.title('Cantidad de Mermas por Producto en los Últimos 3 Meses')
            plt.xlabel('SKU')
            plt.ylabel('Cantidad')
            plt.show()

        def estadistica6(): #------------------------------------------------------------------------------------------------------------------------------------------------------------
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
                consulta = "SELECT sku, fecha, cantidad, razon FROM jardineria.movimiento WHERE fecha >= %s"
                df_movimientos = pd.read_sql_query(consulta, conexion, params=[fecha_6_meses_atras])
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
            finally:
                if conexion:
                    conexion.close()
            # Clasificar movimientos como compras o ventas
            df_movimientos['tipo'] = df_movimientos['razon'].apply(lambda x: 'Venta' if x in ['Venta', 'Baja', 'Merma'] else 'Compra')

            df_resumen = df_movimientos.groupby(['sku', 'fecha', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            import matplotlib.pyplot as plt

            # Crear un DataFrame para cada tipo
            df_compras = df_resumen[df_resumen['tipo'] == 'Compra']
            df_ventas = df_resumen[df_resumen['tipo'] == 'Venta']

           # Combinar DataFrames
            df_resumen = pd.concat([df_compras.assign(tipo='Compra'), df_ventas.assign(tipo='Venta')])

            # Combinar los valores para los duplicados sumando las cantidades
            df_resumen_combinado = df_resumen.groupby(['sku', 'tipo']).agg({'cantidad': 'sum'}).reset_index()

            # Crear un DataFrame pivote para tener las compras y ventas en columnas separadas
            df_pivote = df_resumen_combinado.pivot(index='sku', columns='tipo', values='cantidad').fillna(0)

            # Invertir las columnas para que las ventas se superpongan en lugar de apilarse
            df_pivote = df_pivote[['Venta', 'Compra']]

            # Crear la figura y los ejes
            fig, ax = plt.subplots()

            # Graficar barras superpuestas
            df_pivote.plot(kind='bar', stacked=False, ax=ax)

            # Personalizar el gráfico
            ax.set_xlabel('SKU')
            ax.set_ylabel('Cantidad')
            ax.set_title('Compras y Ventas por SKU en los últimos 6 meses')
            ax.legend(['Ventas', 'Compras'], loc='upper left')

            # Mostrar el gráfico
            plt.show()
            
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
                messagebox.showerror('Error', 'No pueden faltar campos')
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
                            ponefecha = "UPDATE inventario SET fecha_modificacion = NOW() WHERE sku = %s AND cod_ubicacion = %s"
                            valinicia = (SKUresultado[0][0],Ubires[0][0],SKUresultado[0][0],Ubires[0][0])
                            cursor.execute(inicializa,valinicia)
                            cursor.execute(ponefecha,(SKUresultado[0][0],Ubires[0][0]))
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
                            messagebox.showinfo('Éxito', 'Movimiento agregado correctamente')
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
        Etiqueta_Producto = ctk.CTkLabel(self,font=font1,text='Producto:',text_color='#000',bg_color='#91a398')
        Etiqueta_Producto.place(x=20,y=20)
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
        OpcionesProducto = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarProducto,values=OptProducto,state='readonly',bg_color='#91a398')
        OpcionesProducto.set('Productos')
        OpcionesProducto.place(x=120,y=20)
        Etiqueta_Cantidad = ctk.CTkLabel(self,font=font1,text='Cantidad:',text_color='#000',bg_color='#91a398')
        Etiqueta_Cantidad.place(x=20,y=80)
        Entrada_Cantidad = tk.Spinbox(self, from_=0, to=9999, font=font1,borderwidth=3,width=18)
        Entrada_Cantidad.place(x=150,y=100)
        Etiqueta_razon = ctk.CTkLabel(self,font=font1,text='Motivo:',text_color='#000',bg_color='#91a398')
        Etiqueta_razon.place(x=20,y=140)
        razones = ['Compra','Venta','Merma','Baja','Repuesto']
        VarRazon = ctk.StringVar()
        OpcionesRazon = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarRazon,values=razones,state='readonly',bg_color='#91a398')
        OpcionesRazon.set('Compra')
        OpcionesRazon.place(x=120,y=140)
        Etiqueta_Ubicacion = ctk.CTkLabel(self,font=font1,text='Ubicación:',text_color='#000',bg_color='#91a398')
        Etiqueta_Ubicacion.place(x=20,y=200)
        OptUbicacion = [resultado[0] for resultado in Ubiresultados]
        VarUbicacion = ctk.StringVar()
        OpcionesUbicaciones = ctk.CTkComboBox(self,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#68462b',border_width=3,button_color='#68462b',button_hover_color='#0C9295',border_color='#68462b',width=180,variable=VarUbicacion,values=OptUbicacion,state='readonly',bg_color='#91a398')
        OpcionesUbicaciones.set('Ubicación')
        OpcionesUbicaciones.place(x=120,y=200)

        #Botones
        Boton_Agregar = ctk.CTkButton(self,command=insertar,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Añadir Movimiento',fg_color='#74DCAE',hover_color='#5AA986',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Agregar.place(x=20,y=360)
        Boton_Limpiar = ctk.CTkButton(self,command=lambda:clear_cells(True),font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Limpiar',fg_color='#8E6537',hover_color='#78552D',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Limpiar.place(x=300,y=360)
        Boton_Estadisticas = ctk.CTkButton(self,command=estadistica6,font=font1,text_color='#fff',border_color='#68462b',border_width=3,text='Estadística C/V',fg_color='#59A4E2',hover_color='#3F74A1',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Estadisticas.place(x=300,y=360)
        Boton_Estadistica2 = ctk.CTkButton(self,command=estadisticamerma,font=font1,border_color='#68462b',border_width=3,text_color='#fff',text='Estadística Merma',fg_color='#B964D9',hover_color='#9450AD',bg_color='#91a398',cursor='hand2',corner_radius=15,width=260)
        Boton_Estadistica2.place(x=580,y=360)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure('Treeview',font=font2,foreground='#000',background='#D6D6D6',fieldbackground='#E9E0D1')
        style.map('Treeview',background=[('selected','#B97E11')])        
        tree = ttk.Treeview(self,height=19)
        tree['columns']=('Producto','Fecha Movimiento','Cantidad','Motivo','Ubicación','Ultima Modificación','Responsable')
        tree.column('#0',width=0,stretch=tk.NO) #esconde la primera
        tree.column('Producto',anchor=tk.CENTER,width=80)
        tree.column('Fecha Movimiento',anchor=tk.CENTER,width=160)
        tree.column('Cantidad',anchor=tk.CENTER,width=60)
        tree.column('Motivo',anchor=tk.CENTER,width=80)
        tree.column('Ubicación',anchor=tk.CENTER,width=70)
        tree.column('Ultima Modificación',anchor=tk.CENTER,width=160)
        tree.column('Responsable',anchor=tk.CENTER,width=90)
        tree.heading('Producto',text='Producto')
        tree.heading('Fecha Movimiento',text='Fecha Movimiento')
        tree.heading('Cantidad',text='Cantidad')
        tree.heading('Motivo',text='Motivo')
        tree.heading('Ubicación',text='Ubicación')
        tree.heading('Ultima Modificación',text='Ultima Modificación')
        tree.heading('Responsable',text='Responsable')
        tree.place(x=380,y=20)
        tree.bind('<ButtonRelease>',mostrar_data)
        add_to_treeview()

        conexion.close()
