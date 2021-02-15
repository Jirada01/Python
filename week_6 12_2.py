import sqlite3
conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
c = conn.cursor()
"""
c.execute ('''CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT,
    No varchar(30) NOT NULL,
    name varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(30) NOT NULL,
    age varchar(30) NOT NULL,
    year varchar(30) NOT NULL)''')
"""
conn.commit()
conn.close()

def insertTousers (No,name,email,sex,age,year) :
    try :
        conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
        c = conn.cursor()

        sql = '''INSERT INTO student (No,name,email,sex,age,year) VALUES (?,?,?,?,?,?)'''
        data = (No,name,lname,email,sex,age,year)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close()

def menu():
    global choice
    print("-"*10,"ระบบทะเบียนนักเรียน","-"*10)
    print("="*38)
    print(" เพิ่มนักเรียน กด [a]\n แสดงข้อมูลนักเรียน [s]\n แก้ไขข้อมูลนักเรียน [e]\n ลบข้อมูลนักเรียน [d]\n ออกจากโปรแกรม [x]")
    print(" ")
    choice = input('กรุณาเลือกทำรายการ : ')

def add(): 
    print("-"*10,"เพิ่มรายชื่อนักเรียน","-"*10)
    print("="*38)
    b1 = str(input("ลำดับที่ : "))
    b2 = str(input("ชื่อ-นามสกุล : "))
    b3 = str(input("อีเมลล์ : "))
    b4 = str(input("เพศ : "))
    b5 = str(input("อายุ : "))
    b6 = str(input("ชั้นปี : "))
    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
    c = conn.cursor()
    try :
        data = (str(b1),str(b2),str(b3),str(b4),str(b5),str(b6))
        
        c.execute ('INSERT INTO users (No,name,email,sex,age,year) VALUES (?,?,?,?,?,?)',data)
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :

        if conn :
            conn.close()
    print("ทำรายการเสร็จสิ้น")

def show(): 
    print(" ")
    print("-"*25,"รายชื่อนักเรียน","-"*25)
    print("="*60)
    print("No--ลำดับที่--------ชื่อ-นามสกุล--------email-----เพศ----อายุ----ชั้นปี----")
    print("-"*60)

    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')

    result = c.fetchall()
    for x in result :
        print(x)
        
def edit():
    print(" ")
    print("-"*25,"แก้ไขรายชื่อนักเรียน","-"*25)
    print("="*60)
    print("No--ลำดับที่--------ชื่อ-นามสกุล--------email-----เพศ----อายุ----ชั้นปี----")
    print("-"*60)
    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')

    result = c.fetchall()
    for x in result :
        print(x)
    a = str(input("\nกรุณาระบุ ลำดับที่ ที่ท่านต้องการแก้ไข "))
    print("แก้ไขเป็น")
    a1 = input("ลำดับที่ : ")
    a2 = input("ชื่อ-นามสกุล : ")
    a3 = input("อีเมลล์ : ")
    a4 = input("เพศ : ")
    a5 = input("อายุ : ")
    a6 = input("ชั้นปี : ")

    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
    c = conn.cursor()
    try :
        data = (str(a1),str(a2),str(a3),str(a4),str(a5),str(a6),str(a))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        
        if conn :
             conn.close()
        print("ทำรายการเสร็จสิ้น")

def delete(): 
    print(" ")
    print("-"*25,"ลบรายชื่อนักเรียน","-"*25)
    print("="*60)
    print("No--ลำดับที่--------ชื่อ-นามสกุล--------email-----เพศ----อายุ----ชั้นปี----")
    print("-"*60)
    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    result = c.fetchall()
    for x in result :
        print(x)

    c1 = str(input("\nกรุณาเลือก ลำดับที่ ที่ต้องการลบ "))
    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example2.db")
    c = conn.cursor()
    try :
        c.execute("DELETE FROM users WHERE No ="+str(c1))
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
    
        if conn :
            conn.close()
    print("ทำรายการเสร็จสิ้น")

while True: # loop choice
    menu()
    if choice == 'a':
        add()
    elif choice == 's':
        show()
    elif choice == 'e':
        edit()
    elif choice == 'd':
        delete()
    elif choice == 'x':
        z =str(input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :"))
        if z == "y":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กลับเข้าสู่โปรแกรม")