from customtkinter import *
import subprocess
from tkinter import messagebox as mb
import os

app = CTk()
app.geometry("500x500")
app.title("Search")
set_appearance_mode("dark")

def on_entry_click(entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.configure(placeholder_text="")

def on_focusout(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)

#main label
label = CTkLabel(master=app, text="Search pannel",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.place(relx=0.5, rely=0.1, anchor="center")

#textbox for displaying search results
textbox = CTkTextbox(master=app,
                     scrollbar_button_color="#FFCC70",
                     corner_radius=16,
                     border_color="#FFCC70",
                     border_width=2)
textbox.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.8, relheight=0.3)

#instruction label
label2 = CTkLabel(master=app, text="Enter the name of the candidate you want to search for.",
                  font=("century gothic", 15),
                  text_color="#FFCC70")
label2.place(relx=0.5, rely=0.2, anchor="center")

#candidate Entry
candidate = CTkEntry(master=app,
                     placeholder_text="Enter candidate...",
                     text_color="#FFCC70",
                     border_color="#008000")
candidate.place(relx=0.5, rely=0.3, anchor="center", relwidth=0.6)
candidate.bind("<FocusIn>", lambda event: on_entry_click(candidate, "Enter candidate..."))
candidate.bind("<FocusOut>", lambda event: on_focusout(candidate, "Enter candidate..."))

def search_candidate():
    candidate_name = candidate.get().strip()
    if not candidate_name:
        mb.showwarning("Input Error", "Please enter a candidate name.")
        return

    file_path = "candidate_data.txt"
    found = False
    result = ""

#a list to hold lines of a single candidate's data
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            entry = []  
            for line in file:
                if line.strip() == "-----------------":
                    if any(candidate_name.lower() in item.lower() for item in entry):
                        found = True
                        result += "\n".join(entry) + "\n\n"
                    entry = []  
                else:
                    entry.append(line.strip())

            if entry and any(candidate_name.lower() in item.lower() for item in entry):
                found = True
                result += "\n".join(entry) + "\n\n"

    if found:
        mb.showinfo("Candidate Found", "Candidate found!")  
        textbox.delete("1.0", "end")  
        textbox.insert("1.0", result)  
    else:
        mb.showinfo("Not Found", "Candidate doesn't exist.")

#Search Button
search_button = CTkButton(master=app,
                          text="Search",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2,
                          command=search_candidate)
search_button.place(relx=0.3, rely=0.85, anchor="center")

def button_event():
    subprocess.Popen(['python', 'facilitatorDash.py'])
    app.destroy()
    print("Cancel button pressed")

#Cancel Button
cancel_button = CTkButton(master=app, command=button_event,
                          text="Cancel",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2)
cancel_button.place(relx=0.7, rely=0.85, anchor="center")

app.mainloop()