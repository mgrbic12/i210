from tkinter import *
from tkinter.messagebox import showinfo
import random



class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.secret = str(random.randrange(10))

    def create_widgets(self):
        
        self.lbl = Label(self, text="Enter your guess:")
        self.lbl.grid(row = 0, column = 1)

        self.ent = Entry(self, width = 40)
        self.ent.grid(row = 1, column = 0, columnspan = 3)
        
        self.bttn1 = Button(self, text = "Enter", command = self.guess_num)
        self.bttn1.grid(row = 2, column = 1)


    def guess_num(self):
##        print(self.secret)
        if self.ent.get() != self.secret:
            self.lbl["text"] = "Try Again"
            self.ent.delete(0, END)
        else:
            showinfo(message = "Congrats, you guessed the correct number! " + str(self.secret))
            self.lbl["text"] = "Enter your guess:"


# main
root = Tk()
root.title("HW8 9.20")
root.geometry("250x100")
app = Application(root)
root.mainloop()
