from customtkinter import *
import subprocess
from tkinter import messagebox as mb
import os

app = CTk()
app.geometry("500x500")
app.title("Delete")
set_appearance_mode("dark")

app.grid_columnconfigure(0, weight=1)  
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)  

#Title label
label = CTkLabel(master=app, text="Delete pannel",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.grid(row=0, column=0, sticky="n", pady=(10, 5))  


def on_entry_click(entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.configure(placeholder_text="")


def on_focusout(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)


#Instruction label
label2 = CTkLabel(master=app, text="Enter the name of the candidate you want to delete.",
                  font=("century gothic", 15),
                  text_color="#FFCC70")
label2.grid(row=1, column=0, pady=(5, 10))  

#Entry for candidate name
candidate = CTkEntry(master=app,
                     placeholder_text="enter candidate..",
                     text_color="#FFCC70",
                     border_color="#008000")
candidate.grid(row=2, column=0, padx=20, pady=10, sticky="ew")  
candidate.bind("<FocusIn>", lambda event: on_entry_click(candidate, "enter candidate.."))
candidate.bind("<FocusOut>", lambda event: on_focusout(candidate, "enter candidate.."))

found_entries = []  


#Textbox for displaying results
textbox = CTkTextbox(master=app,
                     scrollbar_button_color="#FFCC70",
                     corner_radius=16,
                     border_color="#FFCC70",
                     border_width=2)
textbox.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")  


def search_candidate():
    global found_entries
    candidate_name = candidate.get().strip()
    if not candidate_name:
        mb.showwarning("Input Error", "Please enter a candidate name.")
        return

    file_path = "candidate_data.txt"
    found_entries = []
    result = ""

#List to hold lines of a single candidate's data
#uses "---" to separate single candidate's data
#Check if the current entry contains the candidate's name
# Save the entry and clear entry for the next candidate
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            entry = []  
            for line in file:
                if line.strip() == "-----------------":  
                    if any(candidate_name.lower() in item.lower() for item in entry):
                        found_entries.append(entry.copy())  
                        result += "\n".join(entry) + "\n\n"
                    entry = []  
                else:
                    entry.append(line.strip())

            if entry and any(candidate_name.lower() in item.lower() for item in entry):
                found_entries.append(entry.copy())
                result += "\n".join(entry) + "\n\n"

    if found_entries:
        mb.showinfo("Candidate Found", "Candidate found!") 
        textbox.delete("1.0", "end")  
        textbox.insert("1.0", result)  
    else:
        mb.showinfo("Not Found", "Candidate doesn't exist.")


def delete_candidate():
    global found_entries
    if not found_entries:
        mb.showwarning("Delete Error", "No candidate information to delete.")
        return

    file_path = "candidate_data.txt"
    new_file_data = []

    with open(file_path, "r") as file:
        entry = []
        for line in file:
            if line.strip() == "-----------------": 
                if entry not in found_entries:
                    new_file_data.extend(entry + ["-----------------"])
                entry = []
            else:
                entry.append(line.strip())

        if entry and entry not in found_entries:
            new_file_data.extend(entry + ["-----------------"])

    with open(file_path, "w") as file:
        file.write("\n".join(new_file_data))

    mb.showinfo("Success", "Candidate information deleted successfully.")
    textbox.delete("1.0", "end")  
    found_entries = []  


# Search Button to trigger the search functionality
search_button = CTkButton(master=app,
                          text="Search",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2,
                          command=search_candidate)
search_button.grid(row=4, column=0, sticky="e", padx=(0, 20), pady=5)

delete_button = CTkButton(master=app,
                          text="Delete",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#FF0000",
                          border_color="#FFCC70",
                          border_width=2,
                          command=delete_candidate)
delete_button.grid(row=5, column=0, sticky="e", padx=(0, 20), pady=5)


def button_event():
    subprocess.Popen(['python', 'facilitator/facilitatorDash.py'])
    app.destroy()
    print("cancel button pressed")

cancel_button = CTkButton(master=app, command=button_event,
                          text="Cancel",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2)
cancel_button.grid(row=6, column=0, sticky="e", padx=(0, 20), pady=5)

app.mainloop()#fgggg