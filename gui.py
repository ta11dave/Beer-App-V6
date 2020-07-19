from tkinter import *
import recipes as rp
#starting from scratch because eels won't compile with pyinstaller.

#https://www.tutorialspoint.com/python/python_gui_programming.htm

def say_hi():
	print("hi there, everyone!")

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Load")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Export")
filemenu.add_command(label="Print")
filemenu.add_command(label="Quit")
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Update Hop AA Values")
editmenu.add_command(label="Equipment Values")
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Common Issues")
menubar.add_cascade(label="Help", menu=helpmenu)

#hi_there is the button that triggers the action
hi_there = Button(root)
hi_there["text"] = "Hello World\n(click me)"
hi_there["command"] = say_hi
hi_there.grid(row=1,column=1)

#here's a spot for malts
malt_button = Button(root, text = "Add Malt")
malt_button.grid(row=1,column=2)

#here's a spot for hops
hop_button = Button(root, text = "Add Hop")
hop_button.grid(row=1,column=3)

#this is the quit button
quit = Button(root, text="QUIT", fg="red", command=root.destroy)
quit.grid(row=2,column=2)

root.config(menu=menubar)
root.mainloop()
