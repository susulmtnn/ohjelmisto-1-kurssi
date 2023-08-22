'''
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
'''

bottom = float(input("Anna suorakulmion kannan pituus"))
side = float(input("Anna suorakulmion sivun pituus"))
print("Suorakulmion piiri="+ str(((bottom*2)+(side*2))))
print("Suorakulmion pinta-ala=" + str(bottom*side))