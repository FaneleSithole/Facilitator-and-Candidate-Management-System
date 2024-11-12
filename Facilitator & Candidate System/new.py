import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.geometry("600x400")  # Set the default size of the window

# Configure grid layout to be responsive
app.grid_columnconfigure(0, weight=1)  # Make the first column expand
app.grid_rowconfigure(0, weight=1)     # Make the first row expand

# Create a sample widget, e.g., a button
button = ctk.CTkButton(app, text="Button 1")
button.grid(row=0, column=0, sticky="nsew")  # sticky makes the button expand in all directions

# Adding more widgets with responsiveness
entry = ctk.CTkEntry(app, placeholder_text="Enter text")
entry.grid(row=1, column=0, sticky="ew")  # Expands horizontally only
app.grid_rowconfigure(1, weight=1)

# Run the app
app.mainloop()