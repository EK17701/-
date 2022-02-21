a, b = map(int, input().split())
while a != 0 and b != 0:
    if a > b:
        c = a % b
    else:
        l = b % a
nod = c + l
nok = (a * b) // nod
print(nok)
