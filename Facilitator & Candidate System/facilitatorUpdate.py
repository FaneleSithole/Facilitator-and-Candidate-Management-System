from customtkinter import *
import subprocess
from tkinter import messagebox as mb
import os

app = CTk()
app.geometry("500x500")
app.title("Update")
set_appearance_mode("dark")

def on_entry_click(entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.configure(placeholder_text="")

def on_focusout(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)

# Main label
label = CTkLabel(master=app, text="Update pannel",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.place(relx=0.5, rely=0.1, anchor="center")

# Candidate Entry
candidate = CTkEntry(master=app,
                     placeholder_text="Enter candidate...",
                     text_color="#FFCC70",
                     border_color="#008000")
candidate.place(relx=0.5, rely=0.3, anchor="center", relwidth=0.6)
candidate.bind("<FocusIn>", lambda event: on_entry_click(candidate, "Enter candidate..."))
candidate.bind("<FocusOut>", lambda event: on_focusout(candidate, "Enter candidate..."))

#Label for instructions
label2 = CTkLabel(master=app, text="Enter the name of the candidate you want to update details.",
                  font=("century gothic", 15),
                  text_color="#FFCC70")
label2.place(relx=0.5, rely=0.2, anchor="center")

#Textbox for displaying and editing candidate information
textbox = CTkTextbox(master=app,
                     scrollbar_button_color="#FFCC70",
                     corner_radius=16,
                     border_color="#FFCC70",
                     border_width=2)
textbox.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.8, relheight=0.25)

def search_candidate():
    global found_entries, found_candidate_name
    candidate_name = candidate.get().strip()
    if not candidate_name:
        mb.showwarning("Input Error", "Please enter a candidate name.")
        return

    file_path = "candidate_data.txt"
    found_entries = []
    found_candidate_name = candidate_name.lower()
    result = ""

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            entry = []  
            for line in file:
                if line.strip() == "---":
                    if any(found_candidate_name in item.lower() for item in entry):
                        found_entries.append(entry.copy())  
                        result += "\n".join(entry) + "\n\n"
                    entry = []  
                else:
                    entry.append(line.strip())

            if entry and any(found_candidate_name in item.lower() for item in entry):
                found_entries.append(entry.copy())
                result += "\n".join(entry) + "\n\n"

    if found_entries:
        mb.showinfo("Candidate Found", "Candidate found!")  
        textbox.delete("1.0", "end")  
        textbox.insert("1.0", result)  
    else:
        mb.showinfo("Not Found", "Candidate doesn't exist.")

def save_changes():
    global found_entries, found_candidate_name
    edited_text = textbox.get("1.0", "end").strip()

    if not edited_text or not found_entries:
        mb.showwarning("Save Error", "No changes to save.")
        return

    updated_entries = [entry.splitlines() for entry in edited_text.split("\n\n") if entry]

    file_path = "candidate_data.txt"
    new_file_data = []
#
    with open(file_path, "r") as file:
        current_entry = []
        for line in file:
            if line.strip() == "---":
                if any(found_candidate_name in item.lower() for item in current_entry):
                    if updated_entries:
                        new_file_data.extend(updated_entries.pop(0) + ["---"])
                    else:
                        new_file_data.extend(current_entry + ["---"])
                else:
                    new_file_data.extend(current_entry + ["---"])
                current_entry = []
            else:
                current_entry.append(line.strip())

        if current_entry:
            if any(found_candidate_name in item.lower() for item in current_entry):
                if updated_entries:
                    new_file_data.extend(updated_entries.pop(0) + ["---"])
                else:
                    new_file_data.extend(current_entry + ["---"])
            else:
                new_file_data.extend(current_entry + ["---"])

    with open(file_path, "w") as file:
        file.write("\n".join(new_file_data))

    mb.showinfo("Success", "Changes saved successfully.")

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
search_button.place(relx=0.3, rely=0.8, anchor="center")

#Save Changes Button
save_button = CTkButton(master=app, command=save_changes,
                        text="Save Changes",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
save_button.place(relx=0.7, rely=0.9, anchor="center")

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
cancel_button.place(relx=0.3, rely=0.9, anchor="center")

app.mainloop()#uuuu