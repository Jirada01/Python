dictionary = {}
def menu():
    global choice
    print(" ")
    print('พจนานุกรม\n')
    print(' 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n ')
    choice = input('Input Choice : ')

def word_2():
    word = input('เพิ่มคำศัพท์ : ')
    type_word = input('ชนิดคำศัพท์(n. , v. , adj. ,) : ' )
    mean = input ('ความหมาย : ')
    dictionary[word] = type_word,mean
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def show():
    print('-'*40)
    print(' '*10+'คำศัพท์ของคุณมีดังนี้'+' '*10)
    print('-'*40)
    print('{0:-<15}{1:-<15}{2:-<8}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for k in dictionary:
        print('{0:-15}{1:-15}{2}'.format(k,'',dictionary[k]))

while (True) :
    menu()
    if choice == '1':
        word_2()
    elif choice == '2':
        show()
