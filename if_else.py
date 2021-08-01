# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

a=[1,2,3]
b=[1,2,3]

if a == b :
    print ("Both are eual")
else:
    print ("Both are not equal")

print ('values is :',id(a))

if a is b :
    print ("Both addess are same ")
else:
    print ("Both addressed are difference")
