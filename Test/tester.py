from tkinter import * 
from tkinter import ttk 

root = Tk() 

button1 = Button(root, text = 'First button')
button2 = Button(root, text = 'second button')
button1.grid(row =0, column =0 )
button2.grid(row =0, column =1 )

print (button1.grid_configure())

root.mainloop()