from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel,CTkButton,CTkCheckBox
from tkinter import PhotoImage

Menuroot = CTk() 
Menuroot.geometry("600x600+350+20")
Menuroot.minsize(480,500)
Menuroot.config(bg ='#010101')
Menuroot.title("Iniciar Sesion")

frame = CTkFrame(Menuroot, fg_color='#010101')
frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)
frame.columnconfigure([0,1], weight=1)
frame.rowconfigure([0,1,2,3,4,5], weight=1)

Menuroot.columnconfigure(0, weight=1)
Menuroot.rowconfigure(0, weight=1)

logo = PhotoImage(file='images/logo.png')
logo = logo.subsample(int(logo.width() / 200), int(logo.height() / 200))
img_google = PhotoImage(file='images/google.png')
img_facebook = PhotoImage(file='images/facebook.png')

CTkLabel(frame, image = logo, text="").grid(columnspan=2, row=1)

correo = CTkEntry(frame,  font = ('sans serif',12), placeholder_text= 'Correo electronico', 
	border_color='#2cb67d', fg_color= '#010101',width =220,height=40)
correo.grid(columnspan=2, row=2,padx=4, pady =4)

contrasenna = CTkEntry(frame,show="*", font = ('sans serif',12), placeholder_text= 'Contraseña',
 border_color='#2cb67d', fg_color= '#010101', width =220,height=40)
contrasenna.grid(columnspan=2, row=3,padx=4, pady =4)

checkbox = CTkCheckBox(frame, text="Recordarme",hover_color='#7f5af0', 
	border_color='#2cb67d', fg_color='#2cb67d')
checkbox.grid(columnspan=2, row=4,padx=4, pady =4)

bt_iniciar = CTkButton(frame, font = ('sans serif',12), border_color='#2cb67d', fg_color='#010101',
	hover_color='#2cb67d',corner_radius=12,border_width=2,
    text='Manden PMV')
bt_iniciar.grid(columnspan=2, row=5,padx=4, pady =4)

Espacio = CTkLabel(frame, text="").grid(columnspan=2, row=7)