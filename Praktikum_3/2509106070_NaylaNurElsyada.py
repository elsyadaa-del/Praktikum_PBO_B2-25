# class animal:
#     def __init__(self, nama):
#         self.nama = nama

#     def makan(self):
#         print(f"{self.nama} sedang makan.")

# class mamalia(animal):
#     def __init__(self, nama, WarnaBulu):
#         super().__init__(nama)
#         self.WarnaBulu = WarnaBulu

#     def makan(self):
#         print(f"{self.nama} sedang makan dan bulunya berwarna {self.WarnaBulu}.")

# class AkunBank:
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

#     def hitung_bunga(self):
#         return self.saldo * 0.05

#     class Deposito(AkunBank):
#         def hitung_bunga(self):
#             return self.saldo * 0.07

# daftar_akun = [AkunBank("Nayla", 1000000), AkunBank.Deposito("Nayla", 1000000)]

# for akun in daftar_akun:
#     print(akun.hitung_bunga())




# from abc import ABC, abstractmethod
# class AkunBank(ABC):
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

# class Tabungan(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.05      


import re


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def serang(self, target): # tugas 1: pertarungan
        target.health -= 10

    def tampilkan_status(self): # tugas 2: tampilan
        print(f"{self.name} | HP {self.health}")

    def simpan(self, nama_file): # tugas 3: penyimpanan
        with open(nama_file, "a") as f:
            f.write(f"{self.name},{self.health}\n")

class Hero: # hanya pertarungan
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def serang(self, target):
        target.health -= 10

class TampilanHero: # hanya tampilan
    def tampilkan(self, hero):
        print(f"{hero.name} | HP {hero.health}")

class PenyimpanHero: # hanya penyimpanan
    def simpan(self, hero, nama_file):
        with open(nama_file, "a") as f:
            f.write(f"{hero.name},{hero.health}\n")

layla = Hero("Layla", 70)
Hero("Balmond", 120).serang(layla)
TampilanHero().tampilkan(layla)
PenyimpanHero().simpan(layla, "data_hero.txt")

def hitung_damage(role, attack):
    if role == "fighter":
        return attack + 5
    elif role == "mage":
        return attack * 2
    elif role == "assassin":
        return attack * 3
    else:
        return 0

print(hitung_damage("fighter", 10))
print(hitung_damage("mage", 10))
print(hitung_damage("assassin", 10))

class pedang:
    def pukul(self):
        return 20

class hero:
    def __init__(self, nama):
        self.nama = nama
        self.senjata = pedang
 