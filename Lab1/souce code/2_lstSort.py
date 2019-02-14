lst = [("John",("physics",80)),("Daniel",("science",90)),("John",("science",95)),("Mark",("maths",100)),("Daniel",("history",75)),("Mark",("social",95))]

lstDict = {}

"""sort through the list"""
for name in lst:
    #if student names in dict already then just add their scores and classes
     if name[0] in lstDict:
         lstDict[name[0]] += [name[1]]
         lstDict[name[0]].sort()
     #if student name not in dict, add their name and the first class and grade
     else:
         lstDict[name[0]] = [name[1]]

print(lstDict)


