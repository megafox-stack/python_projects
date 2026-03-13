import tkinter as tk
from tkinter import filedialog, messagebox
from organiser import organise_files

selected_folder = ""

# -------- functions --------

def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        folder_label.config(text=selected_folder)
    else:
        folder_label.config(text="No folder selected")

def organizer_run():
    if not selected_folder:
        messagebox.showwarning("Warning", "Select a folder first")
        return
    organise_files(selected_folder)
    messagebox.showinfo("Done", "Files organized successfully")

# -------- main window --------

root = tk.Tk()
root.title("File Organizer")
root.geometry("320x360")
root.configure(bg="#1e1e1e")

# -------- main frame --------

main_frame = tk.Frame(root, bg="#1e1e1e", padx=15, pady=15)
main_frame.pack(expand=True, fill="both")

# -------- labels --------

tk.Label(
    main_frame,
    text="File Organizer",
    fg="white",
    bg="#1e1e1e"
).pack(pady=10)

tk.Label(
    main_frame,
    text="Simple & Safe File Organizer",
    fg="#BBBBBB",
    bg="#1e1e1e"
).pack(pady=5)

folder_label = tk.Label(
    main_frame,
    text="No folder selected",
    fg="#AAAAAA",
    bg="#1e1e1e",
    wraplength=260
)
folder_label.pack(pady=15)

# -------- buttons --------

tk.Button(
    main_frame,
    text="Select Folder",
    bg="#2196F3",
    fg="white",
    width=22,
    relief="flat",
    command=select_folder
).pack(pady=5)

tk.Button(
    main_frame,
    text="Organize Files",
    bg="#4CAF50",
    fg="white",
    width=22,
    relief="flat",
    command=organizer_run
).pack(pady=10)

# -------- start app --------

root.mainloop()



