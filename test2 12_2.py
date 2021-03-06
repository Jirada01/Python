import sqlite3
conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
c = conn.cursor()
c.execute ('''CREATE TABLE student (id integer PRIMARY KEY AUTOINCREMENT,
    No varchar(30) NOT NULL,
    name varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(30) NOT NULL,
    age varchar(30) NOT NULL,
    year varchar(30) NOT NULL)''')
conn.commit()
conn.close()

def insertTousers (No,name,email,sex,age,year) :
    try :
        conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
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
    No_2 = str(input("ลำดับที่ : "))
    name_2 = str(input("ชื่อ-นามสกุล : "))
    email_2 = str(input("อีเมลล์ : "))
    sex_2 = str(input("เพศ : "))
    age_2 = str(input("อายุ : "))
    year_2 = str(input("ชั้นปี : "))
        
    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
    c = conn.cursor()
    try :
        data = (str(No_2),str(name_2),str(email_2),str(sex_2),str(age_2),str(year_2))

        c.execute('INSERT INTO student (No,name,email,sex,age,year) VALUES (?,?,?,?,?,?)',data)
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
    print("------------------------รายชื่อนักเรียน------------------------")
    print("="*50)
    print("ลำดับที่---------ชื่อ-นามสกุล----------email-----เพศ----อายุ----ชั้นปี----")
    print("-"*50)
    import sqlite3

    conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM student''')

    result = c.fetchall()
    for x in result :
        print(x)
        
def edit():
    print(" ")
    print("------------------------แก้ไขนักเรียน------------------------")
    print("="*50)
    print("ลำดับที่---------ชื่อ-นามสกุล----------email-----เพศ----อายุ----ชั้นปี----")
    print("-"*50)
    import sqlite3
    conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM student''')

    result = c.fetchall()
    for x in result :
        print(x)
        a = str(input("\nกรุณาระบุ ลำดับที่ ที่ท่านต้องการแก้ไข "))
        print("แก้ไขเป็น")
        no_3 = input("ลำดับที่ : ")
        name_3 = input("ชื่อ-นามสกุล : ")
        email_3 = input("อีเมลล์ : ")
        sex_3 = input("เพศ : ")
        age_3 = input("อายุ : ")
        year_3 = input("ชั้นปี : ")

        import sqlite3
        conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
        c = conn.cursor()
        try :
            data = (str(no_3),str(name_3),str(email_3),str(sex_3),str(age_3),str(year_3),str(a))
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
        print("------------------------ลบรายชื่อนักเรียน------------------------")
        print("="*50)
        print("ลำดับที่---------ชื่อ-นามสกุล----------email-----เพศ----อายุ----ชั้นปี----")
        print("-"*50)
        import sqlite3

        conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
        c = conn.cursor()
        c.execute('''SELECT * FROM student''')

        result = c.fetchall()
        for x in result :
            print(x)

        a1 = str(input("\nกรุณาเลือก ลำดับที่ ที่ต้องการลบ "))
        import sqlite3
        conn = sqlite3.connect(r"D:\Jirada_Python\example.db")
        c = conn.cursor()
        try :
            c.execute("DELETE FROM student WHERE No ="+str(a1))
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
        o =str(input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :"))
        if o == "y":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กลับเข้าสู่โปรแกรม")