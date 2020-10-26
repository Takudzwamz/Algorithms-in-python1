from random import randint

while True:
    print("Options:")
    print("Enter '1' for first easy option: ")
    print("Enter '2' for second pro programmer option: ")
    print("Enter '3' toend the program: ")
    user_input = input(": ")
    if user_input == "5":
        break
    elif user_input == "1":
        symbols='qwertyuiopasdfghjklzxcvbn'
line = input("Введите строку: ")

letters = list(set(line))

if len(letters) > 3:
    delline=[]
    for i in (1,2,3):
        delline.append(letters[i])
    newline=''
    for i in line:
        if i not in delline:
            newline+=i
    print('Удаленные сиволы: ',delline)
    print('Результирующая строка : ',newline)
else:
    n = len(letters)
    while n < 4:
        d = symbols[randint(0,len(symbols))]
        if d not in letters:
            k=randint(0,len(line))
            line=line[:k]+d+line[k:]
            n += 1
    print('Новая строка: ')
    print(line)

symbols='qwertyuiopasdfghjklzxcvbn'

line = input("Введите строку: ")

letters = list(set(line))

if len(letters) > 3:
    delline=[]
    for i in (1,2,3):
        delline.append(letters[i])
    newline=''
    for i in line:
        if i not in delline:
            newline+=i
    print('Удаленные сиволы: ',delline)
    print('Результирующая строка : ',newline)
else:
    n = len(letters)
    while n < 4:
        d = symbols[randint(0,len(symbols))]
        if d not in letters:
            k=randint(0,len(line))
            line=line[:k]+d+line[k:]
            n += 1
    print('Новая строка: ')
    print(line)
        


