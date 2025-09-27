import random
import bahan

print(bahan.judul)
print('\nSelamat datang di permainan ini! Berikut aturan yang harus kalian ikuti:')
print('1. Kamu harus menjawab 1 pertanyaan dengan benar untuk menyelamatkan Hangman\n2. Kamu memiliki 6 kesempatan')

user = input('Apakah kamu siap?(Y/n): ')

if user == 'Y':
    file_pertanyaan = open(r'pertanyaan','r')
    file_jawaban = open(r'jawaban','r')
    read_pertanyaan = file_pertanyaan.readlines()
    read_jawaban = file_jawaban.readlines()

    for nyawa in range(len(bahan.hangman)):
        print(bahan.hangman[nyawa])
        x = random.randint(0,19)
        pertanyaan = read_pertanyaan[x]
        jawaban = read_jawaban[x]
        user_jawab = input(f'{pertanyaan.strip()}: ')

        if user_jawab.lower().strip() == jawaban.lower().strip():
            print(bahan.congrats)
            print('\nSelamat kamu berhasil menyelamatkan Hangman!\n')
            break

        else:
            print(bahan.rose)
            print('\nKamu gagal menyelamatkan Hangman')

    file_pertanyaan.close()
    file_jawaban.close()

elif user == 'n':
    print('Baiklah, permainan dihentikan')
    
else:
    print('Input tidak valid!')