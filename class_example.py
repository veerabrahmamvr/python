class bio_data:
    def __init__ (self,name,sirname):
        self.actual_name=name
        self.S_name=sirname
        
    def fullname (self):
        full="full name of the person is : {} ."
        return full.format(self.actual_name + " " + self.S_name)
    def mailid(self):
        return f"{self.actual_name}.{self.S_name}@alifsemi.com"

person01=bio_data("VeeraBrahmam","VannemReddi")

#print (person01.S_name)
print (person01.fullname())
print (person01.mailid())
#print (person01.fullname.total())
