from CFG import dictCFG

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cfg = dictCFG()
cnf={}

def cek_Non_Terminal(RHS):  # Cek jumlah non terminal di RHS (S P O Ket)
  count = 0 
  temp = RHS.split()  # Memisahkan tiap kata ['S', 'P', 'O', 'Ket']
  for x in temp:
    if x in cfg.keys(): # Cek apakah x non terminal atau bukan
      count += 1
  return count

def Buat_Rule_Baru(RHS):  # Membuat rule baru jika terdapat lebih dari 2 non terminal
  temp = RHS.split()      # Memisahkan tiap kata ['S', 'P', 'O']
  while len(temp) != 2:   # Berhenti jika sudah ['A', 'B']
    list_temp = []        # Untuk menyimpan hasil gabungan string index 0 dan 1
    temp[0] = " ".join([temp[0], temp[1]])  # Gabungkan string index 0 dan 1 (['S P', 'P', 'O'])
    list_temp.append(temp[0])
    temp.pop(1)           # Menghilangkan string index 1 (['S P', 'O'])
    if list_temp not in cnf.values(): # Buat rule baru jika 'S P' tidak ada di cnf
      for x in alphabets:         # Ambil LHS dari list alphabets
        if x not in cnf.keys():   # Jika alphabets x belum digunakan
          cnf[x] = list_temp      # Masukkan ke cnf: x --> S P
          temp[0] = x             # Lalu ubah 'S P' di list menjadi x (['X', 'O'])
          break
    else:         # Jika 'S P' sudah ada di cnf (X --> S P)
      for x in cnf:     # Untuk mendapatkan LHS nya
        if cnf[x] == list_temp:   # Jika RHS dari LHS == S P
          temp[0] = x   # Maka ubah 'S P' di list menjadi LHS nya
          break
  RHS_Baru = " ".join([temp[0], temp[1]])   # Gabungkan string di list menjadi ['X O']
  return RHS_Baru

def convert_CFG2CNF():
  for i in cfg:
    RHS = []
    for j in cfg[i]:
      jml_nonterminal_RHS = cek_Non_Terminal(j)
      if jml_nonterminal_RHS == 2 or jml_nonterminal_RHS == 0:
        RHS.append(j)   # Jika non terminal == 2 atau non terminal == 0 (ia adalah terminal) masukkan ke list RHS
      elif jml_nonterminal_RHS > 2:
        RHS.append(Buat_Rule_Baru(j))
      elif jml_nonterminal_RHS == 1:
        for k in cfg[j]: # Jika non terminal == 1 maka ubah menjadi RHS dari non terminal tersebut (S --> NP, NP --> NP Noun maka S --> NP Noun)
          if cek_Non_Terminal(k) >= 2:
            RHS.append(Buat_Rule_Baru(k))
          elif cek_Non_Terminal(k) == 0:
            RHS.append(k)
          elif cek_Non_Terminal(k) == 1:
            for l in cfg[k]:  # Jika kasus S --> NP, NP --> Noun, Noun --> ayam maka S --> ayam
              RHS.append(l)
    cnf[i] = RHS      # Masukkan list RHS ke cnf
  
  return cnf

convert_CFG2CNF()