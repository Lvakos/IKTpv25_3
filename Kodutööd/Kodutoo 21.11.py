#4
for i in range(10, 20):
    print(i * i)

#5
tulemus = 0
while True:
    try:
        arv = input("Sisesta arv, kui sa tahad peatuda, sisesta (stop): ")
        if arv == "stop" or arv == "Stop":
            print(f"Tulemus: {tulemus}")
            break
        elif int(arv) < 0:
            tulemus += int(arv)
        elif int(arv) >= 1:
            continue
    except:
        print("Viga, palun sisesta arv!")

#6
negativ = 0
positiv = 0
nullid = 0

while True:
    try:
        numbrid = input("Sisesta arv(kui sa tahad peatuda, sisesta (stop): ")
        if numbrid == "stop" or numbrid == "Stop":
            print("Negatiivne:", negativ)
            print("Positiivne:", positiv)
            print("Nullid:", nullid)
            break
        elif int(numbrid) > 0:
            positiv += 1
            continue
        elif int(numbrid) < 0:
            negativ += 1
            continue
        elif int(numbrid) == 0:
            nullid += 1
            continue
    except:
        print("Viga, palun sisesta arv!")

#7

a = int(input("Sisesta simene arv: "))
b = int(input("Sisesta teine arv: "))
k = int(input("Sisesta arv, millega jagada: "))

if a <= b:
    for i in range(a, b + 1):
        if i % k == 0:
            print(i)
else:
    for i in range(a, b - 1, -1):
        if i % k == 0:
            print(i)
#8
cm = 1
toll = 2.5
counts = 1

while True:
    print(cm, "cm =", toll, "tolli")
    toll += 2.5
    cm+= 1
    counts += 1
    if counts == 21:
        break
    else:
        continue
