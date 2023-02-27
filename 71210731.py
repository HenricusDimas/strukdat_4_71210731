import json
inp = int(input("Masukkan jumlah barang :"))
daftar = []
for i in range(inp):
    nama = input("masukkan nama barang : ")
    harga = int(input("masukkan harga barang :"))
    daftar.append({"nama": nama, "harga": harga})


total = sum([barang["harga"] for barang in daftar])
data = {"total": total, "barang": daftar} 
with open("71210731.json", "w") as outfile:
    json.dump(data,outfile)
    
with open('71210731.json', 'r') as openfile:
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))
