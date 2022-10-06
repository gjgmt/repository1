n = int(input())
a = list(map(int,input().split()))
n1 = min(a[0],a[5])
n2 = min(a[1],a[4])
n3 = min(a[2],a[3])
nlist = sorted([n1,n2,n3])
m1 = 5*((n-2)**2) + ((n-2)*4)
m2 = (n-2)*8 + 4
m3 = 4

a1 = nlist[0]
a2 = a1 + nlist[1]
a3 = a2 + nlist[2]

if n==1:
    print(sum(sorted(a)) - max(a))
else:
    print(a1*m1 + a2*m2 + a3*m3)
#KIT C E

print(1+1+1+1)