from tkinter import * 
from tkinter import ttk 

class MyCalculator: 


	def __init__(self, master): 

			master.title("Jimmy's calculator")
			master.geometry('240x305+200+50')
			master.resizable(False, False)

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

			self.math_express=' '
			self.answered = False	#Check to see if final answer 
			self.enter = False 		
			self.lastb = False  		#Check to see if the last button was a non-number 

			def insert_num(integer):
				if self.enter == True: 
					self.entry.delete(0,END)
					self.enter = False 
				check_answer()
				self.entry.insert(END, integer) 
				self.lastb = False 

			def check_answer():
				if self.answered == True: 
					self.entry.delete(0,END)
					self.answered = False

			def decimal(existing_string): 
				if '.' not in existing_string:
					self.entry.insert(END,'.')

			def plus_event(): 
				#CHECK IF THE LAST BUTTON WAS NOT A NUMBER 
				if self.lastb == True:
					return
				if self.math_express[:-1] != '+':
					self.math_express += self.entry.get()
					self.math_express += '+'					
				print(self.math_express)
				self.enter = True 
				self.lastb = True 

			def minus_event(): 
				#CHECK IF THE LAST BUTTON WAS NOT A NUMBER 
				if self.lastb == True:
					return
				print ('Printing', self.math_express[:-1])
				if self.math_express[:-1] != '-':
					self.math_express += self.entry.get()
					self.math_express += '-'					
				print(self.math_express)
				self.enter = True 
				self.lastb = True 

			def multiply_event(): 
				#CHECK IF THE LAST BUTTON WAS NOT A NUMBER 
				if self.lastb == True:
					return
				print ('Printing', self.math_express[:-1])
				if self.math_express[:-1] != '-':
					self.math_express += self.entry.get()
					self.math_express += '*'					
				print(self.math_express)
				self.enter = True 
				self.lastb = True 

			def divide_event(): 
				#CHECK IF THE LAST BUTTON WAS NOT A NUMBER 
				if self.lastb == True:
					return
				print ('Printing', self.math_express[:-1])
				if self.math_express[:-1] != '-':
					self.math_express += self.entry.get()
					self.math_express += '.0/'					
				print(self.math_express)
				self.enter = True 
				self.lastb = True 

			def square_event(): 
				#CHECK IF THE LAST BUTTON WAS NOT A NUMBER 
				if self.lastb == True:
					return
				print ('Printing', self.math_express[:-1])
				if self.math_express[:-1] != '-':
					self.math_express += self.entry.get()
					self.math_express += '**'					
				print(self.math_express)
				self.enter = True 
				self.lastb = True 

			def mod_event(): 
				#CHECK IF THE LAST BUTTON WAS NOT A NUMBER 
				if self.lastb == True:
					return
				if '%' not in self.math_express:
					self.math_express += self.entry.get()
					self.math_express += '%' 					
				print(self.math_express)
				self.enter = True 
				self.lastb = True 

			def evaluate():
				self.math_express += self.entry.get() 
				print ('Expression:', self.math_express)
				if self.math_express[-1] not in '+-':
					print ('Answer :',eval(self.math_express))
					answer = eval(self.math_express)#
				self.entry.delete(0,END)
				if str(answer)[-2:] == '.0':
					answer = str(answer)[:-2]
				self.entry.insert(END,answer)
				self.math_express = " "
				self.answered = True

#MOUSE event configuration 
			self.button_0.config(command = lambda: insert_num(0)) 
			self.button_1 .config(command = lambda: insert_num(1)) 
			self.button_2 .config(command = lambda: insert_num(2)) 
			self.button_3.config(command = lambda: insert_num(3))
			self.button_4.config(command = lambda: insert_num(4))
			self.button_5.config(command = lambda: insert_num(5))
			self.button_6.config(command = lambda: insert_num(6))
			self.button_7.config(command = lambda: insert_num(7))
			self.button_8.config(command = lambda: insert_num(8))
			self.button_9.config(command = lambda: insert_num(9))
			self.button_dot.config(command = lambda: decimal(self.entry.get()))
			self.button_clear.config(command = lambda: self.entry.delete(0,END))
			self.button_equal.config(command = lambda: evaluate())
			self.button_plus.config(command = lambda: plus_event())
			self.button_minus.config(command = lambda: minus_event())
			self.button_multiply.config(command = lambda: multiply_event())
			self.button_divide.config(command = lambda: divide_event())
			self.button_modulus.config(command = lambda: mod_event())
			self.button_square.config(command = lambda: square_event())


#Keyboard bind event configuration 
			
			def keyeval(event):
				evaluate()

			def keyclear(event):
				self.entry.delete(0,END)

			def keydel(event):
				self.entry.delete(len(self.entry.get())-1,END)

			def keyplus(event):
				plus_event()

			def keyminus(event):
				minus_event()

			def keymultiply(event):
				multiply_event()

			def keydivide(event):
				divide_event()

			def keymod(event):
				mod_event()

			def keysquare(event):
				square_event()

			master.bind('<Return>', keyeval)
			master.bind('c', keyclear)
			master.bind('<BackSpace>', keydel)
			master.bind('+', keyplus)
			master.bind('-', keyminus)
			master.bind('*', keymultiply)			
			master.bind('/', keydivide)			
			master.bind('%', keymod)
			master.bind('^', keysquare)						
			master.bind('1', lambda e: insert_num(1))
			master.bind('2', lambda e: insert_num(2))
			master.bind('3', lambda e: insert_num(3))
			master.bind('4', lambda e: insert_num(4))
			master.bind('5', lambda e: insert_num(5))
			master.bind('6', lambda e: insert_num(6))
			master.bind('7', lambda e: insert_num(7))
			master.bind('8', lambda e: insert_num(8))
			master.bind('9', lambda e: insert_num(9))
			master.bind('0', lambda e: insert_num(0))

root = Tk()
my_calculator = MyCalculator(root)
root.mainloop() 