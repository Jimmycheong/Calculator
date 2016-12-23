from tkinter import * 
from tkinter import ttk 

class MyCalculator: 

	def __init__(self, master): 
			master.title("Jimmy's calculator")

#WIDGET CREATION 
			self.entry = Entry(master, width = 15, font = ('Arial', 24), justify = RIGHT) 

			self.button_0 = Button(master, text = '0', width = 13, height = 3)
			self.button_1 = Button(master, text = '1',width = 5, height = 3)
			self.button_2 = Button(master, text = '2',width = 5, height = 3)
			self.button_3 = Button(master, text = '3', width = 5, height = 3)
			self.button_4 = Button(master, text = '4', width = 5, height = 3)
			self.button_5 = Button(master, text = '5', width = 5, height = 3)
			self.button_6 = Button(master, text = '6', width = 5, height = 3)
			self.button_7 = Button(master, text = '7', width = 5, height = 3)
			self.button_8 = Button(master, text = '8', width = 5, height = 3)
			self.button_9 = Button(master, text = '9', width = 5, height = 3)
			self.button_dot = Button(master, text = '.', width = 5, height = 3)
			self.button_plus = Button(master, text = '+', width = 5, height = 3)			
			self.button_minus = Button(master, text = '-', width = 5, height = 3)			
			self.button_multiply = Button(master, text = 'x', width = 5, height = 3)			
			self.button_divide = Button(master, text = '/', width = 5, height = 3)			
			self.button_equal = Button(master, text = '=', width = 5, height = 3)			
			self.button_clear = Button(master, text = 'C', width = 5, height = 3)			
			self.button_modulus = Button(master, text = '%', width = 5, height = 3)			
			self.button_square = Button(master, text = '^', width = 5, height = 3)			

#GEOMETRY MANAGEMENT 
			self.entry.grid(row=0, column = 0, columnspan=4)
			self.button_0.grid(row=5, column=0, columnspan=2)
			self.button_1.grid(row=4, column=0, ipadx=5) 
			self.button_2.grid(row=4, column=1, ipadx=5)
			self.button_3.grid(row=4, column=2, ipadx=5)
			self.button_4.grid(row=3, column=0, ipadx=5)
			self.button_5.grid(row=3, column=1, ipadx=5)
			self.button_6.grid(row=3, column=2, ipadx=5)
			self.button_7.grid(row=2, column=0, ipadx=5)
			self.button_8.grid(row=2, column=1, ipadx=5)
			self.button_9.grid(row=2, column=2, ipadx=5)
			self.button_dot.grid(row=5, column=2, ipadx=5)
			self.button_plus.grid(row=1, column=3, ipadx=5)
			self.button_minus.grid(row=2, column=3, ipadx=5)
			self.button_multiply.grid(row=3, column=3, ipadx=5)
			self.button_divide.grid(row=4, column=3, ipadx=5)
			self.button_equal.grid(row=5, column=3, ipadx=5)
			self.button_square.grid(row=1, column=2, ipadx=5)
			self.button_modulus.grid(row=1, column=1, ipadx=5)
			self.button_clear.grid(row=1, column=0, ipadx=5)

#BIND EVENTS 

			def decimal(existing_string): 
				if '.' not in existing_string:
					self.entry.insert(END,'.')

			self.button_0.config(command = lambda: self.entry.insert(END,0)) 
			self.button_1 .config(command = lambda: self.entry.insert(END,1)) 
			self.button_2 .config(command = lambda: self.entry.insert(END,2)) 
			self.button_3.config(command = lambda: self.entry.insert(END,3))
			self.button_4.config(command = lambda: self.entry.insert(END,4))
			self.button_5.config(command = lambda: self.entry.insert(END,5)) 
			self.button_6.config(command = lambda: self.entry.insert(END,6))
			self.button_7.config(command = lambda: self.entry.insert(END,7))
			self.button_8.config(command = lambda: self.entry.insert(END,8))
			self.button_9.config(command = lambda: self.entry.insert(END,9))
			self.button_dot.config(command = lambda: decimal(self.entry.get()))
			self.button_clear.config(command = lambda: self.entry.delete(0,END))
		
			def addition(self, a, b): 
				return a + b 

			def subtraction(self, a, b): 
				return a - b  



root = Tk()
my_calculator = MyCalculator(root)
root.mainloop() 