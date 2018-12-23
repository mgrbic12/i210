class Worker(object):

    def __init__(self,worker, wage):
        self.worker = worker
        self.wage = wage

    def changeRate(self, new_rate):
        self.wage = new_rate

    def pay(self, hours):
        self.hours = hours
        print("Not Implemented")

class HourlyWorker(Worker):
    
    def __init__(self, worker, wage):
        self.worker = worker
        self.wage = wage
        
    def pay(self, pay_hours):
        if pay_hours > 40:
            dif = pay_hours - 40
            OTpay = self.wage * 2
            total_pay = (self.wage * 40) 

            print((dif * OTpay) + total_pay)
                
        else:
            money = self.wage * pay_hours
            print(money)
           

class SalariedWorker(Worker):

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
    def pay(self, hours = 0):
        print(self.wage * 40)

  

#Test/Main
#Went to office hours and the UI told me to just put the test code in the probelm for a few of these problems

w1 = Worker("Joe", 15)
w1.pay(35)
w2 = SalariedWorker("Sue", 14.50)
w2.pay()
w2.pay(60)
w3 = HourlyWorker("Dana", 20)
w3.pay(25)
w3.changeRate(35)
w3.pay(25)


