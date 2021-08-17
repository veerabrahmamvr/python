class employee:
    raise_amt=1.04
    def __init__ (self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.pay=pay

    def fullname(self):
        """ This method is useful to get full name of any employee
            i/p :  no arguments
            o/p : retuns fullname of employee
        """
        return f"{self.firstname}{self.lastname}"

    def mialID(self):
        return f"{self.firstname}{self.lastname}.alifsemi.com"

    def apply_raise (self):
        return int(self.pay*self.raise_amt)



class developer (employee):
    raise_amt=1.1
    def __init__ (self,firstname,lastname,pay,prog_lang):
        super().__init__(firstname,lastname,pay)
        self.prog_lang=prog_lang

class manager (employee):
    def __init__ (self,firstname,lastname,pay,report_emp=None):
        super().__init__(firstname,lastname,pay)
        if report_emp == None:
            self.report_emp = []
        else:
            self.report_emp=report_emp
    def add_emp(self,emp):
        #print ("Adding employee")
        if emp not in self.report_emp:
            self.report_emp.append(emp)
    def del_emp(self,emp):
        if emp in self.report_emp:
            self.report_emp.remove(emp)
    def print_emp(self):
        for i in self.report_emp:
            print (i.fullname())


dev01=developer("veera brahmam","vannem reddi",3800000,"python")
emp02=employee ("prasad","jampana",400000)
dev03=developer("bhaskara rao","vannem reddi",800000,"natural")

print (dev01.apply_raise())
print (emp02.apply_raise())

man=manager("prakash","N",5000000,[dev01])

man.add_emp(dev03)
man.print_emp()
man.del_emp(dev03)
man.print_emp()

print (isinstance (man,employee))
print (issubclass (manager,developer))
#print (help(developer))
#print (dev01.fullname())
#print (dev01.mialID())
