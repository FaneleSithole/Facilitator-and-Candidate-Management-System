from customtkinter import *
import subprocess
import os

app = CTk()
app.geometry("700x500")
app.title("Register")
set_appearance_mode("dark")

#Text Label
label = CTkLabel(master=app, text="Complete!",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.place(relx=0.2, rely=0.1, anchor="center")

CTkLabel(master=app, text="The candidate is saved successfully to the register! ",
         font=("arial", 10), text_color="#FFCC70").place(relx=0.7, rely=0.9, anchor="center")

#function to creat eand store info
def read_and_combine_data():
    file1_path = "candidate_data.txt"  
    data = []

    if os.path.exists(file1_path):
        with open(file1_path, "r") as file1:
            for line in file1:
                data.append(line.strip().split(":"))  
    return data        

def display_table(data):
    table_frame = CTkScrollableFrame(master=app,
                                     width=650,
                                     height=300)
    table_frame.place(relx=0.5, rely=0.5, anchor="center")

    headers = ["Details"]
    for col, header in enumerate(headers):
        header_label = CTkLabel(master=table_frame,
                                text=header,
                                width=10,
                                anchor="center",
                                text_color="#FFCC70")
        header_label.grid(row=0, column=col, padx=2, pady=5)

    for i, row in enumerate(data):
        first_name = row[0] if len(row) > 0 else ""
        last_name = row[1] if len(row) > 1 else ""
        cellphone = row[2] if len(row) > 2 else ""
        year = row[3] if len(row) > 3 else ""
        month = row[4] if len(row) > 4 else ""
        day = row[5] if len(row) > 5 else ""
        province = row[6] if len(row) > 6 else ""
        email = row[7] if len(row) > 7 else ""
        gender = row[8] if len(row) > 8 else ""

        CTkLabel(master=table_frame,
                 text=first_name,
                 width=20,
                 anchor="center").grid(row=i + 1, column=0, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=last_name,
                 width=20,
                 anchor="center").grid(row=i + 1, column=1, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=cellphone,
                 width=20,
                 anchor="center").grid(row=i + 1, column=2, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=year,
                 width=20,
                 anchor="center").grid(row=i + 1, column=3, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=month,
                 width=20,
                 anchor="center").grid(row=i + 1, column=4, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=day,
                 width=20,
                 anchor="center").grid(row=i + 1, column=5, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=province,
                 width=20,
                 anchor="center").grid(row=i + 1, column=6, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=email,
                 width=20,
                 anchor="center").grid(row=i + 1, column=7, padx=10, pady=5)
        
        CTkLabel(master=table_frame,
                 text=gender,
                 width=20,
                 anchor="center").grid(row=i + 1, column=8, padx=10, pady=5)

def button_event():
    subprocess.Popen(['python', 'main.py'])
    app.destroy()
    print("candidate button pressed")

#Home Button
home_button = CTkButton(master=app, command=button_event,
                        text="Home",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
home_button.place(relx=0.3, rely=0.9, anchor="ne")

data = read_and_combine_data()
display_table(data)

app.mainloop()