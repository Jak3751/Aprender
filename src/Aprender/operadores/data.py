from datetime import date
print(date.today())
print("Data do dia é : " + str(date.today()))



parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

print("calculator program")
first_number = int(input("first number: "))     #se não tivesse colocado int o resultado seria primeiro numero ao lado do segundo e não a soma como foi programado.
second_number = int(input("second number: "))
print(first_number + second_number)