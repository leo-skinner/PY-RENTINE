import time

name = input("What is your name? ")
time.sleep(1)

welcome = "Hello "+name+"!"
print(welcome)
time.sleep(1)

age = int(input(name + ", how old are you?"))
time.sleep(1)

if age > 30:
    print("You are too old, "+name+"!")
else:
    print("Hey "+name+", you are young pal!")
time.sleep(1)

print(name+", do you know, I am a computer. I can do anything with numbers...")
num1 = int(input("Please, insert a number :"))
num2 = int(input("Now, insert another number :"))
print("Thinking...")
time.sleep(1)
result = num1+num2

print("The sum between "+str(num1)+" and "+str(num2)+" is"+str(result))
