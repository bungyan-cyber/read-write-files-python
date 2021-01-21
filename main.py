import json

nama = str(input("masukan nama anda : \n"))
print(f'Hi, {nama}')

cetak = f'Hi, {nama} apakabar'
with open('dupsElast.txt', 'w') as f :
    json.dump(cetak, f, indent = 2)

