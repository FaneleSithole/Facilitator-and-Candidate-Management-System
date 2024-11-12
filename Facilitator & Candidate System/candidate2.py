from customtkinter import *
import subprocess
from tkinter import messagebox as mb

app = CTk()
app.geometry("500x500")
app.title("Register")
set_appearance_mode("dark")

# Labels and text entries setup
CTkLabel(master=app, text="It is advised that you select a \nminimum of three certifications",
         font=("arial", 10), text_color="#FFCC70").place(relx=0.7, rely=0.2, anchor="center")

CTkLabel(master=app, text="By signing up at OUR Institute, you agree to abide by all \nacademic policies, honor codes, and attendance requirements. \nYou consent to the use of your personal data for educational \npurposes. Tuition and fees must be paid by the deadlines. \nMisconduct may result in disciplinary action, including \nsuspension or expulsion.",
         font=("arial", 10), text_color="#FFCC70").place(relx=0.7, rely=0.8, anchor="center")

qualification = CTkEntry(master=app,
                         placeholder_text="highest qualification..",
                         width=300, text_color="#FFCC70",
                         border_color="#008000")
qualification.place(relx=0.6, rely=0.1, anchor="center")

certificate1 = CTkEntry(master=app,
                        placeholder_text="enter 1st certificate..",
                        width=300,
                        text_color="#FFCC70",
                        border_color="#008000")
certificate1.place(relx=0.6, rely=0.3, anchor="center")

certificate2 = CTkEntry(master=app,
                        placeholder_text="enter 2nd certificate..",
                        width=300,
                        text_color="#FFCC70",
                        border_color="#008000")
certificate2.place(relx=0.6, rely=0.4, anchor="center")

certificate3 = CTkEntry(master=app,
                        placeholder_text="enter 3rd certificate..",
                        width=300,
                        text_color="#FFCC70",
                        border_color="#008000")
certificate3.place(relx=0.6, rely=0.5, anchor="center")

certificate4 = CTkEntry(master=app,
                        placeholder_text="enter 4th certificate..",
                        width=300,
                        text_color="#FFCC70",
                        border_color="#008000")
certificate4.place(relx=0.6, rely=0.6, anchor="center")

def check_certificates():
    certificates = [certificate1.get(), certificate2.get(), certificate3.get(), certificate4.get()]
    filled_certificates = len([cert for cert in certificates if cert.strip()])

    if filled_certificates < 3:
        mb.showwarning("Warning", "Enter at least three certificates")
        checkbox.deselect()
    else:
        checkbox.select()

checkbox = CTkCheckBox(master=app, command=check_certificates,
                       text="I AGREE",
                       fg_color="#0093E9",
                       checkbox_height=15,
                       checkbox_width=15,
                       border_color="#008000",
                       corner_radius=36)
checkbox.place(relx=0.7, rely=0.9, anchor="center")

def save_to_text_file(data):
    """Saves data to a text file."""
    file_path = "candidate_data.txt"
    try:
        with open(file_path, "a") as file:
            # Format each line as 'Field Name: Value'
            file.write(f"Qualification: {data['qualification']}\n")
            file.write(f"Certificate 1: {data['certificate1']}\n")
            file.write(f"Certificate 2: {data['certificate2']}\n")
            file.write(f"Certificate 3: {data['certificate3']}\n")
            file.write(f"Certificate 4: {data['certificate4']}\n")
            file.write("-----------------\n")  
        mb.showinfo("Success", "Data saved successfully to text file!")
    except Exception as e:
        mb.showerror("Error", f"Failed to save data to text file: {e}")

def submit_form():
    if checkbox.get() == 1:
        data = {
            "qualification": qualification.get(),
            "certificate1": certificate1.get(),
            "certificate2": certificate2.get(),
            "certificate3": certificate3.get(),
            "certificate4": certificate4.get()
        }
        save_to_text_file(data)
        continue_button.configure(state="normal")
        submit_button.configure(state="disabled")
    else:
        mb.showwarning("Warning", "Please check the checkbox")

submit_button = CTkButton(master=app, command=submit_form,
                          text="Submit",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2,)
submit_button.place(relx=0.3, rely=0.8, anchor="ne")

def back_button_event():
    subprocess.Popen(['python', 'candidate1.py'])
    app.destroy()

back_button = CTkButton(master=app, command=back_button_event,
                        text="Back",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
back_button.place(relx=0.3, rely=0.9, anchor="ne")

def cont_button_event():
    subprocess.Popen(['python', 'candidate3.py'])
    app.destroy()

continue_button = CTkButton(master=app, command=cont_button_event,
                            text="Continue",
                            text_color="#FFCC70",
                            corner_radius=32,
                            fg_color="transparent",
                            hover_color="#008000",
                            border_color="#FFCC70",
                            border_width=2,
                            state="disabled")
continue_button.place(relx=0.3, rely=0.7, anchor="ne")

app.mainloop()
