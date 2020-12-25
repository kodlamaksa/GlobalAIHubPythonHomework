mylist = []

name = str(input("Lutfen Adinizi giriniz: "))
lastname = str(input("Lutfen Soyadinizi giriniz: "))
age = int(input("Lutfen Yaşinizi giriniz: "))
dateofbirth = int(input("Lütfen dogum yilinizi yaziniz: "))

mylist.append(name)
mylist.append(lastname)
mylist.append(age)
mylist.append(dateofbirth)

for i in mylist:
    print(i)

print(mylist)

if (age < 18):
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")