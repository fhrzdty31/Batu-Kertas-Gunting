import random

bot = ['batu', 'kertas', 'gunting']

print("\n\n== Batu Kertas Gunting ==\n\n* 99 untuk berhenti\n\n")
while True:
    x = random.choice(bot)
    user = input('Masukkan pilihan : ')

    # Seri
    if user.lower() == x:
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Hasil Seri #\n\n")
    
    # Menang
    elif user.lower() == 'batu' and x == 'gunting':
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Kamu Menang #\n\n")
    elif user.lower() == 'kertas' and x == 'batu':
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Kamu Menang #\n\n")
    elif user.lower() == 'gunting' and x == 'kertas':
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Kamu Menang #\n\n")

    # Kalah
    elif user.lower() == 'batu' and x == 'kertas':
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Kamu Kalah #\n\n")
    elif user.lower() == 'kertas' and x == 'gunting':
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Kamu Kalah #\n\n")
    elif user.lower() == 'gunting' and x == 'batu':
        print(f'\nKamu\t: {user.capitalize()}')
        print(f'Bot\t: {x.capitalize()}')
        print("\n# Kamu Kalah #\n\n")
    
    # Berhenti
    elif user == '99':
        print("\n== Terimakasih Telah Bermain ==\n\n")
        break

    # Eror
    else:
        print("\n# Data Salah !! #\n\n")
    