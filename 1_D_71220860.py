susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

Duit = int(input('Masukkan jumlah uang: RP'))
start = input('ketik START untuk memulai: ')
if start.lower() == 'start':
    while True:
        membeli = input('Apa barang yang akan Anda membeli? ')
        if membeli.lower() =='susu':
            if Duit >= susu:
                Duit -= susu
                print('Sisa uang Anda',Duit)
            else:
                print('Uang tidak cukup')
        elif membeli.lower() =='permen':
            if Duit >= permen:
                Duit -= permen
                print('Sisa uang Anda',Duit)
            else:
                print('Uang anda tidak cukup')
        elif membeli.lower() =='roti':
            if Duit >= roti:
                Duit -= roti
                print('Sisa uang Anda',Duit)
            else:
                print('Uang anda tidak cukup')
        elif membeli.lower() =='indomie':
            if Duit >= indomie:
                Duit -= indomie
                print('Sisa uang Anda',Duit)
            else:
                print('Uang anda tidak cukup')
        elif membeli.lower() =='vitamin':
            if Duit >= vitamin:
                Duit -= vitamin
                print('Sisa uang Anda',Duit)
            else:
                print('Uang anda tidak cukup')
        elif membeli.lower() == 'sudah':
            break
        else :
            print('Barang tidak tersedia')