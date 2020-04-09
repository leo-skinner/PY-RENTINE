import time

name = input("What is your name? ")
time.sleep(2)

welcome = "Hello "+name+"!"
print(welcome)
time.sleep(2)

age = int(input(name + ", how old are you?"))
time.sleep(2)

if age > 30:
    print("You are too old, "+name+"!")
else:
    print("Hey "+name+", you are young pal!")
