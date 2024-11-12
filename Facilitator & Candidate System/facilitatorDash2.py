from customtkinter import *
import subprocess
import os
from PIL import Image  
from tkinter import messagebox as mb

app = CTk()
app.geometry("500x500")
app.title("dashboard")
set_appearance_mode("dark")

#Text
label = CTkLabel(master=app, text="Profile Management.",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.place(relx=0.3, rely=0.1, anchor="center")


def on_entry_click(entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.configure(placeholder_text="")

def on_focusout(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)


image_path = "profile_image.jpg" 
try:
    profile_image = CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(90, 90))
    image_label = CTkLabel(master=app, image=profile_image, text="")
    image_label.place(relx=0.15, rely=0.35, anchor="center")
except FileNotFoundError:
    print(f"Error: The file {image_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

#Text bars
first_name = CTkEntry(master=app,
                     placeholder_text="enter first name..",
                     width=300,
                     text_color="#FFCC70",
                     border_color="#008000")
first_name.place(relx=0.6, rely=0.2, anchor="center")
first_name.bind("<FocusIn>", lambda event: on_entry_click(first_name, "enter first name.."))
first_name.bind("<FocusOut>", lambda event: on_focusout(first_name, "enter first name.."))

last_name = CTkEntry(master=app,
                     placeholder_text="enter last name..",
                     width=300,
                     text_color="#FFCC70",
                     border_color="#008000")
last_name.place(relx=0.6, rely=0.3, anchor="center")
last_name.bind("<FocusIn>", lambda event: on_entry_click(last_name, "enter last name.."))
last_name.bind("<FocusOut>", lambda event: on_focusout(last_name, "enter last name.."))

email = CTkEntry(master=app,
                 placeholder_text="enter email address..",
                 width=300,
                 text_color="#FFCC70",
                 border_color="#008000")
email.place(relx=0.6, rely=0.5, anchor="center")
email.bind("<FocusIn>", lambda event: on_entry_click(email, "enter email address.."))
email.bind("<FocusOut>", lambda event: on_focusout(email, "enter email address.."))

label2 = CTkLabel(master=app, text="Please provide a brief description of your role and\n responsibilities as a facilitator at our educational institute.",
                 font=("century gothic", 10),
                 text_color="#FFCC70")
label2.place(relx=0.6, rely=0.63, anchor="center")

textbox = CTkTextbox(master=app, width=250, height=120,
                     scrollbar_button_color="#FFCC70",
                     corner_radius=16,
                     border_color="#FFCC70",
                     border_width=2)
textbox.place(relx=0.6, rely=0.8, anchor="center")

#Gender radio buttons
gender_var = StringVar()

radio_female = CTkRadioButton(master=app,
                              text="Female",
                              variable=gender_var,
                              value="Female",
                              fg_color="#0093E9",
                              corner_radius=36)
radio_female.place(relx=0.5, rely=0.4, anchor="center")

radio_male = CTkRadioButton(master=app,
                            text="Male",
                            variable=gender_var,
                            value="Male",
                            fg_color="#0093E9",
                            corner_radius=36)
radio_male.place(relx=0.7, rely=0.4, anchor="center")

def clear_fields():
    first_name.delete(0, "end")
    last_name.delete(0, "end")
    email.delete(0, "end")
    textbox.delete("1.0", "end")
    gender_var.set("")

clear_button = CTkButton(master=app, command=clear_fields, 
                        text="Clear",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
clear_button.place(relx=0.3, rely=0.7, anchor="ne")


#Save changes function
def save_changes():
    first_name_text = first_name.get().strip()
    last_name_text = last_name.get().strip()
    email_text = email.get().strip()
    description_text = textbox.get("1.0", "end").strip()
    gender_text = gender_var.get().strip()

    if not first_name_text or not last_name_text or not email_text or not description_text or not gender_text:
        mb.showwarning("Save Error", "Please fill out all fields before saving.")
        return

    with open("facilitator_profile.txt", "w") as file:
        file.write(f"First Name: {first_name_text}\n")
        file.write(f"Last Name: {last_name_text}\n")
        file.write(f"Email: {email_text}\n")
        file.write(f"Gender: {gender_text}\n")
        file.write(f"Description:\n{description_text}\n")
        file.write("-----------------\n")

    mb.showinfo("Success", "Profile saved successfully.")

save_button = CTkButton(master=app, command=save_changes,
                        text="Save",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
save_button.place(relx=0.3, rely=0.8, anchor="ne")

root = app

def button_event():
    subprocess.Popen(['python', 'facilitatorDash.py'])
    root.destroy()
    print("Back button pressed")


back_button = CTkButton(master=app, command=button_event,
                        text="Back",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
back_button.place(relx=0.3, rely=0.9, anchor="ne")


app.mainloop()