# Oliot voivat olla vuorovaikutuksessa keskenään
# tätä suhdetta kutsutaan assosiaatioksi

'''
    1. aluksi luodaan kolme opiskelijaa
    2. sitten luodaan kolme kurssia, kusseihin 1 ja 2 molempiin 2 opiskelijaa
    3. viimeisenä luodaan kaksi koulua, Mp saa kaksi ja Laurea yhden kurssin
'''

# laajennetaan ensin opiskelija esimerkkiä niin että luodaan Kurssi luokka.
# Opiskelija kuuluu tietylle kurssille (esim. Ohjelmisto1)
# Kurssille osallistuu ja sieltä poistuu opiskelijoita

'''
Kurssi siis toimii omana luokkana (class), sillä se pyörii opiskelijasta huolimatta.

Kurssilla on:
    * nimi
    * lista opiskelijoista
Kurssille voi:
    * tsekata kurssin nimen (check_coursename)
    * lisätä opiskelijan (add_student)
    * poistaa opiskelijan (remove_student)
    * printata osallistujalistan (check_students_on_course)
    * lisätä kaikille jokaiselle osallistujalle opintopisteitä yhdellä kerralla (add_credits_to_all)

Tehdään nyt molempien luokkien välinen vuorovaikutus.
    * lisätään kurssille opiskelijoita
    * kun opintopisteitä lisätään opiskelijoille, kaikki opiskelijat tervehtivät takaisin
    ja kertovat nimensä sekä opintopisteensä, tähän käytetään Students luokan say_hello metodia
'''

# laajennetaan lisää, tietyt kurssit kuuluvat myös tiettyy kouluun.
# Opiskelija voi ilmoittautuessaan kurssille, olla esim. kahdessa eri koulussa yhtäaikaa
# (esim. Metropolia ja Laurea). Käytännössä koulut hallitsevat kursseja, kurssit opiskelijoita

'''
Koulukin toimii omana luokkanaan (class), se sisältää kursseja ja opiskelijoita
Koululla on nimi ja lokaatio. Koulu voi
    * lisätä kurssin (add_course)
    * poistaa kurssin (remove_course)
    * lähettää palohälytyksen, silloin printataan koulun nimi, lokaatio, kurssit ja oppilaat (fire_alarm)
'''

class School:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def fire_alarm(self):
        print(f'Kamalaa! 🔥 Palohäytys 🚒 koulussa {self.name}, lokaatiossa {self.location}')
        for course in self.courses:
            print(f'Kurssi käynnissä: {course.name}')
            course.check_students_on_course()


class Course:

    def __init__(self, name):
        self.name = name
        self.students = []

    def check_coursename(self):
        print(f'Kurssin nimi on: {self.name}')

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def check_students_on_course(self):
        for student in self.students:
            # print(student)
            print(student.name)

    def add_credits_to_all(self, credit_units):
        for student in self.students:
            # kutsutaan Student olion metodeja!!!
            student.add_credits(credit_units)
            student.say_hello()

class Student:

    count = 0

    def __init__(self, name, age=15):  # age oletusarvo 15, jossei määritelty kutsussa
        self.name = name
        self.age = age
        self.credits = 0
        Student.count += 1
        # print(f"Uusi opiskelija luotu. Opiskelijoita on nyt yhteensä {Student.count}.")

    def say_hello(self):
        print(f"Morjes! olen {self.name}, {self.age} vuotta. "
              f"Minulla on {self.credits} opintopistettä.")

    def change_name(self, new_name):
        self.name = new_name

    def add_credits(self, credits):
        # estä opintopisteiden meneminen negaativiseksi
        if self.credits + credits < 0:
            self.credits = 0
        else:
            self.credits = self.credits + credits


print('Hei, tervetuloa kouluun!')

# luodaan 3 opiskelijaa ja annetaan opintopisteet
st1 = Student("Mikko Mallikas", 38)
print(st1)
st1.add_credits(3)
st1.say_hello()
st2 = Student("Iines Ankka", 34)
print(st2)
st2.add_credits(3)
st2.say_hello()
st3 = Student("Rob Fury", 20)
print(st3)
st3.add_credits(3)
st3.say_hello()

print(f'Uusia opiskeljoita on kurssilla {Student.count}')

print("*==========*")

# Luodaan kaksi kusrssia, tsekataan kurssien kurssin nimi (metodi)
course1 = Course('Ohjelmisto1')
course1.check_coursename()

course2 = Course('Ohjelmisto2')


print("*==========*")

# lisätään oppilaat kursseille
# Mikko ja Iines ovat Ohjelmisto 1 kurssilla
# Iines ja Rob ovat Ohjelmisto 2 kurssilla

course1.check_coursename()
course1.students.append(st1)
course1.students.append(st2)
course1.check_students_on_course()

print("*==========*")

# parempi tapa on käyttää metodeja tähän toimintoon
# Student-olio (tai oikeastaan viittaus siihen) annetaan metodikutsun parametrina

course2.check_coursename()
course2.add_student(st2)
course2.add_student(st3)
course2.check_students_on_course()

print("*==========*")

# Oppilaat olet kurssilla 2 tosi ahkeria ja saavat lisää opintopisteitä!!!
course2.add_credits_to_all(5)

# Luodaan nyt kaksi koulua
# Metropolia ja Laura. MP saa Ohelmisto 1 ja Laurea Ohjelmisto 2.
# Molemmista tallennetan nimi ja lokaatio

print("*==========*")

school1 = School('Metropolia', 'Karamalmi')
school2 = School('Laurea', 'Leppävaara')
school1.add_course(course1)
school2.add_course(course2)

# apua koululla on palohälytys!!!!!
# Printatkaa koulun nimi, lokaatio, kurssit ja opiskelijat

school1.fire_alarm()




