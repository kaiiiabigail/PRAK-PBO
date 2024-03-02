jarijari = int(input("Inputkan jari-jari : "))
phi = 3.14

if jarijari < 0 :
    print("Maaf, jari-jari lingkaran tidak boleh negatif")
else :
    luas = phi * jarijari ** 2
    keliling = 2 * phi * jarijari

    print("Luas lingkaran adalah : ", luas)
    print("Keliling lingkaran adalah : ", keliling)
