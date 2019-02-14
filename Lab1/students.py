#User can input students who are in the classes
python = input("enter a list of students in the python class: ").split(",")
webapp = input("enter a list of students in the Web Application class: ").split(",")
# python =["jack","ill","bob","ash"]
# webapp =["jim","bob","meg","kat"]
print("webapp: ", webapp)
print("python: ", python)
#print the common students for the classes
print("similar: ", list(set(python) & set(webapp)))
#prints the difference of students for the class
print("different: ", list(set(python) ^ set(webapp)))