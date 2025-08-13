from array import *
val= array('i',[8,6,4])
print("old array:",val)
print()
val.append(2)
val.remove(8)
val.reverse()

l=len(val)
print("new array:",val)
print("second element in the new array:",val[1])
print("no of values in new array:",l)
