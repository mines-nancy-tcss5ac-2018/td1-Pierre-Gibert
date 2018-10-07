liste='abcdefghijklmnopqrstuvwxyz'

def solve():
    fichier = open('p022_names.txt',r)
    L=fichier.read()
    L.split("","")
    L.sort
    somme = 0
    for k in range(len(L)):    
        somme+=(k+1)*valeur(L,k)
    return somme

def valeur(n,k):
    r=0
    for i in n[k]:
        for j in range(len(liste)):
            if i == liste[j]:
                r += j
    return r
                
print(solve())