roma = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}
sayi = input("1 ile 5000 arasında bir romen rakamını büyük harf kullanarak giriniz = ")

for key,value in roma.items():
    if sayi == key:
        print(f"{sayi} = {value}")

