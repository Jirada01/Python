import os
choice = 0
filename =""

def menu():
    global choice
    print('Menu\n 1.Open Calculator\n 2.Open Notpad\n 3.Exit ')
    choice = input('Select Menu : ')

def opennotepad():
    filename = 'C:\\Windows\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Calculate Number %s' %filename)
    os.system(filename)
while True:
    menu()
    if choice == '1':
        opencalculator()
    elif choice == '2':
        opennotepad()
    else:
        break