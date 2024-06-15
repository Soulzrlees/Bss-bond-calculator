import tkinter as tk
import customtkinter  # Assuming customtkinter is a custom tkinter module you have

def Exit():
    global app
    app.destroy()

def tabs():
    global app, tab1
    tab = customtkinter.CTkTabview(app, height=600, width=1100)
    tab.pack(pady=1)
    # Creating different tabs
    tab1 = tab.add("Main")
    tab2 = tab.add("About")
    
    def main_interface():
        global tab1, app, main_interface_frame, Beelevel_entry, Totalbond_label
        main_interface_frame = customtkinter.CTkFrame(tab1, width=540, height=550, fg_color="#3B3B3B")
        main_interface_frame.pack(side="left")
        
        def on_slider_change(value):
            Totalbond_label.configure(text=f"Current bee\n level: {int(value)}")  # Update Totalbond_label text dynamically

        def labels():
            global app, tab1, main_interface_frame, Totalbond_label
            Title_picture = tk.PhotoImage(file="pictures/logo.png").subsample(11, 11)  # Adjust subsample values as needed
            Title_label = customtkinter.CTkLabel(main_interface_frame, image=Title_picture, text="", fg_color="#0080ff", 
                                                width=Title_picture.width(), height=Title_picture.height(), corner_radius=20)
            Title_label.place(relx=0.5, rely=0.19, anchor=customtkinter.CENTER)

            Beeamount_label = customtkinter.CTkLabel(main_interface_frame, text="Bee amount", fg_color="#0080ff", 
                                                    width=90, height=50, font=("Helvetica", 15, "bold"), justify="center", 
                                                    anchor="center", corner_radius=5)
            Beeamount_label.place(relx=0.23, rely=0.45, anchor=customtkinter.CENTER)

            Totalbond_label = customtkinter.CTkLabel(main_interface_frame, fg_color="#0080ff", width=90, height=50, text="Current bee\n level: 1", 
                                                     font=("Helvetica", 15, "bold"), justify="center", anchor="center", 
                                                     corner_radius=5)
            Totalbond_label.place(relx=0.23, rely=0.6, anchor=customtkinter.CENTER)

        def buttons():
            global app, tab1, main_interface_frame
            input_button = customtkinter.CTkButton(main_interface_frame, text="", text_color="white", fg_color="#4FFFB0", 
                                                   corner_radius=3, width=387, height=50)
            input_button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        def Entries():
            global app, tab1, main_interface_frame, Beelevel_entry
            Beeamount_entry = customtkinter.CTkEntry(main_interface_frame, placeholder_text="Amount of bees at hive:", 
                                                     height=50, width=275, font=("Helvetica", 15, "bold"))
            Beeamount_entry.place(relx=0.6, rely=0.45, anchor=customtkinter.CENTER)

            Beelevel_entry = customtkinter.CTkSlider(main_interface_frame, from_=1, to=24, width=285, height=20, 
                                                     number_of_steps=24, progress_color="#4FFFB0", 
                                                     command=on_slider_change)
            Beelevel_entry.place(relx=0.6, rely=0.6, anchor=customtkinter.CENTER)

            puppybee_var = customtkinter.StringVar(value="on")
            puppybee_switch = customtkinter.CTkSwitch(main_interface_frame, text="Toggle for puppybee", 
                                                      variable=puppybee_var, onvalue="on", offvalue="off", 
                                                      width=386, height=50, font=("Helvetica", 15, "bold"))
            puppybee_switch.place(relx=0.65, rely=0.7, anchor=customtkinter.CENTER)

        Entries()
        buttons()
        labels()

    main_interface()

    def main_interface2():
        global tab1, app, main_interface_frame2
        main_interface_frame2 = customtkinter.CTkFrame(tab1, width=540, height=550, fg_color="#3B3B3B")
        main_interface_frame2.pack(side="right")

        def textbox2():
            global tab1, app, main_interface_frame2
            Result_textbox = customtkinter.CTkTextbox(main_interface_frame2, height=400, width=500)
            Result_textbox.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        def buttons2():
            global tab1, app, main_interface_frame2
            Exit_picture = tk.PhotoImage(file="pictures/Exitpic.png").subsample(15, 15)  # Adjust subsample values as needed
            Exit_button = customtkinter.CTkButton(main_interface_frame2, image=Exit_picture, text="", fg_color="#0080ff", 
                                                  width=Exit_picture.width(), height=Exit_picture.height(), 
                                                  corner_radius=100, command=Exit)
            Exit_button.place(relx=0.9, rely=0.055, anchor=customtkinter.CENTER)

        textbox2()
        buttons2()

    main_interface2()

def Main():
    global app
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
    app = customtkinter.CTk()
    # Getting the user screen size to make sure the program size fits perfectly
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    width_percentage = 0.6
    height_percentage = 0.4
    app_width = int(screen_width * width_percentage)
    app_height = int(screen_height * height_percentage)
    x_position = (screen_width - app_width) // 2  # Center the window horizontally
    y_position = (screen_height - app_height) // 2  # Center the window vertically
    app.title("BSS bond calculator")
    app.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
    # setting minimum size of the program
    app.minsize(1100, 600)
    app.maxsize(1100, 600)
    tabs()
    app.mainloop()

Main()
