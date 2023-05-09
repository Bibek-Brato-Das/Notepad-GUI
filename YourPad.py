import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as font
import tkinter.simpledialog as simpledialog

class YourPad:
    def __init__(self, master):
        self.master = master
        master.title("YourPad++")

        # create scrolledtext widget
        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=("Consolas", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # create menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # create file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_program)

        # create edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)

        # create format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.set_font)
        self.format_menu.add_command(label="Font Size", command=self.set_font_size)

    #Create a new Notepad
    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    #Open a file
    def open_file(self):
        file = tk.filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, file.read())
            file.close()

    #Save the Notepad with the required extension
    def save_file(self):
        file = tk.filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            file.write(self.text_area.get(1.0, tk.END))
            file.close()

    #Exiting the program
    def exit_program(self):
        self.master.destroy()

    #Cut a selected text
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    #Copy a selected text
    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    #Paste a selected text
    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    #Set the font style
    def set_font(self):
        font_family = simpledialog.askstring("Font Family", "Enter font family:")
        if font_family:
            self.text_area.configure(font=font.Font(family=font_family))
			
	#Set the font size
    def set_font_size(self):
        font_size = simpledialog.askinteger("Font Size", "Enter font size:")
        if font_size:
            self.text_area.configure(font=font.Font(size=font_size))

root = tk.Tk()
yourpad = YourPad(root)
root.mainloop()