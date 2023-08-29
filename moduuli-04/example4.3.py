num1= input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki")
num2 = float(num1)
num3= float(num1)

while num1 != " ":
    num1 =float(num1)
    while num1 == " ":
        print("pienin luku:" + num1 + "ja suurin luku:" + num2)
        num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))
    while num1 <= num2:
        num2 = num1
        num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))
    while num1 >= num3:
        num3 = num1
        num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))
    while num2<=num1<=num3:
         num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))