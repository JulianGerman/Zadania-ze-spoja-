import random


## Dwie cyfry silni

D = int(input("Podaj liczbe : "))
a = 1
for i in range(1, D+1):
    a = a*i
    print(a)
print(a)
print(a % 10, "\t", int((a % 100) / 10))

## NWD

a= int(input("Podaj 1 liczbe : "))
b= int(input("Podaj 2 liczbe : "))

print(a,b)




