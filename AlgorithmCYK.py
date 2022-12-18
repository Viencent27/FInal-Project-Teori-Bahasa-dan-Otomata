def algorithm(SOP, str):  # Untuk menyimpan atribut yang diperlukan
  global temp, temp1, table, cnf  # dalam algoritma CYK
  temp = [] # Untuk menampung sementara himpunan LHS untuk tabel
  temp1 = []  # Untuk menampung hasil concatenate dan union
  table = {}
  cnf = SOP
  lenght = len(str)
  for i in range (lenght):
    table[i] = {}
  insertTable(lenght, str)
  return table

def insertTable(lenght, str): # Untuk index pada Table Filling
  global temp, temp1
  for i in range (lenght):
    for j in range (lenght):
      for k in range (lenght):
        if i == 0:  # Untuk mengisi kolom pada baris pertama
          CekBhs(i, k, str) # Untuk cek simbol indeks i, k
          table[k][k] = temp  # Memasukkan himpunan LHS ke tabel
        elif j == k-i:  # Baris 2 dan seterusnya
          Baris2dst(i, j, k, str)
        temp = []
        temp1 = []
      if i == 0: break  # Baris 1 sudah terisi sehingga tidak perlu j selanjutnya

def CekBhs(a, b, str): # Untuk cek production rules
  for i in cnf.keys():
    for j in cnf[i]:
      if a == j and i not in b: # Untuk cek hasil dari concatenate dan union
        b.append(i)
      elif a == 0 and j == str[b]:  # Untuk cek simbol dari baris 1
        temp.append(i)

def Baris2dst(i, j, k, str):  # Untuk mengisi kolom pada baris 2 dan seterusnya
  for x in range (i): # Untuk concatenate dan union
    for y in table[j][j+x]:
      for z in table[j+x+1][k]:
        if y == "Ø":  # Jika terdapat Ø
          temp1.append(z)
        elif z == "Ø":
          temp1.append(y)
        else: # Jika tidak terdapat Ø
          temp1.append(" ".join([y, z]))
  for x in temp1: # Untuk cek hasil dari concatenate dan union
    CekBhs(x, temp, str)
  if temp == []:  # Jika tidak sesuai rule maka kolom diberi 'Ø'
    temp.append("Ø")
  table[j][k] = temp