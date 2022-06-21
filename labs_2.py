Vvodimaya_stroka = input("Введите:")
if "C" in Vvodimaya_stroka or "c" in Vvodimaya_stroka or "с" in Vvodimaya_stroka or "С" in Vvodimaya_stroka:
    print("Буква С есть в строке на русском или на английском языке")
count = len(Vvodimaya_stroka)
schet = 0
dlina_novoy_stroki = 0
for izmeneniya in Vvodimaya_stroka:
    if len(Vvodimaya_stroka)>=3:
        schet = schet + 1
        if schet == 3:
            continue
        if schet == count:
            break
        dlina_novoy_stroki += 1
    print(izmeneniya,end="")
print("\n","Длина старой строки:",count)
print("\n","Длина новой строки:",dlina_novoy_stroki)
