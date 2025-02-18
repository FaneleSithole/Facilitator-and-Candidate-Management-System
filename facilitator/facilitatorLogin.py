from customtkinter import *
import subprocess
from tkinter import messagebox as mb  # Import messagebox for pop-up messages

# Initialize the main app window
app = CTk()
app.geometry("500x500")
app.title("Log-in")
set_appearance_mode("dark")

# Configure the main window to be responsive
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# Main frame for holding all widgets
main_frame = CTkFrame(master=app, fg_color="transparent")
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

# Title label
label = CTkLabel(master=main_frame, text="Log into your account.",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.grid(row=0, column=0, pady=(20, 10))

# Frame for username and password entries
frame = CTkFrame(master=main_frame,
                 fg_color="transparent",
                 border_color="#FFCC70",
                 border_width=3)
frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure([0, 1, 2, 3], weight=1)

# Username label
label2 = CTkLabel(master=frame, text="USER NAME",
                  font=("arial", 10),
                  text_color="#FFCC70")
label2.grid(row=0, column=0, pady=(10, 5))

# Username entry
entry = CTkEntry(master=frame, placeholder_text="enter user name..")
entry.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

# Password label
label3 = CTkLabel(master=frame, text="PASSWORD",
                  font=("arial", 10),
                  text_color="#FFCC70")
label3.grid(row=2, column=0, pady=(10, 5))

# Password entry
entry2 = CTkEntry(master=frame, placeholder_text="enter password..", show="*")
entry2.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

# Sign-in button event
def signin_button_event():
    username = entry.get()
    password = entry2.get()
    # Validate credentials
    if username == "admin" and password == "1234":
        subprocess.Popen(['python', 'facilitatorDash.py'])
        app.destroy()
        print("Sign-in successful")
    else:
        # Show an error message if credentials are incorrect
        mb.showerror("Error", "Enter valid credentials")

# Frame for buttons
button_frame = CTkFrame(master=main_frame, fg_color="transparent")
button_frame.grid(row=2, column=0, pady=10, sticky="ew")
button_frame.grid_columnconfigure([0, 1], weight=1)

# Sign-in button
btn = CTkButton(master=button_frame, command=signin_button_event,
                text="Sign-in",
                text_color="#FFCC70",
                corner_radius=32,
                fg_color="transparent",
                hover_color="#008000",
                border_color="#FFCC70",
                border_width=2)
btn.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Back button event
def back_button_event():
    subprocess.Popen(['python', 'main.py'])
    app.destroy()
    print("Back button pressed")

# Back button
back_btn = CTkButton(master=button_frame, command=back_button_event,
                     text="Back",
                     text_color="#FFCC70",
                     corner_radius=32,
                     fg_color="transparent",
                     hover_color="#008000",
                     border_color="#FFCC70",
                     border_width=2)
back_btn.grid(row=0, column=1, padx=10, pady=10, sticky="w")

app.mainloop()#uuu