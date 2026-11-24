# Menentukan Ganjil atau Genap
def ganjil_genap(n):
    return "genap" if n % 2 == 0 else "ganjil"

# Menentukan Apakah Bilangan Prima atau Bukan
def prima(n):
    if n < 2: return False
    i = 2
    while i + i <= n:
        if n % i == 0: return False
        i += 1
        return True

# Menentukan FPB Seluruh Bilangan
def fpb(a, b):
    while b != 0: a, b = b, a % b
    return a

# Menentukan KPK Seluruh Bilangan
def kpk(a, b):
    return abs(a * b) // fpb(a, b)

# Mengubah Desimal ke Hexadesimal
def desimal_ke_hex(n):
    digit = "0123456789ABCDEF"
    hasil = " "
    while n > 0:
        hasil = digit[n % 16] + hasil
        n //= 16
        return hasil or "0"

#Struktur Program Utama
data = [260306054, 3, 11, 2026, 26, 2, 2008]

print("=" * 50)
print("ANALISIS BILANGAN")
print("=" * 50)

for n in data:
    print(f"\nBilangan  : {n}")
    print(f"Status      : {ganjil_genap(n)}")
    print(f"Prima       : {'ya' if prima(n) else 'tidak'}")
    print(f"Hex         : {desimal_ke_hex(n)}")

hasil_fpb = data[0]
hasil_kpk = data[0]
for x in data[1:]:
    hasil_fpb = fpb(hasil_fpb, x)
    hasil_kpk = kpk(hasil_kpk, x)

print(f"\nFpb semua bilangan    : {hasil_fpb}")
print(f"kpk semua bilangan      : {hasil_kpk}")