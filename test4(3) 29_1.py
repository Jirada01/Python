dictionary = {}
def menu():
    global choice
    print(" ")
    print('พจนานุกรม\n')
    print(' 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n ')
    choice = input('Input Choice : ')

def เพิ่มคำศัพท์():
    word = input('เพิ่มคำศัพท์ : ')
    type_word = input('ชนิดคำศัพท์(n. , v. , adj. ,) : ' )
    mean = input ('ความหมาย : ')
    dictionary[word] = "{0: <15}{1: <15}".format(type_word,mean)
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def แสดงคำศัพท์():
    print('-'*40)
    print(' '*10+'คำศัพท์ของคุณมีดังนี้'+' '*10)
    print('-'*40)
    print('{0:-<15}{1:-<15}{2:-<8}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for i in dictionary:
        print('{0: <15}{1: <15}'.format(i,dictionary[i]))

def ลบคำศัพท์():
    remove = input('พิมพ์คำศัพท์ที่ต้องการลบ : ')
    a = input('ต้องการลบ'+remove+'ใช่หรือไม่ (y/n) : ')
    if a == 'y' :
        dictionary.pop(remove)
        print('ลบ',remove,'เรียบร้อยแล้ว')
    elif a == 'n' :
        print(' ')
while True:
    menu()
    if choice == '1':
       เพิ่มคำศัพท์()
    elif choice == '2':
        แสดงคำศัพท์()
    elif choice == '3' :
        ลบคำศัพท์()
    elif  choice == '4' :
        a = input('ต้องการออกโปรแกรมใช่หรือไม่ y/n : ')
        if a == 'y' :
            print('ออกจากโปรแกรมเรียบร้อย')
        elif a == 'n' :
            break