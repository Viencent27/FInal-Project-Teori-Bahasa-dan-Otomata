import os
from CNF import convert_CFG2CNF
from AlgorithmCYK import algorithm
from CreateTable import IndexTabel

def header(): # Header
  print("\n\t\t+ -------------" +
        " | Parsing Bahasa Baku Bahasa Indonesia | " +
        "------------- +\n\n")

def main():
  os.system("cls")
  header()
  cnf = convert_CFG2CNF() # Mendapatkan hasil dari konversi CFG ke CNF
  terminal = [] # Untuk menampung simbol dari Σ
  for i in cnf.keys(): # Untuk mendapatkan Σ dari CNF
    for j in cnf[i]:
      for k in j.split():
        if k not in cnf.keys() and k not in terminal:
          terminal.append(k)
  str = input("\nMasukkan string yang ingin dicek: ") # Meminta input user
  str = str.lower()
  string = str.split()
  lenght = len(string) # Mendapatkan panjang string untuk batas table filling
  for i in string: # Untuk mengecek input-an user
    if i not in terminal: # Apakah terdapat simbol diluar Σ
      print("String yang Anda masukkan terdapat simbol diluar Σ\n")
      loop()
  table = algorithm(cnf, string) # Untuk table filling
  IndexTabel(table, lenght)  # Untuk mencetak tabel
  for i in table[0][lenght-1]:  # Untuk cek string valid atau tidak
    valid = 0
    if i == "K":
      valid = 1
      print("String " + str + " valid!")
      break
  if valid != 1:  # Jika string tidak valid
    print("String " + str + " tidak valid!")
  loop()


def loop(): # Untuk mengulang program
  print("\nApakah Anda ingin mengulang?[y/n]")
  pil = input("\nPilihan = ")
  if pil in ["y", "Y"]:
    main()
  elif pil in ["n", "N"]:
    print("Terima kasih!^^")
    exit()
  else:
    loop()

if __name__ == "__main__":
  main()