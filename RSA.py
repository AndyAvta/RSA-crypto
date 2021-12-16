from random import randint

def coder_key_open(): # функция кодирования RSA методом при помощи открытого ключа уже существующего
    message=input("Введите сообщение которое необходимо закодировать")
    key_1=int(input("Введите первую часть открытого ключа"))
    key_2 = int(input("Введите вторую часть открытого ключа"))
    ass=[]
    for i in range(0,len(message)):
        ass.append((((ord(message[i]))**key_1)%key_2))
    print(ass)


def decoder_key_sec(): # функцмя раскодирования RSA методом при помощи секретного ключа уже существующего
    message = input("Введите сообщение которое необходимо раскодировать").split(", ")
    key_1 = int(input("Введите первую часть секретного ключа"))
    key_2 = int(input("Введите вторую часть секретного ключа"))
    ass = []
    otv=""
    for i in range(0, len(message)):
        ass.append(chr(((int(message[i])) ** key_1) % key_2))
        otv+=ass[i]
    print(otv)

def key():
    print("Происходит создание ключей для нового сообщения")
    lst = [2]
    for i in range(3, 100, 2): #Создание алгоритма для нахождения простых чисел
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    # for i in range(11):#Удаление первых 11 элементов списка с простыми числами для упрощения работы программы и повышения качества ключей для шифрования
    #     lst.pop(0)
    while True: #Выбор случайных простых чисел в списке простых чисел
        p=lst[randint(0,len(lst)-1)]
        q=lst[randint(0,len(lst)-1)]
        if p==q:
            pass
        else:
            break
    n=p*q#Модуль произведения(требуемое вычисление для открытого ключа и секретного)
    F=(p-1)*(q-1) #Вычисление функции Эйлера
    try:
        lst_2=[]
        for i in range(0,len(lst)):
            if lst[i]<F and lst[i]%F!=0:
                lst_2.append(lst[i])
        e=lst_2[randint(0,len(lst_2))]
    except IndexError:
        key()

    d=0
    for i in range(0, 100000):
        if (i * e) % F == 1 and i != e:
            d=i
            break
    if d == 0:
        key()

    print(e,n,"открытй ключ")
    print(d,n,"Секретнвй ключ ")

while True: # Начало программы
    print("Выберите из перечня требуемое действие и введите его:Выход,Создать ключ, Шифрование или Расшифрование")
    intu=input()
    if intu=="Выход":
        exit()
    elif intu == "Создать ключ":
        print(key())
    elif intu == "Шифрование":
        print(coder_key_open())
    elif intu == "Расшифрование":
        print(decoder_key_sec())
    else:
        print("Ошибка. Повторите ввод косанды")




