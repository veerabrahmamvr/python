class employee:
    hike=1.05
    emp_count=0
    def __init__ (self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        employee.emp_count+=1
    def fullname(self):
        return f"Employee full name : {self.first} {self.last}"
    def mail_id (self):
        return "{}.{}@alifsmi.com".format(self.first,self.last)
    def emp_hike(self,incr=hike):
        self.incr=incr
        return self.pay * self.incr
    @classmethod
    def emp_hike_incr(cls,per):
        cls.hike=per
    @staticmethod
    def is_workday ():
        print ("Welcome to alif")
        
emp01=employee("VeeraBrahmam","VannemReddi",3800000)
employee.emp_hike_incr(1.1)
#print (employee.hike)
#print (emp01.hike)
employee.is_workday()
