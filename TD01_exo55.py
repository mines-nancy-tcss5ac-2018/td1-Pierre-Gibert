def solve():
    compteur = 0
    for k in range(1,10001):
        l=[k]
        for j in range(50):
            l.append(l[-1]+reverse(l[-1]))
        for element in l:
            if element == reverse(element):
                compteur += 1
                break
    return (10000-compteur)
        
def reverse(n):
    rev=[]
    l=list(str(n))
    while l != []:
        rev.append(l[-1])
        del(l[-1])
    resultat=''
    for k in rev :
        resultat += k
    return int(resultat)

print(solve())
