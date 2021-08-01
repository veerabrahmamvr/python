student={'name':"veera brahmam",'age': 98, 'rol num': 'L3EC338'}

#print (student.get('hi',"entry is not available"))

student.update({'age': [12,38,98] , 'phone': 9916673623})
student.update({'city':'bangalore'})

print (student)

print (student.items())

#del student['rol num']
#student.pop('rol num')

for i,j in student.items():
    print (i,j)
