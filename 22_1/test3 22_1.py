food = []
print("ป้อนชื่ออาหารสุดโปรของคุณ หรือ exit เพื่อออกจากโปรแกรม")
i = 1
b= 1
while (i>0) :
    a = input("อาหารโปรดอันดับที่ "+str(i)+" คือ ")
    i += 1
    food.append(a)
    if a == "exit" :
        break 
food.remove("exit")
print("อาหารสุดโปรดของคุณมีดังนี้ ",end=" ")
for x in food :
    print(str(b)+"."+x,end=" ")
    b+=1