# Çözümün
bakiye = int(input("bakiye: "))
girdi = input("komut: ")
while girdi != "BITIR":    
    girdi = girdi.split(" ")
    if girdi[0] == "YATIR":
        bakiye += int(girdi[1])
    elif girdi[0] == "CEK":
        if bakiye < int(girdi[1]):
            print("Yetersiz bakiye.")
        elif int(girdi[1]) > 5000:
            print("Limit aşıldı.")
        else:
            bakiye -= int(girdi[1])
    elif girdi[0] == "FAIZ":
        bakiye += bakiye * int(girdi[1])/100
    else:
        print("Geçersiz komut.")
    girdi = input("komut: ")
print("bakiye: ", bakiye)
