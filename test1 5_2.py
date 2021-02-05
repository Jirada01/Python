print("-"*15,"แนะนำตัว","-"*15)
class nisit :
    def __init__(self,name,id,sex,year,department,province,graduate_school) :
        self.name = name
        self.id = id
        self.sex = sex
        self.year = year
        self.department = department
        self.province = province
        self.graduate_school = graduate_school
    
    def showinsit (self):
        print('-'*30)
        print('ชื่อ-นามสกุล : ',self.name,'รหัสนักศึกษา : ',self.id,'เพศ : ',self.sex,'ชั้นปีการศึกษา : ',self.year,'สาขาวิชา : ',self.department,'จังหวัด : ',self.province,'โรงเรียนที่จบการศึกษา : ',self.graduate_school)
                

name_ =input("ชื่อ-นามสกุล : ")
id_ =input("รหัสนักศึกษา : ")
sex_ =input("เพศ : ")
year_=input("ชั้นปีการศึกษา : ")
department_=input("สาขาวิชา : ")
province_=input("จังหวัด : ")
graduate_school_=input("โรงเรียนที่จบการศึกษา : ")

x = nisit(name_,id_,sex_,year_,department_,province_,graduate_school_)
x.showinsit()
        