from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('WiNote')
# root.iconbitmap('../_img/winote.ico')
root.geometry('1200x660')

#Create main frame
main_frame = Frame(root)
main_frame.pack(pady=5)
#Create scrollbar for the text box
tb_scrollbar = Scrollbar(main_frame)
tb_scrollbar.pack(side=RIGHT, fill=Y)

#Create text box
text_box = Text(main_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=tb_scrollbar.set)
#text_box = Text(m_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
text_box.pack()

#Configure scrollbar
tb_scrollbar.config(command=text_box.yview)

#Create menu
main_menu = Menu(root)
root.config(menu=main_menu)

#Add file menu
file_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit")

#Add edit menu
edit_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#Add help menu
help_menu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
help_menu.add_command(label="Documentation")


root.mainloop()
