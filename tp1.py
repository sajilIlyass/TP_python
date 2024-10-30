#exercice 1 :
a= int(input(print("saisir la valeur de a :")))
b= int(input(print("saisir la valeur de b :")))
print("Somme :",a+b)
print("Difference :",a-b)
#exercice 2 :
Prix_en_euros= float(input(print("saisir le prix en euros :")))
print("Prix en euros:",Prix_en_euros)
print("Prix en dhs:",Prix_en_euros*10.627)
#exercice 3 :
a= int(input(print("saisir la valeur de a :")))
b= int(input(print("saisir la valeur de b :")))
if a+b>=100 :
    print("la somme depasse 100")
else:
    print("la somme est :",a+b)
#exercice 4 :
print("Maximum de trois entiers")
a= int(input(print("1er entier=")))
b= int(input(print("2eme entier=")))
c= int(input(print("3eme entier=")))
if (a>b and a>c):
   print("le maximum est:",a)
elif(b>a and b>c):
    print("le maximum est:",b)
else:
    print("le maximum est:",c)
#exercice 5:
str = "la"
x=int(input(print("combien de \"la\" pour l'echo ?" )))
print("Debut :\"la\"")
print(str*x)
#exercice 6:
N=int(input(print("entrer la valeur de N")))
print("le carre de ce nombre est ",N*N)
A=input(print("voulez-vous recommencer ? "))
while A=="oui": 
       N=int(input(print("entrer la valeur de N")))
       print("le carre de ce nombre est ",N*N)
       A=input(print("voulez-vous recommencer ? "))
       if A=="non":
          print("Au revoir")
          break
#exercice 7 :
X=int(input(print("taper un nombre impair :")))
while X%2==0:
    X=int(input(print("j'ai demande un nombre impair !Reessayez:")))
    if X%2!=0:
        print("Merci")
        break
#exercice 8 :
nd=int(input(print("saisir num de debut:")))   
nf=int(input(print("saisir num de fin:")))   
nz=int(input(print("saisir nombre de z:"))) 
for i in range(nd,nf,2):
    print("z"*nz+"zigzag",i)
    print(i+1,"z"*nz+"zigzag")

#exercice 9 :
n=int(input("saisir n "))
P=1
if n==0 :
    print("la factorielle de 0 vaut 1")
elif n<0 :
    print("la factorielle n'est pas definie pour les nombres negatifs") 
else :
    for i in range(1,n+1) :
        P=P*i
    print(f"la factorielle de {n} vaut {P}")          
#exercice 10 :
X=int(input(print("nombre max de lettres?")))
L=""
for i in range(1,X+1):
    Lettre=str(input(print("Lettre:")))
    if Lettre=="stop" :
        break
    L+=Lettre
print(L)
#exercice 11 :
#une suite de nmbre croissante : 1 ,2 ,3 , 4 ,....,N
N = int(input(print("saisr la valeur de N :")))
for i in range(1,N) :
    print(i,",",end='')
print(N)
print('\n')    

#une suite de nmbre decroissantes : M,M-1,......3,2,1
M = int(input(print("saisir la valeur de M :")))
for i in range(M,1,-1) :
    print(i,",",end='') 
print(M-M+1)   
print('\n')

#une suire de nmbre impaire inferieur a N :1,3,5,7,..
N = int(input(print("saisr la valeur de N :")))
if  N%2==0 :
    N=N-1
for i in range(1,N-1,2) :
       print(i,",",end='')
print(N)
print('\n')

#question 4
N = int(input(print("saisir la valeur de N :")))
for i in range(0,N):
    print(" "*i+"1")

#question 5
N = int(input(print("saisir la valeur de N :")))
for i in range(N,0,-1):
    for j in range(i) :
         print(' ',end='') 
    print(i)  


        



    