import random

password = []
upperCase1 = chr(random.randint(65,90))
upperCase2 = chr(random.randint(65,90))
password.append(upperCase1)
password.append(upperCase2)

lowerCase1 = chr(random.randint(97,122))
lowerCase2 = chr(random.randint(97,122))
password.append(lowerCase1)
password.append(lowerCase2)

simbol1 = chr(random.randint(33,47))
simbol2 = chr(random.randint(33,47))
password.append(simbol1)
password.append(simbol2)

number1 = chr(random.randint(48,57))
number2 = chr(random.randint(48,57))
password.append(number1)
password.append(number2)

random.shuffle(password)
print(*password, sep="")
