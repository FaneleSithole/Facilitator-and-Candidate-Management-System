from customtkinter import *
import subprocess
import os

app = CTk()
app.geometry("700x500")
app.title("Add New")
set_appearance_mode("dark")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure((0, 1, 2), weight=1)

label = CTkLabel(master=app, text="Complete!",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.grid(row=0, column=0, pady=(10, 5), sticky="nw")

info_label = CTkLabel(master=app, text="Please note You can make changes by using the update. ",
                      font=("arial", 10), text_color="#FFCC70")
info_label.grid(row=2, column=0, sticky="se", padx=20, pady=10)

def read_and_combine_data():
    file1_path = "candidate_data.txt" 
    data = []

    if os.path.exists(file1_path):
        with open(file1_path, "r") as file1:
            for line in file1:
                data.append(line.strip().split(":"))  
    return data

def display_table(data):
    table_frame = CTkScrollableFrame(master=app, width=650, height=300)
    table_frame.grid(row=1, column=0, pady=10, padx=20, sticky="nsew") 

    headers = ["Candidate details"]
    for col, header in enumerate(headers):
        header_label = CTkLabel(master=table_frame, text=header, width=10, anchor="center", text_color="#FFCC70")
        header_label.grid(row=0, column=col, padx=5, pady=5)

    for i, row in enumerate(data):
        for col, text in enumerate(row):
            CTkLabel(master=table_frame, text=text, width=20, anchor="center").grid(row=i + 1, column=col, padx=5, pady=5)

def button_event():
    subprocess.Popen(['python', 'facilitator/facilitatorDash.py'])
    app.destroy()
    print("Back button pressed")

back_button = CTkButton(master=app, command=button_event,
                        text="Back",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
back_button.grid(row=2, column=0, sticky="sw", padx=20, pady=10)

data = read_and_combine_data()
display_table(data)

app.mainloop()