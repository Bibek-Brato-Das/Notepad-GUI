# Notepad-GUI

**This is the source code for a simple Notepad GUI using the Tkinter library. Here is a brief explanation of the code:

**The first line imports the Tkinter library as 'tk', while the second and third lines import the ScrolledText and Font modules respectively.
The class PyPad is defined to represent the Notepad GUI.
The constructor for the PyPad class takes in a master object (which represents the main window of the GUI) and sets its title to "Your Pypad".
A ScrolledText widget is created using the ScrolledText module, with the wrap style set to WORD and the font set to Consolas 12. The widget is then packed onto the master window using the pack() method.
A menu bar is created using the Menu class and assigned to the master window using the config() method.
The File menu is created as a cascading menu under the menu bar using the add_cascade() method. Four menu options - New, Open, Save, and Exit - are added to the File menu using the add_command() method.
The Edit menu is created as another cascading menu under the menu bar using the add_cascade() method. Three menu options - Cut, Copy, and Paste - are added to the Edit menu using the add_command() method.
The Format menu is created as a cascading menu under the menu bar using the add_cascade() method. One menu option - Font - is added to the Format menu using the add_command() method.
The rest of the code defines various methods that handle the actions corresponding to the menu options added in steps 6-8.
The new_file() method deletes the contents of the ScrolledText widget when the New menu option is selected.
The open_file() method opens a file dialog box and allows the user to select a text file to open. If a file is selected, its contents are read and displayed in the ScrolledText widget.
The save_file() method opens a file dialog box and allows the user to select a location to save the contents of the ScrolledText widget. If a location is selected, the contents are written to a text file with the .txt extension.
The exit_program() method destroys the main window of the GUI when the Exit menu option is selected.
The cut(), copy(), and paste() methods simulate the Cut, Copy, and Paste operations respectively on the selected text in the ScrolledText widget.
The set_font() method opens two dialog boxes - one for the user to enter the font family and another for the user to enter the font size. If both font family and font size are entered, a new Font object is created with the specified attributes and applied to the ScrolledText widget using the configure() method.

**The last few lines create a Tkinter root object and pass it as an argument to the PyPad constructor to create an instance of the Notepad GUI. The mainloop() method of the root object is then called to start the event loop and keep the GUI window open.
******
