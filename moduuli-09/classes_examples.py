#laajennetaan students esimerkkiä
#opiskelija kuuluu tietylle kurssille joilta voi poistua
#kurssit kuuluvat tietylle koululle.
#1 tehdään 3 opiskelijaa ja luodaan 3 kurssia. Kursseihin 1 ja 2 lisätään opiskelijoita.
#Luodaan kaksi koulua: Metropolia ja Laurea. Molemmat saa yhden kurssin.
#kurssi toimii omana luokkanaan ja sillä on nimi ja lista opiskelijoista

class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.classeslist = []
    def remove_course(self, course):
        self.classeslist.remove(course)

    def add_course(self, course):
        self.classeslist.append(course)

    def fire_alarm(self):
        print("Tulipalo")
        for i in self.classeslist:
            print(f"Kurssi käynnissä: {i.name}")
            i.check_students_in_class()
            i.check_students_in_class

class Luokka:
    def __init__(self, name):
        self.name = name
        self.student = []

    def check_coursename(self):
        print(self.name)

    def check_students_in_class(self):
        for student in self.student:
            print(student.name)

    def remove_student(self, student):
        self.student.remove(student)

    def add_student(self, student):
        self.student.append(student)

    def add_credits_to_students(self, credits):
        for student in self.student:
            #kutsutaan olion metodeja
            student.add_credits(credits)
            student.say_hello()


class Student:

    count=0

    def __init__(self, name, age=15): #konstruktori tai rakentaja. Alustetaan uusi luokka
        #age oletusarvo 15, ellei erikseen määritelty toisin.
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        #print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")

    def say_hello(self):
        print(f"Morjes, olen {self.name}, {self.age}. Minulla on {self.credits} opintopistettä.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        if self.credits + credits < 0:
            self.credits=0
        else: self.credits = self.credits + credits



st1 = Student("Matti", 56)
st1.age = "56"
st1.add_credits(22)

st2 = Student("Maija", 22)

#st1.change_name("Uusi nimi")
st2.add_credits(3)
st1.add_credits(15)
st1.say_hello()
st2.say_hello()
st3 = Student("Iines", 33)
st3.add_credits(15)
st3.say_hello()
st4 = Student("Iines2", 33)
st4.add_credits(15)
st4.say_hello()
print(f"opiskelijoita kurssilla: {Student.count}")

'''
students = []
for i in range(10):
    new_student = Student(f"Opiskelija {i}").say_hello()
    students.append(new_student)
students.append(st1)
students.append(st2)


for student in students:
    student.say_hello()
'''
course1 = Luokka("Ohjelmisto1")
course1.check_coursename()

course2 = Luokka("Ohjelmisto2")
course2.check_coursename()

#lisätään oppilaat kursseille
#St1 ja st2 ovat ohjelmisto 1 kurssilla. St3 on molemmilla. St4 on ohjelmisto2 kurssilla

course1.student.append(st1)
course1.student.append(st2)
course1.check_students_in_class()

#parempi tapa on käyttää metodeja tähän toimintoon.
#Student-olio (tai oikeastaan viittaus siihen) annetaan metodikutsun parametrina

course2.add_student(st2)
course2.add_student(st3)
course1.check_coursename()
course1.check_students_in_class()
course2.check_coursename()
course2.check_students_in_class()
course2.add_credits_to_students(100)
scool1 = School("Metropolia", "Espoo")
scool2 = School("Laurea", "Helsinki")
scool1.add_course(course1)
scool2.add_course(course2)

#koululla on palohälytys. Prinntaa koulun nimi, lokaatio, kurssit ja opiskelijat
scool1.fire_alarm()
