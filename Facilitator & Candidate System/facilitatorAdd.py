from customtkinter import *
import subprocess
from tkinter import messagebox as mb
import os

app = CTk()
app.geometry("500x500")
app.title("Register")
set_appearance_mode("dark")

def on_entry_click(entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.configure(placeholder_text="")

def on_focusout(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)

label = CTkLabel(master=app, text="Add new candidate",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.place(relx=0.5, rely=0.1, anchor="center")

#First name text bar
first_name = CTkEntry(master=app,
                      placeholder_text="enter first name..",
                      width=300,
                      text_color="#FFCC70",
                      border_color="#008000")
first_name.place(relx=0.6, rely=0.2, anchor="center")
first_name.bind("<FocusIn>", lambda event: on_entry_click(first_name, "enter first name.."))
first_name.bind("<FocusOut>", lambda event: on_focusout(first_name, "enter first name.."))

# Last name text bar
last_name = CTkEntry(master=app,
                     placeholder_text="enter last name..",
                     width=300,
                     text_color="#FFCC70",
                     border_color="#008000")
last_name.place(relx=0.6, rely=0.3, anchor="center")
last_name.bind("<FocusIn>", lambda event: on_entry_click(last_name, "enter last name.."))
last_name.bind("<FocusOut>", lambda event: on_focusout(last_name, "enter last name.."))

#cellphone text bar
cellphone = CTkEntry(master=app,
                         placeholder_text="enter cellphone..",
                         width=300,
                         text_color="#FFCC70",
                         border_color="#008000")
cellphone.place(relx=0.6, rely=0.4, anchor="center")
cellphone.bind("<FocusIn>", lambda event: on_entry_click(cellphone, "enter date of birth.."))
cellphone.bind("<FocusOut>", lambda event: on_focusout(cellphone, "enter date of birth.."))

#Gender combo boxes
combobox_year = CTkComboBox(master=app, width=80, height=30,
                            values=["year", "94", "95", "96", "97", "98", "99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"],
                            fg_color="#0093E9",
                            border_color="#FFCC70",
                            dropdown_fg_color="#008000")
combobox_year.place(relx=0.8, rely=0.5, anchor="center")

combobox_month = CTkComboBox(master=app, width=105, height=30,
                             values=["month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                             fg_color="#0093E9",
                             border_color="#FFCC70",
                             dropdown_fg_color="#008000")
combobox_month.place(relx=0.6, rely=0.5, anchor="center")

combobox_day = CTkComboBox(master=app, width=60, height=30,
                           values=["day", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
                           fg_color="#0093E9",
                           border_color="#FFCC70",
                           dropdown_fg_color="#008000")
combobox_day.place(relx=0.4, rely=0.5, anchor="center")

#Province text bar
province = CTkEntry(master=app,
                    placeholder_text="enter province..",
                    width=300,
                    text_color="#FFCC70",
                    border_color="#008000")
province.place(relx=0.6, rely=0.6, anchor="center")
province.bind("<FocusIn>", lambda event: on_entry_click(province, "enter province.."))
province.bind("<FocusOut>", lambda event: on_focusout(province, "enter province.."))

#Email text bar
email = CTkEntry(master=app,
                 placeholder_text="enter email address..",
                 width=300,
                 text_color="#FFCC70",
                 border_color="#008000")
email.place(relx=0.6, rely=0.7, anchor="center")
email.bind("<FocusIn>", lambda event: on_entry_click(email, "enter email address.."))
email.bind("<FocusOut>", lambda event: on_focusout(email, "enter email address.."))

#Gender radio buttons
gender_var = StringVar()

radio_female = CTkRadioButton(master=app,
                              text="Female",
                              variable=gender_var,
                              value="Female",
                              fg_color="#0093E9",
                              corner_radius=36)
radio_female.place(relx=0.5, rely=0.8, anchor="center")

radio_male = CTkRadioButton(master=app,
                            text="Male",
                            variable=gender_var,
                            value="Male",
                            fg_color="#0093E9",
                            corner_radius=36)
radio_male.place(relx=0.7, rely=0.8, anchor="center")

def create_data_dict():
    data = {
        "first_name": first_name.get(),
        "last_name": last_name.get(),
        "cellphone": cellphone.get(),
        "year": combobox_year.get(),
        "month": combobox_month.get(),
        "day": combobox_day.get(),
        "province": province.get(),
        "email": email.get(),
        "gender": gender_var.get()
    }
    save_to_text_file(data)

def save_to_text_file(data):
    file_path = "candidate_data.txt"
    try:
        with open(file_path, "a") as file:  # Append mode
            file.write(f"First Name: {data['first_name']}\n")
            file.write(f"Last Name: {data['last_name']}\n")
            file.write(f"cellphone: {data['cellphone']}\n")
            file.write(f"Year: {data['year']}\n")
            file.write(f"Month: {data['month']}\n")
            file.write(f"Day: {data['day']}\n")
            file.write(f"Province: {data['province']}\n")
            file.write(f"Email: {data['email']}\n")
            file.write(f"Gender: {data['gender']}\n")
            file.write("\n-----------------\n\n") 
        mb.showinfo("Success", "Data saved successfully to text file!")
    except Exception as e:
        mb.showerror("Error", f"Failed to save data to text file: {e}")

def toggle_continue_button():
    if switch.get() == 1:
        continue_button.configure(state="normal")
    else:
        continue_button.configure(state="disabled")

def continue_button_event():
    if continue_button.cget("state") == "normal":
        create_data_dict()  
        subprocess.Popen(['python', 'candidate2.py'])
        app.destroy()
    else:
        mb.showwarning("Warning", "Please agree!")

#Switch
switch = CTkSwitch(master=app,
                   text="Done!",
                   button_color="#FFCC70",
                   progress_color="#008000",
                   button_hover_color="#008000",
                   command=toggle_continue_button)
switch.place(relx=0.9, rely=0.9, anchor="center")

#Continue button
continue_button = CTkButton(master=app,
                            text="Continue",
                            text_color="#FFCC70",
                            corner_radius=32,
                            fg_color="transparent",
                            hover_color="#008000",
                            border_color="#FFCC70",
                            border_width=2,
                            command=continue_button_event,
                            state="disabled")
continue_button = CTkButton(master=app,
                            text="Continue",
                            text_color="#FFCC70",
                            corner_radius=32,
                            fg_color="transparent",
                            hover_color="#008000",
                            border_color="#FFCC70",
                            border_width=2,
                            command=continue_button_event,
                            state="disabled")
continue_button.place(relx=0.3, rely=0.8, anchor="ne")

#Back button
def cancel_button_event():
    subprocess.Popen(['python', 'facilitatorDash.py'])
    app.destroy()
    print("Back button pressed")

cancel_button = CTkButton(master=app, command=cancel_button_event,
                        text="Cancel",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
cancel_button.place(relx=0.3, rely=0.9, anchor="ne")

app.mainloop()
