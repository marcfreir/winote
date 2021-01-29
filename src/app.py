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

root.mainloop()
