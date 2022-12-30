def sol(rna):
  global keys_Q
  fin = ""
  final = True
  for i in rna:
    if i in keys_Q.keys():
      fin+=keys_Q[i]
    else:
      final = False
      break
  if final:
    return fin
  else:
    return "Unknown"


def sol2(let):

  sols = 0ṇ
  for i in range(len(let)):
    list1 = []
    try:
      word = let[i] + let[i+1]
      for l in keys_Q.keys():
        if word in l:
          str_var = let.replace(word)
          print(str_var)
          x = len(str_var)/3
          for k in range(x):
            list1.append(str_var[k*3:(k+1)*3])
          for s in list1:
            if s in keys_Q.keys():
                print(s)
                sols+=1
    
  
          
            
            
          
    except:pass
    print(list1)
  return sols
      


    
keys_Q = {
  "AUG": "M",
  "UCG": "S",
  "AGA": "R",
  "AGU": "S",
  "CAC": "H",
  "ACC": "T",
  "CCA": "P",
  "CCU": "P",
  "UCC": "S",
  "GAA": "E",
  "UCU": "S",
  "AGC": "S",
  "CUC": "L",
  "AAG": "K",
  "AAU": "N",
  "CUA": "L",
  "UAU": "Y",
  "UGG": "W",
  "GAU": "D",
  "GAG": "E",
  "AUU": "I",
  "ACA":"T"
}

t = int(input(""))
for i in range(t):
  rna = input().split("-")
  print(sol(rna))
  
n = int(input())
for f in range(n):
  let = input()
  print(sol2(let))