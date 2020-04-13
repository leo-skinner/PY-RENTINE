import time

name = input("What is your name? ")
time.sleep(1)

welcome = 'Hello {}! Nice to meet you!'.format(name)
print(welcome)
time.sleep(1)

age = int(input('{}, how old are you? '.format(name)))
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

print('The sum between {} and {} is {}'.format(num1, num2, result))
time.sleep(1)
word = input('{}, please type any word: '.format(name))
print('Now I will dissecate this word...')
time.sleep(1)

print('Primitive type is {}'.format(type(word)))
print('has only spaces ?', word.isspace())
print('Is number ?', word.isnumeric())
print('Is alphabetical ?', word.isalpha())
print('Is lower case ?', word.islower())
print('Is upper case ?', word.isupper())
print('Is capitalized ?', word.istitle())
time.sleep(1)
middle_number = int(input('{}, now type any number: '.format(name)))
print('the predecessor of number {} is {} and forward number is {}'.format(
    middle_number, middle_number-1, middle_number+1))
time.sleep(1)
print('Bye!')
