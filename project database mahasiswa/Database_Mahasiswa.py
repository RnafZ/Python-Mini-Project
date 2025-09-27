class database_mahasiswa:
    def __init__(self,file1,file2):
        self.file1 = file1
        self.file2 = file2
    
    def tambah_mahasiswa(self,nama,nim):
        with open(self.file2,'r') as file_nim:
            list_nim = [i.strip() for i in file_nim.readlines()]
        if nim in list_nim:
            print(f'Mahasiswa dengan NIM {nim} sudah tersedia')
        else:
            with open(self.file1,'a') as file_nama, open(self.file2,'a') as file_nim:
                file_nama.write(f'\n{nama}')
                file_nim.write(f'\n{nim}')
            print(f'Mahasiswa bernama {nama} dengan NIM {nim} berhasil ditambahkan!')

    def list_mahasiswa(self):
        with open(self.file1,'r') as file_nama, open(self.file2,'r') as file_nim:
            list_nama = file_nama.readlines()
            list_nim = file_nim.readlines()
        if len(list_nama) == 0:
            print('Tidak ada data dalam file')
        else:
            print('List Mahasiswa:\n')
            print(f"{'No.':<5}{'Nama':<20}{'NIM':<15}")
            print('=' * 40)
            for i in range(len(list_nama)):
                print(f"{f'{i+1}.':<5}{list_nama[i].strip():<20}{list_nim[i].strip():<15}")
    
    def hapus_mahasiswa(self,nim):
        with open(self.file2,'r') as file_nim, open(self.file1,'r') as file_nama:
            list_nama = file_nama.readlines()
            list_nim = file_nim.readlines()
        index_hapus = None
        for i,x in enumerate(list_nim):
            if x.strip() == nim:
                index_hapus = i
                break
        if index_hapus is not None:
            telah_dihapus = f'Mahasiswa bernama {list_nama[index_hapus].strip()} dengan NIM {nim} berhasil dihapus'
            del list_nama[index_hapus]
            del list_nim[index_hapus]
            with open(self.file2,'w') as file_nim, open(self.file1,'w') as file_nama:
                file_nama.writelines(list_nama)
                file_nim.writelines(list_nim)
            print(telah_dihapus)
        else:
            print(f'Mahasiswa dengan NIM {nim} tidak ditemukan!')

    def cari_mahasiswa(self,nim):
        with open(self.file2,'r') as file_nim, open(self.file1,'r') as file_nama:
            list_nama = file_nama.readlines()
            list_nim = file_nim.readlines()
        index_cari = None
        for i,x in enumerate(list_nim):
            if x.strip() == nim:
                index_cari = i
                break
        if index_cari == None:
            print(f'Mahasiswa dengan NIM {nim} tidak ditemukan')
        else:
            print(f'Mahasiswa ditemukan!\nNama:{list_nama[i]}NIM: {x.strip()}')

db = database_mahasiswa(r'project database mahasiswa\Nama',r'project database mahasiswa\Nim')
