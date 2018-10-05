def solve(n):
    N=2**n
    ch=str(N)
    s=0
    for k in ch:
        s+=int(k)
    return s

assert(solve(15))==26
print(solve(1000))

#ou bien :

def solve(n):
    r=0
    while n!=0:
        r += n % 10
        n = n // 10
        return(n)
    
    assert(solve(15))==26
    print(solve(1000))