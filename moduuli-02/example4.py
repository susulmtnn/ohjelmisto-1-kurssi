#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
#Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
listnum = list(input("Anna kolme kokonaislukua"))
num1 = int(listnum[0])
num2 = int(listnum[1])
num3 = int(listnum[2])
print("Summa= " + str((num1+num2+num3)) +"\n" +
      "Tulo= " + str((num1*num2*num3)) + "\n" +
      "Keskiarvo= " + str((round((num1+num2+num3)/3, 2))))