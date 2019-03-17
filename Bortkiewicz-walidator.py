print("Walidator numeru pesel")
print("")
pes = input("Podaj swoj pesel: ")



if(len(pes) == 11):
    age = pes[0] + pes[1]
    month = pes[2] + pes[3]
    if int(month) > 12 or int(month) < 0:
        print("Pesel niepoprawny - miesiac")
        exit()
    day = pes[4] + pes[5]
    if int(day) > 31 or int(day) < 0:
        print("Pesel niepoprawny - dzien")
        exit()
    print("Data urodzenia: ",age,"/",month,"/",day)
    sex = pes[6] + pes[7] + pes[8] + pes[9]
    if int(sex) % 2 == 0:
        print("Plec: kobieta")
    else:
        print("Plec: mezczyzna")
    sum = int(pes[0])+ int(pes[4]) + int(pes[8])
    sum = sum + int(pes[1])*3+ int(pes[5])*3 + int(pes[9])*3
    sum = sum + int(pes[2])*7+ int(pes[6])*7
    sum = sum + int(pes[3])*9+ int(pes[7])*9
    sum = sum % 10
    sum = 10 - sum
    if int(pes[10]) == int(sum):
        print("Pesel poprawny")
    else:
        print("Pesel niepoprawny - suma kontrolna", sum)


else:
    print("Pesel != 11")