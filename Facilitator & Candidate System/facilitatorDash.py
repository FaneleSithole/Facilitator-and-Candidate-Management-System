from customtkinter import *
import subprocess

# Initialize the main application window
app = CTk()
app.geometry("500x500")
app.title("Dashboard")
set_appearance_mode("dark")

# Main label
label = CTkLabel(master=app, text="Facilitator Dashboard",
                 font=("century gothic", 25),
                 text_color="#FFCC70")
label.place(relx=0.5, rely=0.1, anchor="center")

# Frames and buttons with relative positioning for responsiveness
search_frame = CTkFrame(master=app, fg_color="transparent", border_color="#FFCC70", border_width=3)
search_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

update_frame = CTkFrame(master=app, fg_color="transparent", border_color="#FFCC70", border_width=3)
update_frame.place(relx=0.1, rely=0.32, relwidth=0.8, relheight=0.1)

add_frame = CTkFrame(master=app, fg_color="transparent", border_color="#FFCC70", border_width=3)
add_frame.place(relx=0.1, rely=0.44, relwidth=0.8, relheight=0.1)

delete_frame = CTkFrame(master=app, fg_color="transparent", border_color="#FFCC70", border_width=3)
delete_frame.place(relx=0.1, rely=0.56, relwidth=0.8, relheight=0.1)

more_frame = CTkFrame(master=app, fg_color="transparent", border_color="#FFCC70", border_width=3)
more_frame.place(relx=0.1, rely=0.68, relwidth=0.8, relheight=0.1)


# Functions to handle button events
def search_button_event():
    subprocess.Popen(['python', 'facilitatorSearch.py'])
    app.destroy()
    print("Search button pressed")


def update_button_event():
    subprocess.Popen(['python', 'facilitatorUpdate.py'])
    app.destroy()
    print("Update button pressed")


def add_button_event():
    subprocess.Popen(['python', 'facilitatorAdd.py'])
    app.destroy()
    print("Add New button pressed")


def delete_button_event():
    subprocess.Popen(['python', 'facilitatorDelete.py'])
    app.destroy()
    print("Delete button pressed")


def more_button_event():
    subprocess.Popen(['python', 'facilitatorDash2.py'])
    app.destroy()
    print("More button pressed")


# Create buttons and place them in their respective frames
search_button = CTkButton(master=search_frame, command=search_button_event,
                          text="Search",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2)
search_button.place(relx=0.5, rely=0.5, anchor="center")

update_button = CTkButton(master=update_frame, command=update_button_event,
                          text="Update",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2)
update_button.place(relx=0.5, rely=0.5, anchor="center")

add_button = CTkButton(master=add_frame, command=add_button_event,
                       text="Add New",
                       text_color="#FFCC70",
                       corner_radius=32,
                       fg_color="transparent",
                       hover_color="#008000",
                       border_color="#FFCC70",
                       border_width=2)
add_button.place(relx=0.5, rely=0.5, anchor="center")

delete_button = CTkButton(master=delete_frame, command=delete_button_event,
                          text="Delete",
                          text_color="#FFCC70",
                          corner_radius=32,
                          fg_color="transparent",
                          hover_color="#008000",
                          border_color="#FFCC70",
                          border_width=2)
delete_button.place(relx=0.5, rely=0.5, anchor="center")

more_button = CTkButton(master=more_frame, command=more_button_event,
                        text="More",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
more_button.place(relx=0.5, rely=0.5, anchor="center")


# Back button to exit the current window
def back_button_event():
    subprocess.Popen(['python', 'facilitatorLogin.py'])
    app.destroy()
    print("Back button pressed")


back_button = CTkButton(master=app, command=back_button_event,
                        text="Back",
                        text_color="#FFCC70",
                        corner_radius=32,
                        fg_color="transparent",
                        hover_color="#008000",
                        border_color="#FFCC70",
                        border_width=2)
back_button.place(relx=0.9, rely=0.9, anchor="se")

app.mainloop()