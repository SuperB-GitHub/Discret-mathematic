# Функция нахождения НОД
def NOD():
    nodinston=[]
    for i in range(len(fin_mnoj)):
        in_fin_mnoj=fin_mnoj[i]
        for o in range(2,50):
            if o in in_fin_mnoj:
                nodinston.append(o)
    itog=1
    for p in range(2,50):
        if len(fin_mnoj)==1 or len(fin_mnoj)==0:
            continue
        else:
            if len(fin_mnoj)==nodinston.count(p):
                itog=p
    print('Ваш НОД:')
    return itog

# Функция нахождения НОК
def NOK1():
    nokinston=[]
    for i in range(len(fin_mnoj)):
        in_fin_mnoj=fin_mnoj[i]
        for d in range(len(in_fin_mnoj)):
            if in_fin_mnoj[d] not in nokinston:
                nokinston.append(in_fin_mnoj[d])
            elif nokinston.count(in_fin_mnoj[d]) < list(in_fin_mnoj).count(in_fin_mnoj[d]):
                nokinston.append(in_fin_mnoj[d])
    itog=1
    for i in range(len(nokinston)):
        itog*=nokinston[i]
    print('Ваш НОК:')
    return itog

# Функция разложения на множители
def Packlad(n):
    mnoj = []
    delit = 2
    
    while n >= delit:
        if n % delit == 0:
            mnoj.append(delit)
            n = n / delit
        else:
            delit = delit + 1
    
    return mnoj

# Функции для ввода и проверка на 0
num1=[]
num=input('Введите числа через пробел, нельзя вводить ноль: ').split()
for i in range(len(num)):
    if num[i]!='0':
        num1.append(num[i])
    else:
        print('Ваш 0 был удален')
print('Ваши числа: ',num1)

fin_mnoj=[]
for i in range(len(num1)):
    try:
        numb=abs(int(num[i]))
    except:
        fin_mnoj.append([float(num[i])])
    else:
        fin_mnoj.append(Packlad(numb))
print('Множители все: ', fin_mnoj)
print(NOD())
print(NOK1())
