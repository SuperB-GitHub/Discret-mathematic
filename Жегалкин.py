from prettytable import PrettyTable

# Функция посторения таблицы истинности
def Table(a):
    table=PrettyTable()
    table.field_names=['x','y','z','f']
    table.add_row(['0','0','0',a[0]])
    table.add_row(['0','0','1',a[1]])
    table.add_row(['0','1','0',a[2]])
    table.add_row(['0','1','1',a[3]])
    table.add_row(['1','0','0',a[4]])
    table.add_row(['1','0','1',a[5]])
    table.add_row(['1','1','0',a[6]])
    table.add_row(['1','1','1',a[7]])
    print('Таблица истинности:')
    return table

# Функция метода треугольником        
def Triangle(a):
    print(' '.join(a).center(20))
    post=[a[0]]
    bylfun1=a
    for l in range(len(a)-1):
        bylfunft1=bylfun1
        lenbfft=len(bylfunft1)-1
        bylfunft=''
        for i in range(lenbfft):
            bylfunft+=logic(bylfunft1[i],bylfunft1[i+1])
        post.append(bylfunft[0])
        print(' '.join(bylfunft).center(20))
        bylfun1=bylfunft
    print(Jegalkin(post))
    return post

# Функция преобразования Жегалкина
def Jegalkin(a):
    table_ist={0:'1',1:'z',2:'y',3:'yz',4:'x',5:'xz',6:'xy',7:'xyz'}
    prejeg=[]
    
    for i in range(len(a)):
        if a[i]=='1':
            prejeg.append(table_ist[i])
    prejeg='⨁ '.join(prejeg)
    print('')
    print('Полином Жегалкина:')
    return prejeg

# Функция логики(Исключающее или)
def logic(a,b):
        if (a=='0' and b=='0') or (a=='1' and b=='1'):
            return '0'
        else:
            return '1'
# Функция метода БПФ
def Foure(a):
    print(' '.join(a).center(17))
    bylfun1=a
    bylfunft=''
    for i in range(0,len(a),2):
        bylfunft+=bylfun1[i]
        bylfunft+=logic(bylfun1[i],bylfun1[i+1])
    print(' '.join(bylfunft).center(17))

    bylfun1=bylfunft[0]+bylfunft[1]
    for i in range(0,2):
        bylfun1+=logic(bylfunft[i],bylfunft[i+2])
    bylfun1+=bylfunft[4]+bylfunft[5]
    for i in range(4,6):
        bylfun1+=logic(bylfunft[i],bylfunft[i+2])
    print(' '.join(bylfun1).center(17))
    
    print('-'*17)
    bylfunft=bylfun1[0:4]
    for i in range(4):
        bylfunft+=logic(bylfun1[i],bylfun1[i+4])
    print(' '.join(bylfunft).center(17))    
    print(Jegalkin(bylfunft))
    return bylfunft

#Функция ввода и проверки
bylfun=input('Введите б.ф. для 3-ех переменных (слитно): ')
u=0
while u!=1:
    if len(bylfun)==8 and bylfun.isdigit()==True:
        for i2 in range(len(bylfun)):
            if '0' in bylfun[i2] or '1' in bylfun[i2]:
                continue
            else: bylfun=input('Введите цифры б.ф. для 3-ех переменных(8 цифр состоящие из 0 и 1): ')
        u=1
    else:
        bylfun=input('Введите цифры б.ф. для 3-ех переменных(8 цифр): ') 
print('Всё правильно! Ваша функция:')
print(bylfun)
print("")

print(Table(bylfun))
print("")

print("Метод треугольника:")
post = Triangle(bylfun)
print("")

print("Обратный треугольник:")
Triangle(post)
print("")

print('Метод БПФ:')
post = Foure(bylfun)
print("")

print('Метод БПФ, но обратно:')
Foure(post)
print("")