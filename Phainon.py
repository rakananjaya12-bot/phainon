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

# hero minum potion! darahnya bertambah 20
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
    damage_phainon = 500
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

# 1. Buat inventory kosong di bagian atas (dekat variable darah/mana)
inventory = []

# 2. setelah dapat hasil gacha, masukkan senjatanya ke inventory
inventory.append(senjata)

# 3. Tampilkan isi inventory pemain di akhir game
print("\n--- ISI INVENTORY kamu ---")
for item in inventory:
    print("- " + item)
    
    import random

# --- 1. SETTING MATA UANG & HARGA SELL ---
GOA = 1000  # Modal awal pemain (bisa kamu atur sesuai keinginan)
HARGA_JUAL = {
    "LEGEND": 70,
    "EPIC": 50,
    "RARE": 30,
    "COMMON": 10
}

inventory = []

# --- 2. LOGIKA MEMBUNUH MONSTER (KUMPUL GOA & LOOT) ---
print("--- PHAINON BERTARUNG ---")
# Anggap Phainon menang lawan monster
GOA += 20  # Pemain dapat 20 GOA secara langsung
print(f"Monster berhasil dikalahkan! Kamu mendapatkan 20 GOA.")
print(f"Sisa GOA saat ini: {GOA}")

# Monster dropping loot berdasarkan kelangkaan
kelangkaan_loot = ["COMMON", "RARE", "EPIC", "LEGEND"]
loot_dapat = random.choice(kelangkaan_loot)
inventory.append(loot_dapat)
print(f"Monster menjatuhkan barang bertipe: [{loot_dapat}]")


# --- 3. LOGIKA MENJUAL BARANG DARI INVENTORY ---
print("\n--- MENJUAL BARANG ---")
if loot_dapat in HARGA_JUAL:
    hasil_jual = HARGA_JUAL[loot_dapat]
    GOA += hasil_jual
    inventory.remove(loot_dapat)
    print(f"Kamu menjual barang [{loot_dapat}] seharga {hasil_jual} GOA!")
    print(f"GOA kamu sekarang: {GOA}")


# --- 4. LOGIKA GACHA (BUTUH 120 GOA) ---
HARGA_GACHA = 120

print("\n--- SISTEM GACHA ---")
if GOA >= HARGA_GACHA:
    GOA -= HARGA_GACHA  # Bayar 120 GOA
    
    # List Senjata Gacha
    list_senjata = ["Katana", "Sword of Light", "Bow of Artemis", "Wooden Stick"]
    senjata_dapat = random.choice(list_senjata)
    inventory.append(senjata_dapat)
    
    print(f"Gacha Berhasil! Kamu membayar 120 GOA.")
    print(f"Kamu mendapatkan: {senjata_dapat}!")
    print(f"Sisa GOA kamu: {GOA}")
else:
    print(f"GOA tidak cukup! Kamu butuh {HARGA_GACHA} GOA untuk gacha (GOA kamu: {GOA}).")
    
    import random

# --- STATUS AWAL PEMAIN ---
nama_hero = "Phainon"
hp = 100
goa = 1000
inventory = []

# --- LOOP GAME UTAMA ---
while True:
    print("\n" + "="*30)
    print(f"--- MENU UTAMA RPG {nama_hero.upper()} ---")
    print(f"HP: {hp} | GOA: {goa}")
    print("="*30)
    print("1. Bertarung lawan Monster")
    print("2. Jual Loot di Inventory")
    print("3. Main Gacha Senjata (120 GOA)")
    print("4. Cek Tas / Inventory")
    print("5. Keluar Game")
    
    pilihan = input("\nPilih aksi kamu (1-5): ")

    if pilihan == "1":
        print("\n⚔️ PHAINON BERTARUNG!")
        goa += 20
        print("Monster kalah! Kamu mendapatkan +20 GOA.")
        
    elif pilihan == "2":
        print("\n💰 MENJUAL BARANG...")
        if len(inventory) > 0:
            barang = inventory.pop() # Mengambil 1 barang dari tas
            goa += 50
            print(f"Kamu menjual {barang} seharga 50 GOA!")
        else:
            print("Tas kamu kosong! Tidak ada barang untuk dijual.")

    elif pilihan == "3":
        print("\n🎰 SISTEM GACHA SENJATA")
        if goa >= 120:
            goa -= 120
            hadiah = random.choice(["Katana", "Dagger", "Greatsword"])
            inventory.append(hadiah)
            print(f"Selamat! Kamu dapat: {hadiah}")
        else:
            print("GOA tidak cukup! Butuh 120 GOA.")

    elif pilihan == "4":
        print("\n🎒 ISI INVENTORY KAMU:")
        if len(inventory) == 0:
            print("- (Tas Kosong)")
        else:
            for item in inventory:
                print(f"- {item}")

    elif pilihan == "5":
        print("\nTerima kasih sudah bermain Game Phainon! Sampai jumpa 👋")
        break # Menghentikan game / keluar dari loop

    else:
        print("\nPilihan tidak valid! Masukkan angka 1 sampai 5.")
        
        import random

# --- STATUS AWAL HERO & MATA UANG ---
nama_hero = "Phainon"
hp_maksimal = 100
hp_sekarang = 100
goa = 1000  # Currency Gold Of Amphorious

# --- DATABASE HARGA & ITEM ---
HARGA_JUAL_LOOT = {
    "LEGEND": 70,
    "EPIC": 50,
    "RARE": 30,
    "COMMON": 10
}

SHOP_ARMOR = {
    "1": ("Training Armor", 500),
    "2": ("Gold Armor", 500),
    "3": ("Iron Armor", 1000),
    "4": ("Diamond Armor", 3000),
    "5": ("Tank Armor", 5000)
}

inventory = []

# --- LOOP GAME UTAMA ---
while True:
    print("\n" + "="*35)
    print(f"--- MENU UTAMA RPG {nama_hero.upper()} ---")
    print(f"HP: {hp_sekarang}/{hp_maksimal} | GOA: {goa}")
    print("="*35)
    print("1. Bertarung lawan Monster (+20 GOA & Loot)")
    print("2. Jual Loot di Inventory")
    print("3. Main Gacha Senjata (120 GOA)")
    print("4. Buka Toko / Shop (Armor & Potion)")
    print("5. Pakai Potion / Heal")
    print("6. Cek Tas / Inventory")
    print("7. Keluar Game")
    
    pilihan = input("\nPilih aksi kamu (1-7): ")

    # 1. BERTARUNG
    if pilihan == "1":
        print("\n⚔️ PHAINON BERTARUNG!")
        goa += 20
        
        # Monster dropping loot
        kelangkaan = ["COMMON", "RARE", "EPIC", "LEGEND"]
        loot_dapat = random.choice(kelangkaan)
        inventory.append(f"Loot [{loot_dapat}]")
        
        print("Monster kalah! Kamu mendapatkan +20 GOA.")
        print(f"Monster menjatuhkan: Loot [{loot_dapat}]")

    # 2. JUAL LOOT
    elif pilihan == "2":
        print("\n💰 MENJUAL LOOT...")
        # Cari loot yang bisa dijual di inventory
        loot_ditemukan = False
        for item in inventory:
            for raritas, harga in HARGA_JUAL_LOOT.items():
                if raritas in item:
                    inventory.remove(item)
                    goa += harga
                    print(f"Berhasil menjual {item} seharga {harga} GOA!")
                    loot_ditemukan = True
                    break
            if loot_ditemukan:
                break
        
        if not loot_ditemukan:
            print("Tidak ada Loot di tas yang bisa dijual!")

    # 3. GACHA SENJATA
    elif pilihan == "3":
        print("\n🎰 GACHA SENJATA PHAINON")
        if goa >= 120:
            goa -= 120
            list_senjata = ["Katana", "Pisau Dapur", "Dagger", "Greatsword", "Bow of Artemis"]
            hadiah = random.choice(list_senjata)
            inventory.append(hadiah)
            print(f"Gacha Berhasil (-120 GOA)! Kamu mendapatkan: {hadiah}")
        else:
            print(f"GOA tidak cukup! Kamu butuh 120 GOA (GOA kamu: {goa}).")

    # 4. TOKO / SHOP
    elif pilihan == "4":
        print("\n" + "="*30)
        print("🏪 TOKO / SHOP AMPHORIOUS")
        print("="*30)
        print("1. Beli Armor")
        print("2. Beli Potion")
        sub_shop = input("Pilih kategori (1-2): ")

        # SHOP ARMOR
        if sub_shop == "1":
            print("\n--- DAFTAR ARMOR ---")
            for k, (nama_armor, harga) in SHOP_ARMOR.items():
                print(f"{k}. {nama_armor} ({harga} GOA)")
            
            pilih_armor = input("Pilih Armor yang ingin dibeli (1-5): ")
            if pilih_armor in SHOP_ARMOR:
                nama_a, harga_a = SHOP_ARMOR[pilih_armor]
                if goa >= harga_a:
                    goa -= harga_a
                    inventory.append(nama_a)
                    print(f"🎉 Berhasil membeli {nama_a} seharga {harga_a} GOA!")
                else:
                    print("GOA kamu tidak cukup!")
            else:
                print("Pilihan Armor tidak ada!")

        # SHOP POTION
        elif sub_shop == "2":
            print("\n--- DAFTAR POTION ---")
            print("1. Potion Biasa (+20% HP) - 100 GOA")
            print("2. Heal Deras (+100% HP) - 300 GOA")
            pilih_pot = input("Pilih Potion (1-2): ")
            
            if pilih_pot == "1":
                if goa >= 100:
                    goa -= 100
                    inventory.append("Potion Biasa")
                    print("🎉 Berhasil membeli Potion Biasa!")
                else:
                    print("GOA kamu tidak cukup!")
            elif pilih_pot == "2":
                if goa >= 300:
                    goa -= 300
                    inventory.append("Heal Deras")
                    print("🎉 Berhasil membeli Heal Deras!")
                else:
                    print("GOA kamu tidak cukup!")

    # 5. PAKAI POTION
    elif pilihan == "5":
        print("\n🧪 MENGGUNAKAN POTION...")
        if "Heal Deras" in inventory:
            inventory.remove("Heal Deras")
            hp_sekarang = hp_maksimal
            print("Kamu menggunakan Heal Deras! HP kamu kembali PENUH (100%)!")
        elif "Potion Biasa" in inventory:
            inventory.remove("Potion Biasa")
            pemulihan = int(hp_maksimal * 0.20)
            hp_sekarang = min(hp_maksimal, hp_sekarang + pemulihan)
            print(f"Kamu menggunakan Potion Biasa! HP bertambah {pemulihan}.")
        else:
            print("Kamu tidak punya Potion di inventory!")

    # 6. INVENTORY
    elif pilihan == "6":
        print("\n🎒 ISI INVENTORY KAMU:")
        if len(inventory) == 0:
            print("- (Tas Kosong)")
        else:
            for item in inventory:
                print(f"- {item}")

    # 7. KELUAR GAME
    elif pilihan == "7":
        print("\nTerima kasih sudah bermain Game Phainon! Sampai jumpa 👋")
        break

    else:
        print("\nPilihan tidak valid! Masukkan angka 1 sampai 7.")
        
        import random

# --- STATUS AWAL HERO & MATA UANG ---
nama_hero = "Phainon"
hp_dasar = 100         # HP bawaan hero tanpa armor
bonus_hp_armor = 0    # Bonus HP dari armor yang dipake
hp_sekarang = 100
goa = 1000            # Currency Gold Of Amphorious
armor_terpakai = "Tidak Ada"

# --- DATABASE HARGA, BONUS ARMOR & ITEM ---
HARGA_JUAL_LOOT = {
    "LEGEND": 70,
    "EPIC": 50,
    "RARE": 30,
    "COMMON": 10
}

# (Nama Armor: [Harga, Bonus HP])
SHOP_ARMOR = {
    "1": ("Training Armor", 500, 50),
    "2": ("Gold Armor", 500, 50),
    "3": ("Iron Armor", 1000, 100),
    "4": ("Diamond Armor", 3000, 300),
    "5": ("Tank Armor", 5000, 500)
}

inventory = []

# --- LOOP GAME UTAMA ---
while True:
    # Hitung total HP maksimal (HP Dasar + Bonus Armor)
    hp_maksimal = hp_dasar + bonus_hp_armor
    
    print("\n" + "="*40)
    print(f"--- MENU UTAMA RPG {nama_hero.upper()} ---")
    print(f"HP: {hp_sekarang}/{hp_maksimal} | GOA: {goa}")
    print(f"Armor Terpakai: {armor_terpakai} (+{bonus_hp_armor} HP)")
    print("="*40)
    print("1. Bertarung lawan Monster (+20 GOA & Loot)")
    print("2. Jual Loot di Inventory")
    print("3. Main Gacha Senjata (120 GOA)")
    print("4. Buka Toko / Shop (Armor & Potion)")
    print("5. Pakai / Equip Armor")
    print("6. Pakai Potion / Heal")
    print("7. Cek Tas / Inventory")
    print("8. Keluar Game")
    
    pilihan = input("\nPilih aksi kamu (1-8): ")

    # 1. BERTARUNG
    if pilihan == "1":
        print("\n⚔️ PHAINON BERTARUNG!")
        goa += 20
        
        # Simulasi kena serang sedikit saat bertarung
        kerusakan = random.randint(10, 25)
        hp_sekarang = max(0, hp_sekarang - kerusakan)
        
        kelangkaan = ["COMMON", "RARE", "EPIC", "LEGEND"]
        loot_dapat = random.choice(kelangkaan)
        inventory.append(f"Loot [{loot_dapat}]")
        
        print(f"Monster kalah! Phainon terkena {kerusakan} damage.")
        print(f"Kamu mendapatkan +20 GOA & Loot [{loot_dapat}].")

    # 2. JUAL LOOT
    elif pilihan == "2":
        print("\n💰 MENJUAL LOOT...")
        loot_ditemukan = False
        for item in inventory:
            for raritas, harga in HARGA_JUAL_LOOT.items():
                if raritas in item:
                    inventory.remove(item)
                    goa += harga
                    print(f"Berhasil menjual {item} seharga {harga} GOA!")
                    loot_ditemukan = True
                    break
            if loot_ditemukan:
                break
        
        if not loot_ditemukan:
            print("Tidak ada Loot di tas yang bisa dijual!")

    # 3. GACHA SENJATA
    elif pilihan == "3":
        print("\n🎰 GACHA SENJATA PHAINON")
        if goa >= 120:
            goa -= 120
            list_senjata = ["Katana", "Pisau Dapur", "Dagger", "Greatsword", "Bow of Artemis"]
            hadiah = random.choice(list_senjata)
            inventory.append(hadiah)
            print(f"Gacha Berhasil (-120 GOA)! Kamu mendapatkan: {hadiah}")
        else:
            print(f"GOA tidak cukup! Kamu butuh 120 GOA (GOA kamu: {goa}).")

    # 4. TOKO / SHOP
    elif pilihan == "4":
        print("\n" + "="*30)
        print("🏪 TOKO / SHOP AMPHORIOUS")
        print("="*30)
        print("1. Beli Armor")
        print("2. Beli Potion")
        sub_shop = input("Pilih kategori (1-2): ")

        # SHOP ARMOR
        if sub_shop == "1":
            print("\n--- DAFTAR ARMOR ---")
            for k, (nama_a, harga_a, bonus_a) in SHOP_ARMOR.items():
                print(f"{k}. {nama_a} ({harga_a} GOA) [+{bonus_a} HP]")
            
            pilih_armor = input("Pilih Armor yang ingin dibeli (1-5): ")
            if pilih_armor in SHOP_ARMOR:
                nama_a, harga_a, bonus_a = SHOP_ARMOR[pilih_armor]
                if goa >= harga_a:
                    goa -= harga_a
                    inventory.append(nama_a)
                    print(f"🎉 Berhasil membeli {nama_a} seharga {harga_a} GOA!")
                else:
                    print("GOA kamu tidak cukup!")
            else:
                print("Pilihan Armor tidak ada!")

        # SHOP POTION
        elif sub_shop == "2":
            print("\n--- DAFTAR POTION ---")
            print("1. Potion Biasa (+20% HP) - 100 GOA")
            print("2. Heal Deras (+100% HP) - 300 GOA")
            pilih_pot = input("Pilih Potion (1-2): ")
            
            if pilih_pot == "1":
                if goa >= 100:
                    goa -= 100
                    inventory.append("Potion Biasa")
                    print("🎉 Berhasil membeli Potion Biasa!")
                else:
                    print("GOA kamu tidak cukup!")
            elif pilih_pot == "2":
                if goa >= 300:
                    goa -= 300
                    inventory.append("Heal Deras")
                    print("🎉 Berhasil membeli Heal Deras!")
                else:
                    print("GOA kamu tidak cukup!")

    # 5. EQUIP ARMOR
    elif pilihan == "5":
        print("\n🛡️ PAKAI / EQUIP ARMOR")
        # Cari armor yang dimiliki pemain
        armor_dimiliki = []
        for k, (nama_a, harga_a, bonus_a) in SHOP_ARMOR.items():
            if nama_a in inventory:
                armor_dimiliki.append((nama_a, bonus_a))
        
        if len(armor_dimiliki) == 0:
            print("Kamu belum memiliki Armor di inventory! Beli dulu di Toko.")
        else:
            print("Daftar Armor milikmu:")
            for idx, (nama_a, bonus_a) in enumerate(armor_dimiliki, start=1):
                print(f"{idx}. {nama_a} (+{bonus_a} HP)")
            
            pilih_e = input("Pilih nomor Armor yang mau dipakai: ")
            if pilih_e.isdigit() and 1 <= int(pilih_e) <= len(armor_dimiliki):
                armor_terpilih, bonus_terpilih = armor_dimiliki[int(pilih_e) - 1]
                
                # Lepas armor lama jika ada, kembalikan ke inventory
                if armor_terpakai != "Tidak Ada":
                    inventory.append(armor_terpakai)
                
                # Pasang armor baru
                armor_terpakai = armor_terpilih
                bonus_hp_armor = bonus_terpilih
                inventory.remove(armor_terpilih)
                
                # HP Maksimal naik, otomatis tambahkan HP sekarang
                hp_maksimal = hp_dasar + bonus_hp_armor
                hp_sekarang = hp_maksimal
                
                print(f"✨ Berhasil memakai {armor_terpakai}! Max HP Phainon menjadi {hp_maksimal}!")
            else:
                print("Pilihan tidak valid!")

    # 6. PAKAI POTION
    elif pilihan == "6":
        print("\n🧪 MENGGUNAKAN POTION...")
        if "Heal Deras" in inventory:
            inventory.remove("Heal Deras")
            hp_sekarang = hp_maksimal
            print(f"Kamu menggunakan Heal Deras! HP kamu kembali PENUH ({hp_maksimal}/{hp_maksimal})!")
        elif "Potion Biasa" in inventory:
            inventory.remove("Potion Biasa")
            pemulihan = int(hp_maksimal * 0.20)
            hp_sekarang = min(hp_maksimal, hp_sekarang + pemulihan)
            print(f"Kamu menggunakan Potion Biasa! HP bertambah {pemulihan}.")
        else:
            print("Kamu tidak punya Potion di inventory!")

    # 7. INVENTORY
    elif pilihan == "7":
        print("\n🎒 ISI INVENTORY KAMU:")
        if len(inventory) == 0:
            print("- (Tas Kosong)")
        else:
            for item in inventory:
                print(f"- {item}")

    # 8. KELUAR GAME
    elif pilihan == "8":
        print("\nTerima kasih sudah bermain Game Phainon! Sampai jumpa 👋")
        break

    else:
        print("\nPilihan tidak valid! Masukkan angka 1 sampai 8.")
