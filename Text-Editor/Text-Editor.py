import tkinter as tk
from tkinter import filedialog
import re
from tkinter import messagebox
import tkinter.scrolledtext as scrolltext
import os
import sys
import subprocess

file_path = None
current_font_size = 12
file_has_been_saved = False
is_modified = False
file_opened = False
quit = False
app = tk.Tk()


def check_for_updates():
    #logic to see if update available
    return True

def run_updater():
    try:
        subprocess.run(["python", "Update.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"updater.py failed to run {e}")

def main():
    global text, label1
    if check_for_updates():
        print("Checking for updates...")
        run_updater()
        print("Update finished succesfully")

        def open_file(event=None):
            global file_path, file_has_been_saved, is_modified, file_opened
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            lblPath.configure(text=file_path)
            if file_path:
                with open(file_path, 'r') as file:
                    text.delete('1.0', tk.END)  # Clear the current content
                    text.insert(tk.END, file.read())  # Load file content into the text widget
                file_has_been_saved = True
                is_modified = False
                file_opened = True
                update_title()

        def save_file(event=None):
            global file_path, file_has_been_saved, is_modified, app, quit
            if quit == True:
                if file_path:
                    with open(file_path, "w") as file:
                            file.write(text.get('1.0', tk.END))
                    file_has_been_saved = True
                    is_modified = False
                    update_title()
                    app.quit()
                else:
                    save_new_file()
            else:
                if file_path:
                    with open(file_path, "w") as file:
                        file.write(text.get('1.0', tk.END))
                    file_has_been_saved = True
                    is_modified = False
                    update_title()
                else:
                    Save_file_msgbox = messagebox.askyesno("Text Editor", "You Don't have a file opened, Do you want to save it to a new one?")
                    if Save_file_msgbox:
                        save_new_file()

        def save_new_file(event=None):
            global file_path, file_has_been_saved, is_modified, quit
            if quit == True:
                default_name_of_file = "New Text File"
                filetypes = [("Text Files", ".txt")]
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name_of_file, filetypes=filetypes)
                if file_path:
                    with open(file_path, "w") as file:
                        file.write(text.get('1.0', tk.END))
                    file_has_been_saved = True
                    is_modified = False
                    update_title()
                    app.quit()
            else:
                default_name_of_file = "New Text File"
                filetypes = [("Text Files", ".txt")]
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name_of_file, filetypes=filetypes)
                if file_path:
                    with open(file_path, "w") as file:
                        file.write(text.get('1.0', tk.END))
                    file_has_been_saved = True
                    is_modified = False
                    update_title()
        """
        def close_file(event=None):
            global file_opened, file_path, text, is_modified
            if file_opened == True:
                file_path = None
                text.delete('1.0', tk.END)
                file_opened = False
                lblPath.configure(text="No file opened")
                is_modified = False
                update_title()
        """


        def on_text_change(event=None):
            global is_modified
            is_modified = True
            update_title()
            word_counter()

        def zoom_in(event=None):
            global current_font_size
            if current_font_size <= 20:
                current_font_size += 2
                text.configure(font=("Helvetica", current_font_size))

            else:
                messagebox.showinfo("Text Editor", "Cant zoom out anymore!")

        def zoom_out(event=None):
            global current_font_size
            if current_font_size > 2:
                current_font_size -= 2
                text.configure(font=("Helvetica", current_font_size))
            else :
                messagebox.showinfo("Text Editor", "Cant zoom out anymore!")

        def update_title():
            global file_path, file_has_been_saved, is_modified, file_opened
            if file_opened == True:
                filename = file_path.split("/")[-1] if file_path else "No File Opened"
            else:
                filename = "No File Opened"
            modified_flag = " *" if is_modified else ""
            app.title(f"Text Editor - {filename}{modified_flag}")

        def word_counter(event=None):
            global text, label1
            content = text.get("1.0", "end-1c")
            words = re.findall(r'\w+', content)
            word_count = len(words)
            label1.configure(text=f"words: {word_count}")

        def char_counter(event=None):
            global text
            char_count = len(text.get("1.0", "end-1c"))
            label_var.set(f"Characters: {char_count}")
            

        def exit_app():
            global app, quit
            if is_modified == True:
                exit_request = messagebox.askyesnocancel("Text Editor - Exit", "Do you want to save the changes?")
                if exit_request is not None:
                    if exit_request:
                        quit = True
                        save_file()
                    else:  
                        app.quit()
                else:  
                    None
            else:
                app.quit()
            

        def set_icon(window):
            script_dir = os.path.dirname(sys.argv[0])
            icon_file = "Text-editor-ico.ico"
            if os.path.exists(os.path.join(script_dir,icon_file)):
                app.iconbitmap(default=os.path.join(script_dir,icon_file))

            else:
                app.iconbitmap(default=None)

        
        def Undo(event=None):
            if is_modified:
                text.edit_undo()
                update_title()
            else:
                messagebox.showerror("Text Editor", "No things to undo")

        def Redo(event=None):
            if is_modified:
                text.edit_redo()
                update_title()
            else:
                messagebox.showerror("Text Editor", "No things to redo")

        def Copy(event=None):
            selected_text = text.get("sel.first", "sel.last")
            app.clipboard_clear()
            app.clipboard_append(selected_text)
            app.update
        
        def Paste(event=None):
            clipboard_text = text.clipboard_get()
            text.insert("insert", clipboard_text)


        # Create the main application window
        app.title("Text Editor - No File Opened")
        set_icon(app)

        #freame fit context
        text_frame = tk.Frame(app)
        text_frame.grid(row=0, column=0, sticky="nsew")


        #create a menu
        menu_bar = tk.Menu(app)
        app.config(menu=menu_bar)

        #text widget
        text = scrolltext.ScrolledText(app, state="normal", font=("Helvetica", current_font_size), undo=True)
        text.grid(row=0, column=0, sticky="nsew")

        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)

        #file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Open (CTRL + O)", command=open_file)
        file_menu.add_command(label="Save (CTRL + S)", command=save_file)
        file_menu.add_command(label="Save As (CTRL + SHIFT + S)", command=save_new_file)
        #file_menu.add_command(label="Close File (CTRL + K)", command=close_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit (ALT + F4)", command=exit_app)

        #edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        edit_menu.add_command(label="Copy (CTRL - C)", command=Copy)
        edit_menu.add_command(label="Paste (CTRL - V)", command=Paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Undo (CTRL - Z)", command=Undo)
        edit_menu.add_command(label="Redo (CTRL - Y)", command=Redo)
        
        #view menu
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=view_menu)

        view_menu.add_command(label="Zoom In (Ctrl Shift +)", command=zoom_in )
        view_menu.add_command(label="Zoom Out (Ctrl -)", command=zoom_out)

        #binds
        app.bind_all("<Control-plus>", zoom_in)
        app.bind_all("<Control-minus>", zoom_out)
        app.bind_all("<Control-s>", save_file)
        app.bind_all("<Control-o>", open_file)
        app.bind_all("<Control-Shift-s>", save_new_file)
        #app.bind_all("<Control-k>", close_file)

        #bind text change
        text.bind("<<Modified>>", on_text_change)
        text.bind("<KeyRelease>", word_counter)
        text.bind("<Key>", char_counter)

        #bottom labels

        label1 = tk.Label(app, text="words: 0")
        label1.grid(row=1, column=0, sticky="e", padx=90)

        lblPath = tk.Label(app, text="No file opened")
        lblPath.grid(row=1, column=0, sticky="sw")

        label_var = tk.StringVar()
        label_var.set("Characters : 0")
        lbl_charcounter = tk.Label(app, textvariable=label_var)
        lbl_charcounter.grid(row=1, column=0, sticky="e", padx=10)

        #closing button 
        app.protocol("WM_DELETE_WINDOW", exit_app)


        # Run the main event loop
        app.mainloop()

if __name__ == "__main__":
    main()