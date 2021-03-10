from time import sleep

def More():
 print('Are you want once again')
 print('A.Yes\nB.No')
 more = input('Enter A or B: ').upper()

 if more == 'A':
  print('ok!')
  wait()
  start()
  re()
 else:
     print('Thank You!')




def coverter(List):
 i =0
 while i<=len(List):
   t = List[i:i+3]
   if t=='UUU' or t=='UUC':
     print('Phe',end=" ")                                                           #Phe
   elif t=='UUA' or t=='UUG' or t=='CUU' or t=='CUC' or t=='CUA' or t=='CUG':
     print("Leu",end=" ")                                                           #Leu
   elif t == 'UCU' or t=='UCC' or t=='UCA' or t=='UCG':
     print('Ser',end=" ")                                                           #Ser
   elif t == 'UAU' or t=='UAC':
     print('Tyr',end=" ")                                                           #Tyr
   elif t == 'UUU' or t=='UGC' :
     print('Cys',end=" ")                                                           #Cys
   elif t == 'CCU' or t=='CCC' or t=='CCA' or t=='CCG':
     print('Pro',end=" ")                                                           #Pro
   elif t == 'CAU'or t=='CAC' :
     print('His',end=" ")                                                           #His
   elif t == 'CAA' or t=='CAG':
     print('Gln',end=" ")                                                           #Gln
   elif t == 'CGA' or t=='CGU' or t=='CGC' or t=='CGG':
     print('Arg',end=" ")                                                           #Arg
   elif t == 'AUU' or t=='AUC' or t=='AUA':
     print('lle',end=" ")                                                           #lle
   elif t == 'AUG':
     print('Met',end=" ")                                                           #Met
   elif t == 'ACU' or t=='ACC' or t=='ACA' or t=='ACG':
     print('Thr',end=" ")                                                           #Thr
   elif t == 'AAU' or t=='AAC':
      print('Asn',end=" ")                                                          #Asn
   elif t ==  'AAA' or t=='AAG':
      print('Lys',end=" ")                                                          #Lys
   elif t == 'AGU' or t=='AGC':
      print('Ser',end=" ")                                                          #Ser
   elif t == 'AGA' or t=='AGG':
      print('Arg',end=" ")                                                          #Arg
   elif t == 'GUU' or t=='GUC' or t=='GUA' or t=='GUG':
      print('Val',end=" ")                                                          #Val
   elif t == 'GCU' or t=='GCC' or t=='GCA' or t=='GCG':
      print('Ala',end=" ")                                                          #Ala
   elif t == 'GAU' or t=='GAC':
      print('Asp',end=" ")                                                          #Asp
   elif t == 'GAA' or t=='GAG':
      print('Glu',end=" ")                                                          #Glu
   elif t == 'GGU' or t=='GGC' or t=='GGA' or t=='GGG':
      print('Giy',end=" ")                                                          #gly
   elif t == 'UAA' or t=='UAG' or t=='UGA' :
      print('STOP!',end=" ")                                                        #Stop
      print()

   i=i+3
 print()
 More()

def start():
 print('Please Choice any option')
 print('********************')
 print('A. DNA -->m-RNA ')
 print('B. m-RNA-->Protien ')
 print('C. DNA --> Protien ')
 print('====================')

start()
def wait():
    print('Your request under procesing')
    for i in range(5):
        print('..',end='')
        sleep(0.5)

    print()


def re():
 Input= input('Enter your choice: ').upper()
 if Input == 'C':


  x=""
  code = input('Enter your DNA code: ').upper()
  wait()
  for i in code:
    if i == 'G':
     x+=str('C')
    elif i =='T':
     x += str('A')
    elif i == 'C':
     x += str('G')
    elif i == 'A':
     x += str('U')
  List = x
  coverter(List)
 elif Input =='B':

  List = input('Enter your m-RNA code: ').upper()
  wait()
  coverter(List)


 elif Input == 'A':
    x = ""
    code = input('Enter your DNA code: ').upper()
    wait()
    for i in code:
        if i == 'G':
            x += str('C')
        elif i == 'T':
            x += str('A')
        elif i == 'C':
            x += str('G')
        elif i == 'A':
            x += str('U')
        List = x
    print(x)


 else:
    wait()
    print('Invalid Input!!!')

re()
More()

