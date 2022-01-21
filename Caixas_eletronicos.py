dinheiro = 0

while dinheiro < 10 :
    dinheiro = int (input ("Qual o valor que será sacado: "))

    while dinheiro > 600 :
        dinheiro = int (input ("Qual o valor que será sacado: "))

# Início processo
Cont_cent = 0
while dinheiro >= 100 :
    dinheiro = dinheiro - 100
    Cont_cent += 1
print ("Você ira receber ", Cont_cent, " nota(s) de cem")

Cont_cinquenta = 0
while dinheiro >= 50 :
    dinheiro = dinheiro - 50
    Cont_cinquenta += 1
print ("Você ira receber ", Cont_cinquenta, " nota(s) de cinquenta")

Cont_dez = 0
while dinheiro >= 10 :
     dinheiro = dinheiro - 10
     Cont_dez += 1
print ("Você ira receber ", Cont_dez, " nota(s) de dez")

Cont_cinco = 0
if dinheiro >= 5 :
     dinheiro = dinheiro - 5
     Cont_cinco += 1
print ("Você ira receber ", Cont_cinco, " nota(s) de cinco")

Cont_um = 0
if dinheiro >= 1 :
     dinheiro = dinheiro - 1
     Cont_um += 1
print ("Você ira receber ", Cont_um, " nota(s) de um")
