import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import organiser  # Import our file organizer module

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')

        # Title
        title_label = tk.Label(root, text="File Organizer", font=("Arial", 20, "bold"),
                              bg='#f0f0f0', fg='#333')
        title_label.pack(pady=20)

        # Description
        desc_label = tk.Label(root, text="Organize your files by type automatically",
                             font=("Arial", 12), bg='#f0f0f0', fg='#666')
        desc_label.pack(pady=10)

        # Folder selection frame
        folder_frame = tk.Frame(root, bg='#f0f0f0')
        folder_frame.pack(pady=20)

        self.folder_label = tk.Label(folder_frame, text="No folder selected",
                                    font=("Arial", 10), bg='#f0f0f0', fg='#666',
                                    wraplength=400)
        self.folder_label.pack(pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(root, bg='#f0f0f0')
        buttons_frame.pack(pady=20)

        # Select folder button
        select_button = tk.Button(buttons_frame, text="Select Folder",
                                 command=self.select_folder, font=("Arial", 12, "bold"),
                                 bg='#4CAF50', fg='white', padx=20, pady=10,
                                 relief='raised', borderwidth=2)
        select_button.pack(side=tk.LEFT, padx=10)

        # Organize button
        self.organize_button = tk.Button(buttons_frame, text="Organize Files",
                                        command=self.organize_files, font=("Arial", 12, "bold"),
                                        bg='#2196F3', fg='white', padx=20, pady=10,
                                        relief='raised', borderwidth=2, state='disabled')
        self.organize_button.pack(side=tk.LEFT, padx=10)

        # Status frame
        status_frame = tk.Frame(root, bg='#f0f0f0')
        status_frame.pack(pady=20, fill=tk.X, padx=20)

        self.status_label = tk.Label(status_frame, text="Ready to organize files",
                                    font=("Arial", 10), bg='#f0f0f0', fg='#666',
                                    wraplength=500)
        self.status_label.pack()

        # Progress bar (initially hidden)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var,
                                              maximum=100, mode='determinate')
        self.progress_bar.pack(fill=tk.X, pady=10)
        self.progress_bar.pack_forget()  # Hide initially

        self.selected_folder = None

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Select folder to organize")
        if folder_path:
            self.selected_folder = folder_path
            self.folder_label.config(text=f"Selected: {folder_path}", fg='#333')
            self.organize_button.config(state='normal')
            self.status_label.config(text="Folder selected. Click 'Organize Files' to start.")

    def organize_files(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder first!")
            return

        # Disable buttons during processing
        self.organize_button.config(state='disabled')
        self.status_label.config(text="Organizing files... Please wait.")
        self.progress_bar.pack()  # Show progress bar

        try:
            # Count total files for progress
            total_files = len([f for f in os.listdir(self.selected_folder)
                             if os.path.isfile(os.path.join(self.selected_folder, f))])
            processed = 0

            # Redirect stdout to capture organizer output
            import io
            from contextlib import redirect_stdout

            output_buffer = io.StringIO()
            with redirect_stdout(output_buffer):
                organiser.organise_files(self.selected_folder)

            # Update progress (simulated)
            self.progress_var.set(100)
            self.root.update_idletasks()

            # Show results
            output = output_buffer.getvalue()
            if output.strip():
                messagebox.showinfo("Success", f"Files organized successfully!\n\n{output}")
            else:
                messagebox.showinfo("Success", "Files organized successfully!")

            self.status_label.config(text="Organization completed successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error occurred during organization.")

        finally:
            # Re-enable button and hide progress bar
            self.organize_button.config(state='normal')
            self.progress_bar.pack_forget()
            self.progress_var.set(0)

def main():
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()



