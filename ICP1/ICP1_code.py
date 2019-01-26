# Part 1
# The biggest difference between python 2 and three are print statements, integer and floor division
# python 2 integer division for floats: 5/2=2, 5.0/2=2.5 ,floor division: 5//2=2, print "string"
# python 3 integer division 5/2=2.5, floor division: 5//2=2, print("string")

# Part2
num = int(input("Enter a number: "))
rev = 0

while(num>0):
    rev = rev * 10
    rev = rev + num % 10
    num = num // 10
print(rev)

num1 = int(input("enter one number: "))
num2 = int(input("enter a second number: "))
Mul = num1*num2
print("%d Multiplied by %d is %d" % (num1,num2,Mul))

# Part 3
sentence = input("enter a sentence: ")
letters = 0
words = 1
digits = 0
for i in sentence:
    if i.isdigit():
        digits += 1
    if i.isalpha():
        letters += 1
    if i == ' ':
        words += 1
print("Words: %s Letters: %s digits: %s" % (words,letters,digits))
