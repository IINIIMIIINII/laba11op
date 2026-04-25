from tkinter import *
import tkinter.filedialog

def LoadFile(ev):
    global fn
    fn = tkinter.filedialog. Open (root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == "": 
        return 
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())
def SaveFile(ev):
    global fn
    f = open(fn, "wt")
    f.write(textbox.get('1.0', 'end'))
    f.close()
root = Tk()
panelFrame = Frame(root, height=20, bg='blue')
textFrame = Frame(root, height=40, width=50)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
textbox = Text(textFrame, font='Arial 12', wrap='word')
scrollbar = Scrollbar (textFrame)
scrollbar ['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')
loadBtn = Button(panelFrame, text='Open')
loadBtn.bind("<Button-1>", LoadFile)
loadBtn.place(x=10, y=1, width=40, height=20)
saveBtn = Button(panelFrame, text='Save')
saveBtn.bind("<Button-1>", SaveFile)
saveBtn.place(x=60, y=1, width=40, height=20)
root.mainloop()