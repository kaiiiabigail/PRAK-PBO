class Mahasiswa:
    def __init__(self, nim, nama, angkatan, is_mahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.is_mahasiswa = is_mahasiswa
        self.__ipk = 0.0

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, ipk):
        self.__ipk = ipk

    def display_info(self):
        return f"NIM: {self.get_nim()}, Nama: {self.get_nama()}, Angkatan: {self.angkatan}, " \
               f"Status Mahasiswa: {'Aktif' if self.is_mahasiswa else 'Nonaktif'}, IPK: {self.get_ipk()}"

    def hitung_panjang_nama(self):
        return len(self.__nama)

    def cek_status_lulus(self):
        if self.angkatan <= 2022:
            if self.get_ipk() >= 1.90:
                return "Mahasiswa sudah lulus"
            else:
                return "Mahasiswa belum lulus (IPK kurang dari 1.90)"
        else:
            return "Mahasiswa belum lulus"


mahasiswa1 = Mahasiswa(nim="1222140028", nama="Jarwo", angkatan=2022, is_mahasiswa=True)
mahasiswa2 = Mahasiswa(nim="122140000", nama="Joe Biden", angkatan=1980)


mahasiswa1.set_ipk(2.10)
mahasiswa2.set_ipk(1.80)


print(mahasiswa1.display_info())
print(mahasiswa1.cek_status_lulus())

print("\n")

print(mahasiswa2.display_info())
print(mahasiswa2.cek_status_lulus())
