bawah= int(input("Inputkan Batas Bawah Yang Anda Inginkan : "))
atas = int(input("Inputkan Batas Atas Yang Anda Ingnkan : "))

if bawah < 0 or atas < 0 :
    print("Maaf, batas bawah dan atas yang dimasukan tidak boleh di bawah nol")
else :
    sum = 0
    for x in range (bawah, atas) :
        if x % 2 == 1 :
            print(x)
            sum += x
    print("Total : ", sum)
