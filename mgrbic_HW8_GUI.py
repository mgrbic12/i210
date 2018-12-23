from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = "What would you like delivered?")
        self.lbl.grid(row = 0, column = 0, sticky = W)
        
        self.delivery_ent = Entry(self, width = 70)
        self.delivery_ent.grid(row = 0, column = 1, columnspan = 3, sticky = W)

        self.options_lbl = Label(self, text = "Options")
        self.options_lbl.grid(row = 1, column = 2)

        self.method_lbl = Label(self, text = "Delivery Method:")
        self.method_lbl.grid(row = 2, column = 0)

        self.addon_lbl = Label(self, text = "Addons:")
        self.addon_lbl.grid(row = 2, column = 3)
        

        self.method_var = StringVar()
        self.method_var.set(None)
        self.drone_bttn = Radiobutton(self, text = "Flying Drone ($10)", variable = self.method_var, value = "drone")
        self.drone_bttn.grid(row = 3, column = 0)

        self.car_bttn = Radiobutton(self, text = "Self Driving Car ($20)", variable = self.method_var, value = "self driving car")
        self.car_bttn.grid(row = 4, column = 0)

        self.robot_bttn = Radiobutton(self, text = "Giant Robot ($1000)", variable = self.method_var, value = "giant robot")
        self.robot_bttn.grid(row = 5, column = 0)

        self.express_var = BooleanVar()
        self.express_check = Checkbutton(self, text = "Express Delivery (+$30)", variable = self.express_var)
        self.express_check.grid(row = 3, column = 3)

        self.broken_var = BooleanVar()
        self.broken_check = Checkbutton(self, text = "Mostly Not Broken (+$20)", variable = self.broken_var)
        self.broken_check.grid(row = 4, column = 3)

        self.smile_var = BooleanVar()
        self.smile_check = Checkbutton(self, text = "With a Smile (+$1)", variable = self.smile_var)
        self.smile_check.grid(row = 5, column = 3)

        self.confirm_bttn = Button(self, text = "Confirm Delivery", command = self.update_text)
        self.confirm_bttn.grid(row = 6, column = 2)

        self.txt = Text(self, width = 70, height = 5, wrap = WORD)
        self.txt.grid(row = 7, columnspan = 4)

    def update_text(self):
        message = ""
        total_fee = 0

        message += "You have selected to have a " + self.delivery_ent.get() + " delivered by "
        message += self.method_var.get() + " with "
        if self.express_var.get():
            message += "express delivery"
            total_fee += 30
        if self.broken_var.get():
            message += ", mostly not broken"
            total_fee += 20
        if self.smile_var.get():
            message += ", with a smile."
            total_fee += 1
        else:
            message +="."
        if self.method_var.get() == "drone":
            total_fee += 10
        if self.method_var.get() == "self driving car":
            total_fee += 20
        if self.method_var.get() == "giant robot":
            total_fee += 1000
            
        message += " Your total delivery fee comes to: $" + str(total_fee)
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, message)
        
            

        
        


# main
root = Tk()
root.title("Robot Delivery System")
root.geometry("600x300")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
