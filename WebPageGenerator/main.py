
import os
import tkinter
from tkinter import messagebox
import webbrowser

frame_w = 700
frame_h = 160

class ParentWindow(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry(f"{frame_w}x{frame_h}")
        self.master.title("File Transfer")

        # --- Custom text row ---
        self.lbl_custom = tkinter.Label(self, text="Enter text to display on web page.")
        self.lbl_custom.grid(row=0, column=0, padx=(20, 10), pady=(30, 5), sticky="w")
        self.ent_custom_text = tkinter.Entry(self, width=50)
        self.ent_custom_text.grid(row=0, column=1, padx=(0, 10), pady=(30, 5), sticky="ew")
        self.btn_submit_custom = tkinter.Button(self, text="Submit Custom Text", width=20, command=self.submit_custom)
        self.btn_submit_custom.grid(row=0, column=2, padx=(10, 20), pady=(30, 5))

        # --- Default page row ---
        self.lbl_default = tkinter.Label(self, text="Or use the Default web page.")
        self.lbl_default.grid(row=1, column=0, padx=(20, 10), pady=(10, 30), sticky="w")

        self.btn_default = tkinter.Button(self, text="Default HTML Page", width=20, command=self.default_HTML)
        self.btn_default.grid(row=1, column=2, padx=(10, 20), pady=(10, 30))


    def create_webpage(self, message):
        ## build out the body of the html file and write to the file before closing it
        html_content = "<html>\n<body>\n<h1>" + message + "</h1>\n</body>\n</html>"
        ## tries to open, or create if none exists, a new index.html file
        try:
            with open("index.html", "w") as html_file:
                html_file.write(html_content)
            ## then open the newly created webpage in a new tab on the browser.
            webbrowser.open_new_tab("file://" + os.path.abspath("index.html"))
        ## else throw error
        except OSError as error:
            messagebox.showerror("File Error", f"Could not write file:\n{error}")
            return


    def default_HTML(self):
        ## call the create webpage method with the default summer sale message
        self.create_webpage("Stay tuned for summer sale")


    def submit_custom(self):
        ## get the text the user entered, and if they enter text, call the create webpage method with their text
        text = self.ent_custom_text.get().strip()
        if text:
            self.create_webpage(text)
        ## or
        else:
            self.create_webpage("You did not enter any text for the web page to display")



if __name__ == "__main__":
    root = tkinter.Tk()
    app = ParentWindow(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
