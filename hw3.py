char1 = {"ad": "galictia", "gücü": 500, "silah": "sword", "can": 500}

char2 = {"ad": "melania", "gücü": 400, "silah": "bow", "can2": 600}

def attack (vurdu: char1, vuruldu: char2):
    azalan = vurdu["gücü"]
    vuruldu["can"] = vuruldu["can"] - azalan

def attack2 (vuruldu: char1, vurdu: char2):
    azalan = vurdu["gücü"]
    vuruldu["can"] = vuruldu["can"] - azalan

name = str(input("İsminizi Giriniz: "))
print(f"Hoş geldin: ", name,"Oyun başlıyor!")

print("1.Karakterin Adı: {}".format(char1["ad"]))
print("1.Karakterin Gücü: {}".format(char1["gücü"]))
print("2.Karakterin Adı: {}".format(char2["ad"]))
print("2.Karakterin Gücü: {}".format(char2["gücü"]))

attack(char2,char1)
attack2(char1, char2)

print("Dövüştüler!")
print("1.Karakterin Canı:", char1["can"])
print("2.Karakterin Canı: ", char2["can2"])
quit