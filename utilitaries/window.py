from tkinter import font
from tkinter import *
import _thread

import utilitaries.globalvars


def tkinter_window(buffer):
    _thread.start_new_thread(tkinter_open_window, (buffer,1))

def tkinter_open_window(buffer,*args):
    if utilitaries.globalvars.GUI:
        root = Tk()
        # Specify font
        my_font = font.Font(root=root, family='Courier', size=10)
        canvas = Canvas(root)
        canvas.pack(side=TOP, fill=BOTH, expand=TRUE)
        xscrollbar = Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar = Scrollbar(root, orient=VERTICAL, command= canvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)

        canvas.configure(xscrollcommand=xscrollbar.set)
        canvas.configure(yscrollcommand=yscrollbar.set)

        # Create frame inside canvas
        #frame = Frame(canvas)
        canvas_id = canvas.create_text(10, 10, anchor=NW)
        canvas.itemconfig(canvas_id, text=buffer,font=my_font)
        #frame.bind('<MouseWheel>', _on_mousewheel)


        root.mainloop()
