a=0
b=0
c=0
d=0
e=0
while d==0 or c!=0:
    e=int(input("dati cifra:"))
    d=e%2
    c=e%3
    if(d==0):
        b=e+a
        a=b
    print(b)