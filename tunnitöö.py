#ISESEISEV TÖÖ ÜKS

#print ("Tere Maailm")

#aasta = 2020
#liblikas = "teelehe-mosaiikliblikas"
#lause_keskosa = "aasta liblikas on"
#lause = "aasta" "lause" "liblikas"
#lause= str(aasta) + " " + lause_keskosa + " " + liblikas + ""
#print(lause)

korgus = float(input("Sisesta pilvede kõrgus kilomeetrites: "))

if korgus > 6:
    print("Need on ülemised pilved.")
elif 2 <= korgus <= 6:
    print("Need on keskmised pilved.")
else:
    print("Need on alumised pilved.")

