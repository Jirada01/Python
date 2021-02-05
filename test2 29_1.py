import os
shoplist=[0,0,0,0,0,0]
price=[15,25,40,80,54,10]
choose_list=['1.สบู่','2.ยาสีฟัน','3.ยาสระผม','4.ครีมอาบน้ำ','5.น้ำยาบ้วนปาก','6.เยลลี่','7.ออกจากรายการ']
def menu():
    global choice
    print('*'*20)
    print(' ')
    print('โปรแกรมร้านค้าออนไลน์\n')
    print('*'*20)
    print(' 1. แสดงรายการสินค้า\n 2. หยิบสินค้าเข้าตะกร้า\n 3. แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4. หยิบสินค้าออกจากตะกร้า\n 5. ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')

def รายการสินค้า():
    global choice
    print('รายการสินค้า')
    print('*'*20)
    print(' 1.สบู่ 15 บาท\n 2.ยาสีฟัน 25 บาท\n 3.ยาสระผม 40 บาท\n 4.ครีมอาบน้ำ 80 บาท\n 5.น้ำยาบ้วนปาก 54 บาท\n 6.เยลลี่ 10 บาท\n ')

def สินค้า():
    global choice
    for x in range(0,7):
        print(choose_list[x])
    a = int(input('เลือกหยิบสินค้าหมายเลข: '))
    if a==1 :
        shoplist[0] +=1
    elif a==2 :
        shoplist[1] +=1
    elif a==3 :
        shoplist[2] +=1
    elif a==4 :
        shoplist[3] +=1
    elif a==5 :
        shoplist[4] +=1
    elif a==6 :
        shoplist[5] +=1
    elif a==7 :
        menu()

def สินค้าที่หยิบ ():
    print('-'*10,'สินค้าที่หยิบไป มีดังนี้','-'*10)
    print("{0:-<20}{1:-<13}{2:-<13}{3}".format("สินค้าที่หยิบ","ราคา","จำนวน","ราคารวม"))
    for i in range (0,5):
      print("{0:-<20}{1:-<13}{2:-<13}{3}".format(choose_list[i],price[i],shoplist[i],shoplist[i]*price[i]))  

def หยิบสินค้าออก():
    global choice
    for x in range(0,7):
        print(choose_list[x])
    a = int(input('เลือกหยิบสินค้าออกหมายเลข: '))
    if a==1 :
        shoplist[0] -=1
    elif a==2 :
        shoplist[1] -=1
    elif a==3 :
        shoplist[2] -=1
    elif a==4 :
        shoplist[3] -=1
    elif a==5 :
        shoplist[4] -=1
    elif a==6 :
        shoplist[5] -=1
    elif a==7 :
        menu()

def screen_clear():
        clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        os.system('cls')
        รายการสินค้า()
    elif choice == '2':
        os.system('cls')
        สินค้า()
    elif choice == '3':
        os.system('cls')
        สินค้าที่หยิบ()
    elif choice == '4' :
        หยิบสินค้าออก()
        os.system('cls')
    elif choice == '5' :
        b = input('ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n : ')
        if b == 'y' :
            os.system('cls')
        elif b == 'n' :
            os.system('cls')
            break