nama_hero = "Phainon"
darah = 100
mana = 100

print("nama hero:")
print(nama_hero)
print("darah hero awal:")
print(darah)
print("mana hero awal:")
print(mana)

# hero diserang nanook! darahnya berkurang 20
darah = darah - 20

print("darah hero setelah di serang:")
print(darah)

# hero minum potion! darahnya bertambah 50
darah = darah + 20

print("darah setelah minum potion:")
print(darah)

# mana hero berkurang saat menggunakan skil! mana berkurang 20
mana = mana - 20

print("mana setelah menggunakan skill:")
print(mana)

darah = darah - 100
if darah > 0:
    print ("Phainon masih bertahan hidup!")
else:
    print("phainon telah gugur. . .")
    
 # Atur biaya mana untuk skill!
biaya_mana = 50
if mana >= biaya_mana:
     mana = mana - biaya_mana
     print("skill berhasil digunakan!")
     print("sisa mana sekarang:")
     print(mana)
else:
    print("mana tidak cukup untuk menggunakan skill!")
    
    # Status Awal
level = 1
exp = 0
exp_upgrade = 100  # Butuh 100 EXP untuk naik level

# Tentukan monster yang dilawan: "besar" atau "kecil"
tipe_monster = "besar"

print("Melawan monster:", tipe_monster)

# Logika Tambahan EXP
if tipe_monster == "besar":
    exp = exp + 40  # Monster besar kasih EXP banyak (cepat upgrade)
    print("Mendapatkan 40 EXP!")
else:
    exp = exp + 10  # Monster kecil kasih EXP sedikit (lambat upgrade)
    print("Mendapatkan 10 EXP!")

# Cek apakah EXP sudah cukup untuk Upgrade/Naik Level
if exp >= exp_upgrade:
    level = level + 1
    exp = exp - exp_upgrade  # Sisa EXP disimpan
    print("SELAMAT! Phainon naik ke Level:", level)
else:
    print("EXP sekarang:", exp, "/", exp_upgrade)
    
mana = 100

# Status Ultimate Form
is_ultimate = False

print("\n--- MENCOBA MENGGUKAN ULTIMATE FORM ---")

# Cek apakah Mana cukup (butuh 70 mana)
if mana >= 70:
    mana = mana - 70
    is_ultimate = True
    print("PHAINON MEMASUKI ULTIMATE FORM!")
    print("Sisa mana sekarang:", mana)
else:
    print("mana tidak cukup untuk ultimate! Butuh 70 mana.")
    print("Mana kamu saat ini:", mana)
    
# Tentukan Damage berdasarkan status Ultimate Form
if is_ultimate == True:
    damage_phainon = 1000000
    print("CRITICAL HIT! ULTIMATE ATTACK ENEMY!")
else:
    damage_phanon = 500
    print("Menyerang dengan serangan biasa.")
    
print("Damage yang dihasilkan Phainon:", damage_phainon)

import random

print("\n--- SISTEM GACHA SENJATA PHAINON ---")

# Python memilih angka acak dari 1 sampai 100
persen = random.randint(1, 100)

if persen <= 5:
    senjata = "Pedang 'The Burns The Dawn'"
    rarity = "LEGEND"
elif persen <= 20:
    senjata = "Katana"
    rarity = "EPIC"
elif persen <= 50:
    senjata = "Dagger"
    rarity = "RARE"
else:
    senjata = "Pisau Dapur"
    rarity = "COMMON"

print("Hasil Gacha:", senjata)
print("Kelangkaan:", rarity)
