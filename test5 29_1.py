import time
name = []
score = []
time_ = []
hit = []
def time_1() :
    time_is = time.localtime()
    a = time.strftime('%d %B %Y , %H:%M:%S',time_is)
    print(a)

num = int(input('กรุณาพิมพ์จำนวนผู้ซ้อมยิง :'))
for i in range (num) :
    print('ป้อนข้อมูลคนที่ ', 1+i)
    name_ = input('ชื่อผู้ซ้อม : ')
    score_ = float(input('คะแนน : '))
    time_2 = float(input('ระยะเวลาที่ใช้ : '))
    name.append(name_)
    score.append(score_)
    time_.append(time_2)
    hit.append(score_/time_2)
for i in range(num) :
    j =i
    for j in range(num):
        if hit[i]>hit[j]:
            a,b,c,d = hit[i],name[i],score[i],time_[i]
            hit[i],name[i],score[i],time_[i] = hit[j],name[j],score[j],time_[j]
            hit[j],name[j],score[j],time_[j] = a,b,c,d
time_is = time.localtime()
a = time.strftime('%A',time_is)
b = time.strftime('%Y',time_is)
print('Shotgun'+a+'')