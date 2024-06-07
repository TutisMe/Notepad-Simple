import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

#gui main
root = tk.Tk()
root.title("SimpleNotePad")
root.geometry("460x600")
root.resizable(width=False, height=False)
style = Style(theme='journal')
style = ttk.Style()
night_mode = False

#look
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# Load Saved Notes
notebook = ttk.Notebook(root, style="TNotebook")

# Load Saved Notes
notes = {}
try:
    with open("notes.json" "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

#Create the notebook to hold the notes
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#Create a function to add a new
def add_note():

    #Create a new tab for the note
    note_frame = ttk.Frame(notebook, padding=1)
    notebook.add(note_frame, text="New Note")


    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=20, stick="W")

    title_entry = ttk.Entry(note_frame, width=20)
    title_entry.grid(row=0, column=1, padx=100, pady=20, sticky="W")

    content_entry= tk.Text(note_frame, width=45,height=20)
    content_entry.grid(row=2, column=1, padx=10, pady=25)

    #Create a function to save the note
    def save_note():
    #Get the title and content of the note
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)

    # Add the note to the notes dictionary
        notes[title] = content.strip()

    #Save the notes dictionary to the file
        with open("notes.json", "w") as f:
            json.dump(notes, f)

    #Add the note to the notebook
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)

#add a save button tothe note frame
    save_button = ttk.Button(note_frame, text="Save",
                            command=save_note, style="secondary.TButton")
    save_button.grid(row=3, column=1, padx=10, pady=5)

def load_notes():
    try:
        with open("note.json", "r") as f:
            notes = json.load(f)

            for title, content in notes.items():
                #add the note to the notebook
                note_content = tk.Text(notebook, width=40, height=10)
                note_content.insert(tk.END, content)
                notebook.add(note_content, text=title)

    except FileNotFoundError:
        #eğer bulamazsa dosyayı
        pass

    load_notes()

def delete_note():
    current_tab = notebook.index(notebook.select())

    note_title = notebook.tab(current_tab, "text")

    confirm = messagebox.askyesno("Delete Note",
                                      f"Are you sure want to delete {note_title}?")

    if confirm:

        notebook.forget(current_tab)
        notes.pop(note_title)
        with open("notes.json", "w") as f:
            json.dump(notes, f)

new_button = ttk.Button(root, text="New Note",
                       command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete",
                           command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

def toggle_mode():
    global night_mode

    if night_mode:
        root.config(bg="white")
        label.config(bg="white", fg="black", text="")
        night_mode = False
    else:
        root.config(bg="black")
        label.config(bg="black", fg="white", text="")
        night_mode = True

label = tk.Label(root, text="", bg="black", fg="white", font=("Helvetica", 18))
label.pack(side=tk.LEFT, padx=10, pady=10)

toggle_button = tk.Button(root, text="Color Mode", command=toggle_mode)
toggle_button.pack()

root.mainloop()








