from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Buku(BaseModel):
    judul: str
    penulis: str
    harga: int
    tersedia: Optional[bool] = True

db_buku = [
    {"id": 1, "judul": "bljr py", "penulis": "sarah", "harga": 19000}, 
    {"id": 2, "judul": "anjay", "penulis": "irisa", "harga": 21000}, 
] 

@app.get("/buku")
def ambil_buku():
    return db_buku

@app.post("/buku")
def tambah_buku(buku_baru: Buku):
    id_baru = len(db_buku) + 1

    data = buku_baru.dict()
    data["id"] = id_baru

    db_buku.append(data)

    return {"message": "Buku berhasil ditambah!", "data": data}

"""
PENJELASAN: 
from fastapi (package) import FastAPI (kelas/modul) - kelas FastAPI berisi struktur dan fungsi-fungsi dari fastapi 
app = FastAPI() - panggil fungsi fastapi supaya aplikasi bisa berjalan
class ..(BaseModel) - skema struktur data dengan validasi data menggunakan BaseModel dan Optional untuk data optional 
db_buku = list berisi database objek buku
@app.get = endpoint get untuk mengambil data dari server 
@app.post = client menambah data dan disimpan ke server 
def tambah_buku(buku_baru: Buku): = fungsi bernama tambah_buku dengan parameter buku_baru: dan scheme Buku
id_baru = len(db_buku) + 1 = menghitung id baru setiap ada data baru 
data = buku_baru.dict() = isi dari parameter buku_baru diubah jadi dict dan disimpan di variabel sementara bernama data
data["id"] = id_baru = di variabel data, ditambahkan key "id" berisi value dari variabel id_baru
db_buku.append() = menambahkan objek baru ke db_buku dengan memanggil variabel data 
return = return hasil dengan string dan variabel sementara data


STRUKTUR 
1. client request dengan methode post
2. fastapi validasi dengan BaseModel
3. jika validasi berhasil, buat objek baru dan simpan di parameter buku_baru
4. hitung id_baru 
5. ubah objek dalam parameter buku_baru menjadi dictionary, dan simpan di variabel sementara bernama data
6. tambahkan key "id" dengan value dari var id_baru ke variabel data
7. masukkan variabel data ke db_buku 
8. return response ke client menggunakan uvicorn 

"""

