import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("Sytem")

# Carpeta Proyecto
HomeFile = os.path.dirname(__file__)
# Carpeta Imagenes
image_path = os.path.join(HomeFile, "images")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "_622187fe-1d6b-4ecb-a9ab-a52d24e76802.jfif")), size=(150, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "google.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.movimientos = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "camion_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "camion_light.png")), size=(20, 20))
        self.maestroproducto = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Maestro_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "Maestro_light.png")), size=(20, 20))
        self.estadistica = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "estadistica_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "estadistica_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  SGI MarthaStefanowsky", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ingresar Movimiento",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.movimientos, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Maestro Productos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.maestroproducto, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Maestro Ubicaciones",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.maestroproducto, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        
        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Maestro Usuarios",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.maestroproducto, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")
        
        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Maestro Movimientos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.maestroproducto, anchor="w", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=6, column=0, sticky="ew")
        
        self.frame_7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Estadísticas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.estadistica, anchor="w", command=self.frame_7_button_event)
        self.frame_7_button.grid(row=7, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.N2_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.N3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # create third frame
        self.N4_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.N4_frame.grid_columnconfigure(0, weight=1)
        self.N4_frame_image_label = customtkinter.CTkLabel(self.N4_frame, text="", image=self.large_test_image)
        self.N4_frame_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.N4_frame_button_1 = customtkinter.CTkButton(self.N4_frame, text="", image=self.image_icon_image)
        self.N4_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.N4_frame_button_2 = customtkinter.CTkButton(self.N4_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        self.N4_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.N4_frame_button_3 = customtkinter.CTkButton(self.N4_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        self.N4_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.N4_frame_button_4 = customtkinter.CTkButton(self.N4_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.N4_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create third frame
        self.N5_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.N6_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.N7_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Ingresar Movimiento" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Maestro Productos" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "Maestro Ubicaciones" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "Maestro Usuarios" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "Maestro Movimientos" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "Estadísticas" else "transparent")        

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Ingresar Movimiento":
            self.N2_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.N2_frame.grid_forget()
        if name == "Maestro Productos":
            self.N3_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.N3_frame.grid_forget()
        if name == "Maestro Ubicaciones":
            self.N4_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.N4_frame.grid_forget()
        if name == "Maestro Usuarios":
            self.N5_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.N5_frame.grid_forget()
        if name == "Maestro Movimientos":
            self.N6_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.N6_frame.grid_forget()
        if name == "Estadísticas":
            self.N7_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.N7_frame.grid_forget()
            
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("Ingresar Movimiento")

    def frame_3_button_event(self):
        self.select_frame_by_name("Maestro Productos")

    def frame_4_button_event(self):
        self.select_frame_by_name("Maestro Ubicaciones")

    def frame_5_button_event(self):
        self.select_frame_by_name("Maestro Usuarios")
        
    def frame_6_button_event(self):
        self.select_frame_by_name("Maestro Movimientos")
        
    def frame_7_button_event(self):
        self.select_frame_by_name("Estadísticas")
        
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
