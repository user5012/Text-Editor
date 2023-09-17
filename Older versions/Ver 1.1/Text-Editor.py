import tkinter as tk
from tkinter import filedialog

file_path = None
current_font_size = 12
file_has_been_saved = False
is_modified = False

def open_file(event=None):
    global file_path, file_has_been_saved, is_modified
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)  # Clear the current content
            text.insert(tk.END, file.read())  # Load file content into the text widget
        file_has_been_saved = True
        is_modified = False
        update_title()

def save_file(event=None):
    global file_path, file_has_been_saved, is_modified
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get('1.0', tk.END))
        file_has_been_saved = True
        is_modified = False
        update_title()

def save_new_file(event=None):
    global file_path, file_has_been_saved, is_modified
    default_name_of_file = "New Text File"
    filetypes = [("Text Files", ".txt")]
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name_of_file, filetypes=filetypes)
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get('1.0', tk.END))
        file_has_been_saved = True
        is_modified = False
        update_title()

def on_text_change(event=None):
    global is_modified
    is_modified = True
    update_title()

def zoom_in(event=None):
    global current_font_size
    current_font_size += 2
    text.configure(font=("Helvetica", current_font_size))

def zoom_out(event=None):
    global current_font_size
    current_font_size -= 2
    text.configure(font=("Helvetica", current_font_size))

def update_title():
    global file_path, file_has_been_saved, is_modified
    if file_path:
        filename = file_path.split("/")[-1]
        modified_flag = " *" if is_modified else ""
        app.title(f"Text Editor - {filename}{modified_flag}")
    else:
        app.title("Text Editor - No File Opened")

# Create the main application window
app = tk.Tk()
app.title("Text Editor - No File Opened")
app.iconbitmap("C:\\Users\\User\\Documents\\Text editor\\Ver 1.1\\Text-editor-ico.ico") #CHANGE THIS!

#create a menu
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

#text widget
text = tk.Text(app, state="normal", font=("Helvetica", current_font_size))
text.pack()

#file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open (Ctrl + O)", command=open_file)
file_menu.add_command(label="Save (Ctrl + S)", command=save_file)
file_menu.add_command(label="Save As (Ctrl + Shift + S)", command=save_new_file)

#view menu
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Zoom In (Ctrl Shift +)", command=zoom_in)
view_menu.add_command(label="Zoom Out (Ctrl -)", command=zoom_out)

#binds
app.bind_all("<Control-plus>", zoom_in)
app.bind_all("<Control-minus>", zoom_out)
app.bind_all("<Control-s>", save_file)
app.bind_all("<Control-o>", open_file)
app.bind_all("<Control-Shift-s>", save_new_file)

#bind text change
text.bind("<<Modified>>", on_text_change)

# Run the main event loop
app.mainloop()
