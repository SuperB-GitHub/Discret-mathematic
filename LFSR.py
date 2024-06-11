import PySimpleGUI as sg

def main(iz,bt,bk):
    bin_key = bk
    bin_text = bt
    Z = '' + iz 
    schetchik = 0 
    while len(Z) != len(bin_text):
        a = 0
        for count, c in enumerate(bin_key):
            a ^= int(c) * int(Z[schetchik + count])
        Z += str(a)
        schetchik += 1 
    Y = ''
    for count, z in enumerate(Z):
        Y += str(int(z) ^ int(bin_text[count]))
    return Y

layout = [  [sg.Text("",expand_x=True),sg.Text("Шифратор на основе сдвига регистров"),sg.Text("",expand_x=True),],
            [sg.Text("Инициальное значение: "),sg.Input(default_text='',key='iz',expand_x=True, size=(0,1)),sg.Radio('1 сдвиг',"123", size=(10,1), k='r1')],
            [sg.Text("Введите численную последовательность, большую чем инициальное значение:"), sg.Text("",expand_x=True), sg.Radio('2 сдвиг',"123", size=(10,1), k='r2')],
            [sg.Input(key='bin_text',expand_x=True, size=(0,1)),sg.Radio('3 сдвиг',"123", size=(10,1), k='r3')],
            [sg.Text(key='achtung'),sg.Radio('4 сдвиг',"123", size=(10,1), k='r4')],
            [sg.Text(key='achtung1'),sg.Radio('5 сдвиг',"123", size=(10,1), k='r5')],
            [sg.Radio('6 сдвиг',"123", size=(10,1), k='r6')],
            [sg.Radio('7 сдвиг',"123", size=(10,1), k='r7')],
            [sg.Text('Закодированная последовательность:'),sg.Input(k='Y',expand_x=True, size=(0,1),readonly=True),sg.Radio('8 сдвиг',"123", size=(10,1), k='r8')],
            [sg.Text('',expand_y=True, expand_x=True),sg.Button('Шифровать/Расшифровать'), sg.Text('',expand_y=True, expand_x=True)],
            [sg.Button('О лабораторной работе'),sg.Text("",expand_x=True),sg.Button('Выход')]]
window = sg.Window('LFSR', layout,size=(650,350), resizable=True, element_justification='right',)  
while True:
    event, values = window.read() # type: ignore
    try:
        iz=str(values["iz"])
        bt=str(values["bin_text"])
    except TypeError:
        break
    if len(bt)<len(iz) and event=='Шифровать/Расшифровать':
        window['achtung'].update('Кол-во чисел в последовательности > кол-во чисел в иницициальном значении')

    if event=='О лабораторной работе':
        sg.popup('''--------------------------------------------------------
1. Объяснить этот код
2. Прочитать задание для лаб. работы
3. Провести закодирование 3 раза, 
используя сдвиги указаные в таблице
4. Сделать отчет по работе
                    ---------------------------------------------------------''', keep_on_top=True, title='О лабораторной работе')

    if values['r1']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='1'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))

    if values['r2']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='10'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))
    
    if values['r3']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='11'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))

    if values['r4']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='100'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))

    if values['r5']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='101'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))

    if values['r6']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='110'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))

    if values['r7']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='111'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))
    
    if values['r8']==True and event=='Шифровать/Расшифровать' and len(bt)>len(iz):
        bk='1000'
        while len(iz)<4:
            iz='0'+iz
        window['iz'].update(iz)
        while len(bk)!=len(iz):
            bk="0"+bk
        window['achtung'].update('')
        window['Y'].update(main(iz,bt,bk))

    if event=='Выход' or event== sg.WIN_CLOSED:
        break