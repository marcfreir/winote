from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("wiNote")
# root.iconbitmap("../_img/winote.ico")
root.geometry("1200x660")
root.configure(bg="#1e2024")

global check_file_name
check_file_name = False

global selected
selected = False

# Create new file
def new_file():
    # Delete previous text
    text_box.delete("1.0", END)
    # Update status bar
    root.title("New File - wiNote")
    status_bar.config(text="New File       ")

    global check_file_name
    check_file_name = False

# Open file
def open_file():
    # Delete previous text
    text_box.delete("1.0", END)
    # Grab filename
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html, *.htm"), ("Python Files", "*.py"), ("wiNote Files", "*.wnt"), ("All Files", "*.*")))
    # Check if there is a file name
    if text_file:
        # Make filename global to access later
        global check_file_name
        check_file_name = text_file
    # Update status bar
    name = text_file
    status_bar.config(text=f"{name}        ")
    name = name.replace("C:/", "~")
    root.title(f"{name} - wiNote")

    # Open the file
    text_file = open(text_file, "r", encoding="utf8")
    content = text_file.read()
    # Add file content to text box
    text_box.insert(END, content)
    # Close the opened file
    text_file.close()

# Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html, *.htm"), ("Python Files", "*.py"), ("wiNote Files", "*.wnt"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        # Update status bar
        status_bar.config(text=f"Saved: {name}        ")
        name = name.replace("C:/", "~")
        root.title(f"{name} - wiNote")
        # Save the file
        text_file = open(text_file, "w")
        text_file.write(text_box.get(1.0, END))
        # Close the opened file
        text_file.close()

# Save file
def save_file():
    global check_file_name
    if check_file_name:
        # Save the file
        text_file = open(check_file_name, "w")
        text_file.write(text_box.get(1.0, END))
        # Close the opened file
        text_file.close()
        # Update status bar
        status_bar.config(text=f"Saved: {check_file_name}        ")
    else:
        save_as_file()
# Copy text
def copy_text(something):
    global selected
    if text_box.selection_get():
        # Grab selected text from text box
        selected = text_box.selection_get()

# Paste text
def paste_text(something):
    if selected:
        position = text_box.index(INSERT)
        text_box.insert(position, selected)
# Cut text
def cut_text(something):
    global selected
    if text_box.selection_get():
        # Grab selected text from text box
        selected = text_box.selection_get()
        # Delete slected text from text box
        text_box.delete("sel.first", "sel.last")


# Create main frame
main_frame = Frame(root)
main_frame.pack(pady=5)
# Create scrollbar for the text box
tb_scrollbar = Scrollbar(main_frame)
tb_scrollbar.pack(side=RIGHT, fill=Y)

# Create text box
text_box = Text(main_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="#b8f900", selectforeground="#fe3fa2", foreground="white", undo=True, yscrollcommand=tb_scrollbar.set, bg="#1e2024", highlightthickness=0, borderwidth=0)
# text_box = Text(m_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
text_box.pack()

# Configure scrollbar
tb_scrollbar.config(command=text_box.yview)

# Create menu
main_menu = Menu(root)
root.config(menu=main_menu)

# Add file menu
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add edit menu
edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste", command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: cut_text(False))
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add help menu
help_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
help_menu.add_command(label="Documentation")

# Add status bar to the bottom
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()
