class Coffee:
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga

class Cafe:
    def __init__(self):
        self.menu = [
            Coffee('Americano',15000),
            Coffee('Latte',18000),
            Coffee('Vanilla Latte',22000),
            Coffee('Hazelnut Latte',22000),
            Coffee('Caramel Latte',22000),
            Coffee('Caramel Macchiato',23000),
            Coffee('Kopi Susu',18000)
        ]
        self.pesanan = []

    def tampilkan_menu(self):
        print(f"{'Daftar Menu':^20}{'Medium':^8}{'Large':^8}\n{'-'*36}")
        for menu in self.menu:
            print(f"{menu.nama:<20}{menu.harga:^8}{menu.harga+3000:^8}")

    def lihat_pesanan(self):
        if not self.pesanan: print("Kamu belum memesan apapun"); return
        total_harga = 0; i = 1
        print(f"{'No':<3}{'Daftar Pesanan':<18}{'Ukuran':^7}{'Harga':^7}\n{'='*34}")
        for nama,ukuran,harga in self.pesanan:
            if ukuran == 'Large': simbol = '(L)'; harga += 3000
            else: simbol = '(M)'
            print(f"{i:<3}{nama:<18}{simbol:^7}{harga:^7}")
            total_harga += harga; i+=1
        print(f"{'-'*34}\n{'Total Harga: ':>29}{total_harga}")

    def tambah_pesanan(self):
        pesan = input("Mau pesan apa?(ex: americano): ").title().strip()
        for menu in self.menu:
            if menu.nama == pesan:
                ukuran = input("Ukurannya?(medium/large): ").capitalize().strip()
                if ukuran in ['Medium','Large']:
                    self.pesanan.append((menu.nama,ukuran,menu.harga))
                    print(f"{ukuran} {menu.nama} ditambahkan ke pesanan!"); return
        print('Menu atau ukuran tidak ditemukan!')

    def hapus_pesanan(self):
        if not self.pesanan: print("Kamu belum memesan apapun"); return
        self.lihat_pesanan()
        try:
            hapus = int(input('Pilih yang ingin dihapus (sesuai nomor): ').strip())
            print(f"Pesanan {self.pesanan[hapus-1][1]} {self.pesanan[hapus-1][0]} berhasil dihapus!")
            self.pesanan.pop(hapus-1)
        except:
            print('Pesanan tidak ditemukan!')

    def checkout(self):
        if not self.pesanan: print("Kamu belum memesan apapun"); return
        self.lihat_pesanan()
        print("Pastikan pesananmu sesuai sebelum checkout!")
        confirm = input("Checkout sekarang?(y/n): ").lower().strip()
        if confirm == 'y':
            self.pesanan.clear()
            print("Terimakasih Selamat Menikmati ^^")

cafe = Cafe()
while True:
    print('\n========= GanZ Coffee =========')
    print('1. Lihat Menu\n2. Lihat Pesanan\n3. Tambah Pesanan\n4. Hapus Pesanan\n5. Checkout\n6. Exit')
    pilih = input('Pilihanmu: ')
    if pilih == '1': cafe.tampilkan_menu()
    elif pilih == '2': cafe.lihat_pesanan()
    elif pilih == '3': cafe.tambah_pesanan()
    elif pilih == '4': cafe.hapus_pesanan()
    elif pilih == '5': cafe.checkout()
    elif pilih == '6': print('Program berakhir');break
    else: print('Input tidak valid!')