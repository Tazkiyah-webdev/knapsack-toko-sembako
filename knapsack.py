# Data Toko Sembako & Rempah (Barang yang harus ditimbang)
# Format: (Nama Barang, Berat/Kg, Keuntungan/Ribu)
data_toko = [
    ("Beras Kepala", 10, 25), 
    ("Gula Pasir", 5, 12), 
    ("Minyak Goreng Curah", 3, 8), 
    ("Tepung Terigu", 2, 5),
    ("Kacang Tanah", 4, 15), 
    ("Kemiri Utuh", 1, 10),
    ("Bawang Merah", 2, 9), 
    ("Bawang Putih", 2, 7),
    ("Cabai Rawit", 1, 11), 
    ("Telur Ayam", 3, 6)
]

kapasitas_maksimal = 15
max_profit = 0
item_terpilih = []

def solve_knapsack_backtracking(idx, berat_skrg, profit_skrg, dipilih):
    global max_profit, item_terpilih
    
    # Basis: Jika semua item sudah diproses
    if idx == len(data_toko):
        if profit_skrg > max_profit:
            max_profit = profit_skrg
            item_terpilih = list(dipilih)
        return

    nama, berat, profit = data_toko[idx]

    # Cabang INCLUDE: Barang ditimbang & dimasukkan
    # [cite_start]PRUNING: Cek apakah berat melebihi kapasitas M [cite: 587]
    if berat_skrg + berat <= kapasitas_maksimal:
        dipilih.append(data_toko[idx])
        solve_knapsack_backtracking(idx + 1, berat_skrg + berat, profit_skrg + profit, dipilih)
        dipilih.pop() # Backtrack

    # Cabang EXCLUDE: Barang dilewati
    solve_knapsack_backtracking(idx + 1, berat_skrg, profit_skrg, dipilih)

# Menjalankan algoritma
solve_knapsack_backtracking(0, 0, 0, [])

# --- OUTPUT RAPI ---
print("="*50)
print("   HASIL IMPLEMENTASI 0/1 KNAPSACK BACKTRACKING   ")
print("           TOKO SEMBAKO & REMPAH              ")
print("="*50)
print(f"Kapasitas Maksimal Gudang : {kapasitas_maksimal} kg")
print("-" * 50)
print(f"Keuntungan Maksimum (Profit): Rp {max_profit} Ribu")

total_berat = sum(item[1] for item in item_terpilih)
print(f"Total Berat Timbangan       : {total_berat} kg")
print("-" * 50)

print("Barang yang dipilih:")
for i, item in enumerate(item_terpilih, 1):
    print(f"{i}. {item[0]:<20} (Berat: {item[1]}kg, Profit: {item[2]}rb)")
print("="*50)
