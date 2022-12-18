def IndexTabel(table, lenght):
  global T, L, max
  T = table
  L = lenght
  max = PanjangTabel()
  for i in range(L): # Untuk index tabel dan mencetak kolom
    k = 0            # Untuk index i
    CetakTabel(i + 1)
    for j in range(L - i - 1, L): # Untuk index j
      print("|" + str(set(T[k][j])).center(max-2), end='')
      if j == L - 1:
        print("|")
      k += 1
  CetakTabel(i + 1)

def CetakTabel(loop): # Untuk mencetak +---+ pada tabel
  print("+", end='')
  for x in range(loop): # Mencetak +--+ sebanyak kolom loop
    for y in range(max-1):
      if y == max - 2:
        print("+", end='')
      else:
        print("-", end='')
  print()

def PanjangTabel(): # Untuk mendapatkan string paling panjang
  max = 0           # Sebagai batas lebar kolom
  temp = 0
  for i in range(L):  # Mencari panjang string paling besar
    for j in range(i, L):
      for k in T[i][j]:
        temp = temp + len(k)
      if max < temp:
        max = temp
      temp = 0
  max = (max * 3) + 14
  return max