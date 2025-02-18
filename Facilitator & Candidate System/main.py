from customtkinter import *
import subprocess
from tkinter import messagebox

app = CTk()
app.geometry("500x500")
app.title("FMTALI")
set_appearance_mode("dark")

#make the window and its widgets responsive
app.grid_columnconfigure(0, weight=1) 
app.grid_rowconfigure(0, weight=1)    

#responsive window
main_frame = CTkFrame(master=app, fg_color="transparent")
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

#Title label
label = CTkLabel(master=main_frame, text="FMTALI Program",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

#First frame for Candidate information
frame1 = CTkFrame(master=main_frame,
                  fg_color="transparent",
                  border_color="#FFCC70",
                  border_width=3)
frame1.grid(row=1, column=0, padx=(20, 10), pady=20, sticky="nsew")

frame1.grid_columnconfigure(0, weight=1)
frame1.grid_rowconfigure(0, weight=1)

frame1_label = CTkLabel(master=frame1, text="Enhance your skills and advance\n your career with our expert-led\ntraining programs. Register now \nand unlock your potential",
                        font=("century gothic", 10),
                        text_color="#FFCC70")
frame1_label.grid(row=0, column=0, padx=10, pady=10)

#Second frame for Facilitator information
frame2 = CTkFrame(master=main_frame,
                  fg_color="transparent",
                  border_color="#FFCC70",
                  border_width=3)
frame2.grid(row=1, column=1, padx=(10, 20), pady=20, sticky="nsew")

frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)

frame2_label = CTkLabel(master=frame2, text="Welcome back! Log in to access \nyour facilitator dashboard, \nmanage your courses, and engage \nwith your learners effectively.",
                        font=("century gothic", 10),
                        text_color="#FFCC70")
frame2_label.grid(row=0, column=0, padx=10, pady=10)

#Candidate Button
def candidate_button_event():
    subprocess.Popen(['python', 'candidate/candidate1.py'])
    app.destroy()
    print("Candidate button pressed")

candidate_button = CTkButton(master=frame1, command=candidate_button_event,
                             text="Candidate",
                             text_color="#FFCC70",
                             corner_radius=32,
                             fg_color="transparent",
                             hover_color="#008000",
                             border_color="#FFCC70",
                             border_width=2)
candidate_button.grid(row=1, column=0, pady=10, sticky="se")

#Facilitator Button
def facilitator_button_event():
    subprocess.Popen(['python', 'facilitator/facilitatorLogin.py'])
    app.destroy()
    print("Facilitator button pressed")

facilitator_button = CTkButton(master=frame2, command=facilitator_button_event,
                               text="Facilitator",
                               text_color="#FFCC70",
                               corner_radius=32,
                               fg_color="transparent",
                               hover_color="#008000",
                               border_color="#FFCC70",
                               border_width=2)
facilitator_button.grid(row=1, column=0, pady=10, sticky="se")

#Exit Button
def exit_event():
    response = messagebox.askyesno("Exit Confirmation", "Are you sure?")
    if response:
        app.destroy()

exit_button = CTkButton(master=main_frame, command=exit_event,
                        text="Exit",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#FF0000",
                        border_color="#FFCC70",
                        border_width=2)
exit_button.grid(row=2, column=0, columnspan=2, pady=(10, 20), sticky="e")

app.mainloop()