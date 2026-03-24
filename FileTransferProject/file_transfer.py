import os
import shutil
import time
import tkinter
from tkinter import *
from tkinter import filedialog


## Window frame dimensions (width x height in pixels)
frame_w = 750
frame_h = 160


class ParentWindow(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)

        self.master = master
        ## Prevent the user from resizing the window
        self.master.resizable(width=False, height=False)
        ## Set the window size using the frame dimensions defined above
        self.master.geometry(f"{frame_w}x{frame_h}")
        self.master.title("File Transfer")

        ## Button that opens a folder browser dialog for the user to select a source directory
        self.btn_source_dir = tkinter.Button(text="Select Source", width=20, command=self.source_dir)
        self.btn_source_dir.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        ## Entry field that displays the file path of the selected source directory
        self.ent_source_dir = tkinter.Entry(width=75)
        self.ent_source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        ## Button that opens a folder browser dialog for the user to select a destination directory
        self.btn_dest_dir = tkinter.Button(text="Select Destination", width=20, command=self.dest_dir)
        self.btn_dest_dir.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        ## Entry field that displays the file path of the selected destination directory
        self.ent_dest_dir = tkinter.Entry(width=75)
        self.ent_dest_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        ## Button that triggers the file check and transfer process
        self.btn_transfer = tkinter.Button(text="Transfer Files", width=20, command=self.check_files)
        self.btn_transfer.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        ## Button that closes the application window
        self.btn_exit = tkinter.Button(text="Exit", width=20, command=self.exit_program)
        self.btn_exit.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


    def source_dir(self):
        ## Open a dialog for the user to browse and select the source folder
        dlg_select_source_dir = tkinter.filedialog.askdirectory()
        ## Clear any previously displayed path before inserting the new selection
        self.ent_source_dir.delete(0, END)
        self.ent_source_dir.insert(0, dlg_select_source_dir)

    def dest_dir(self):
        ## Open a dialog for the user to browse and select the destination folder
        dlg_select_dest_dir = tkinter.filedialog.askdirectory()
        ## Clear any previously displayed path before inserting the new selection
        self.ent_dest_dir.delete(0, END)
        self.ent_dest_dir.insert(0, dlg_select_dest_dir)


    def check_files(self):
        ## Get the current time as a Unix timestamp (seconds since epoch)
        current_time = time.time()
        ## Calculate the cutoff time: any file modified before this point is older than 24 hours
        cutoff_time = current_time - (24 * 60 * 60)  ## 24 hours * 60 minutes * 60 seconds

        ## Retrieve the source directory path from the entry field
        source_path = self.ent_source_dir.get()

        ## Loop through every item in the source directory
        for file in os.listdir(source_path):
            ## Build the full file path by combining the directory path with the file name
            path = os.path.join(source_path, file)

            ## Skip directories — only process files
            if os.path.isfile(path):
                ## Get the timestamp of when the file was last modified
                modification_time = os.path.getmtime(path)

                ## If the file was modified within the last 24 hours, transfer it
                if modification_time >= cutoff_time:
                    self.transfer_files(path)

    def transfer_files(self, file_path):
        ## Retrieve the destination directory path from the entry field
        dst = self.ent_dest_dir.get()
        ## Extract just the file name from the full source path
        file_name = os.path.basename(file_path)
        ## Move the file from the source directory to the destination directory
        shutil.move(file_path, os.path.join(dst, file_name))
        ## Log the transfer to the console for confirmation
        print(f"{file_path} was transferred")

    def exit_program(self):
        ## Destroy the root window and close the application
        root.destroy()



if __name__ == "__main__":
    root = tkinter.Tk()
    app = ParentWindow(root)
    root.mainloop()