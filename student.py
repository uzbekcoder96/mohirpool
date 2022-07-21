class Student:
    
    def __init__(self, id,  f_name, l_name, nationality, gender,faculty, admission_year):
         self.id = id
         self.full_name = l_name + ' ' +  f_name
         self.nationality = nationality
         self.gender = gender
         self.faculty = faculty
         self.admission_year = admission_year
         
    
  
    # Talaba ma'lumotlarini ko'rsatish      
    def display(self, ob):
        
            if isinstance(ob, Master):
                 print("Bosqich: Master")
            else:
                 print("Bosqich: Bakalavr")
            print("Student_id   : ", ob.id)
            print("Name   : ", ob.full_name)
            print("Faculty: ", ob.faculty)
            print("Admission_year : ", ob.admission_year)
            print('\n')   
            
    # Talabani qidirish    
    def find(self, id):
        for i in range(ls.__len__()):
            if(ls[i].id == id):
                    return i        
  
    # Talabani o'chirish                   
    def remove(self, id):
        i = obj.find(id)  
        del ls[i]
  
    # Talabani o'zgartirish
    def update(self, rn, No):
        i = obj.find(rn)
        roll = No
        ls[i].id = roll
            

class Bachelor(Student):

    def __init__(self,id, f_name, l_name, nationality, gender, faculty, admission_year, residential_hall):
        super().__init__(id, f_name, l_name, nationality, gender, faculty, admission_year)
        
        self.residential_hall = residential_hall
    
    
    def add(self,id,  f_name, l_name, nationality, gender, faculty, admission_year, residential_hall):
        obj = Bachelor(id,  f_name, l_name, nationality, gender, faculty, admission_year, residential_hall)
        ls.append(obj)

class Master(Student):

    def __init__(self,id,  f_name, l_name, nationality, gender, faculty, admission_year, supervisor_name, research_topic):
        super().__init__(id,  f_name, l_name, nationality, gender, faculty, admission_year)
        self.supervisor_name = supervisor_name
        self.research_topic = research_topic
    
    def add(self,id,  f_name, l_name, nationality, gender, faculty, admission_year, supervisor_name, research_topic):
        obj = Master(id, f_name, l_name, nationality, gender, faculty, admission_year, supervisor_name, research_topic)
        ls.append(obj)        


# Talabalar listi
ls =[]


# Bakalavr yoki Magistr ekanligini aniqlash
choice = int(input("Bosqichni tanlang:  Magistr(1)  Bakalavr(2): "))

# Bakalavr talabasini yaratish 
if choice == 1:
    obj = Master(0, '', '', '', '', '', 0, '', "")
    obj1 = Master(0, '', '', '', '', '', 0, '', "")
    obj2 = Master(0, '', '', '', '', '', 0, '', "")
    obj.add(1, 'nodir', 'alimov', 'uzbek', 'male', 'economy', 2015, 'Alex', "Job in the future")
    obj1.add(2, 'ali', 'Nodirov', 'uzbek', 'male', 'geography', 2020, 'Mali', "Aral Sea in Uzbekistan")
    obj2.add(3, 'alina', 'sobitova', 'uzbek', 'female', 'english', 2019, 'Nazima', "How inporrtant English in IT")

# Magistr talabani yaratish 
elif choice == 2:
    obj = Bachelor(0, '', '', '', '', '', 0, '')
    obj1 = Bachelor(0, '', '', '', '', '', 0, '')
    obj2 = Bachelor(0, '', '', '', '', '', 0, '')
    obj.add(1, 'nodir', 'alimov', 'uzbek', 'male', 'economy', 2015, 'Bukhara')
    obj1.add(2, 'ali', 'Nodirov', 'uzbek', 'male', 'geography', 2020, 'samarkand')
    obj2.add(3, 'alina', 'sobitova', 'uzbek', 'female', 'english', 2019, 'Tashkent')
  

# Foydalanuvchiga mavjud buyruqlarni ko'rsatish
print("\nQuyidagi amallarni bajarishingiz mumkin:  ")
print("\n1.Barcha Talabalarni ko'rish(Faqatgina o'zingiz tanlagan bosqichdagi talabalarni ko'rishingiz mumkin)\n" +
         "2.Talabani qidirish\n3.Talabani o'chirish" + 
         "\n4.Talaba ma'lumotini o'zgartirish\n5.Chiqish")

#Foydalanuvchi xoxishini aniqlash 
ch = int(input("Yuqoridagilardan birini tanlang: "))


# Foydalanuvchi istagiga ko'ra buyruqni amalga oshirish        
if(ch == 1):
    print("\n")
    print("\nTalabalar ro'yxati\n")
    for i in range(ls.__len__()):    
        obj.display(ls[i])
             
elif(ch == 2):
    print("\n Talaba topildi, ")
    s = obj.find(2)
    obj.display(ls[s])
         
elif(ch == 3):
    obj.remove(2)
    print(ls.__len__())
    print("Talaba o'chirilgandan keyingi list holati")
    for i in range(ls.__len__()):    
        obj.display(ls[i])
             
elif(ch == 4):
    obj.update(3, 2)
    
    print("O'zgarisdan keyingi list holati")
    for i in range(ls.__len__()):    
        obj.display(ls[i])
             
else:
    print("Thank You !")
