# Store user input as two variables
python = input("enter a list of students in the python class: ").split(",")
webapp = input("enter a list of students in the Web Application class: ").split(",")

# Places user input into a list and
print("Students attending both classes: ", list(set(python) & set(webapp)))
print("Students only attending one class and not the other: ", list(set(python) ^ set(webapp)))
