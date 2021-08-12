class employee:
    Salary_hike=1.05
    def __init__(self,name,lastname,sal):
        self.name=name
        self.lastname=lastname
        self.mail=self.name+self.lastname+"@alifsemi.com"
        self.sal=sal

    def fullname(self):
        return f"{self.name}{self.lastname}"

    def hike(self):
        return self.sal*employee.Salary_hike

emp01=employee ("veera brahmam","vannem reddi",100000)

print (emp01.fullname())
print (emp01.Salary_hike)
print (emp01.sal)
print (emp01.Salary_hike)
print (emp01.hike())
