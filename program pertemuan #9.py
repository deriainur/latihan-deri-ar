def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    
    data_mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })
    
    tambah_data = input("\nTambah data lagi? (y/t): ").lower()
    if tambah_data == 't':
        break

print("\nDaftar Nilai Mahasiswa:")
print(f"{'No':<5}{'Nama':<15}{'NIM':<15}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Nilai Akhir':<10}")
print("=" * 70)
for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i:<5}{mahasiswa['Nama']:<15}{mahasiswa['NIM']:<15}{mahasiswa['Tugas']:<10}{mahasiswa['UTS']:<10}{mahasiswa['UAS']:<10}{mahasiswa['Nilai Akhir']:<10.2f}")
