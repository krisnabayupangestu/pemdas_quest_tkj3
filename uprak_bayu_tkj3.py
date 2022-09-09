#rumus volume balon p * l * t
    
print("\n1.volume balok")
p = int(input("masukkan nilai p: "))
l = int(input("masukkan nilai l: "))
t = int(input("masukkan nilai t: "))
volume_b = p * l * t
    
print("volume balok adalah", volume_b)

#rumus volume kubus s * s * s 
print("\n2.volume kubus")
s = int(input("masukkan nilai s: "))
volume_k = s * s * s 

print("volume kubus  adalah", volume_k)

#rumus volume limas 1/3 * luas alas (persegi) * tinggi
print("\n3.volume limas")
la = int(input("masukkan nilai la: "))
t = int(input("masukkan nilai t: "))
volume_l = 1/3 * la * t
    
print("volume limas adalah", volume_l)

#rumus volume tabung 22/7 * r * r * t

print("\n4.volume tabung")
r = int(input("masukkan nilai r: "))
t = int(input("masukkan nilai t: "))
volume_t = 22/7 * r * r * t

print("volume tabung adalah", volume_t)

#celcius to reamur

print("\n1.celcius to reamur")
celcius = int(input("masukkan nilai celcius: "))
reamur = 4/5 * celcius

print("reamur adalah", reamur)