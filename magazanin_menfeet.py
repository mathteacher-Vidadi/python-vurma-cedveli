mehsul = input("Məhsulun adını yazın: ")
alis = float(input("Alış qiymətini yazın: "))
satis = float(input("Satış qiymətini yazın: "))
say = int(input("Neçə ədəd satılıb: "))
print("Məhsul:", mehsul)
print("Alış qiyməti:", alis)
print("Satış qiyməti:", satis)
menfeet = (satis - alis) * say
print("Mənfəət:", menfeet, "manat")
if menfeet > 0:
  print("Mağaza mənfəət edib.")
else:
  print("Mağaza zərər edib.")  




















































