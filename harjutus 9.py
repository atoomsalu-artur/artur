#HARJUTUS9

for i in range(1,21):
    if i&15 == 0:
        print(i, "TIKTAK")
    elif i%5 == 0:
        print(i, "TIK")
    elif i%15 == 0:
        print(i, "TIKTAK")
    else:
        print(i)