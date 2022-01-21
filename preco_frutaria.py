
print ("Caso a fruta seja uma maçã, tecle 1: ")
print ("Caso a fruta seja um morango, tecle 2: ")
N_cond = int(input(" "))

Peso_g = int (input ("Quantas gramas pesou o produto: "))
Peso_kg = Peso_g / 1000
Valor_maca = 0
Valor_morango = 0

if N_cond == 1:
    if Peso_kg <= 5:
        Valor_morango = Peso_kg * 2.50 

    else :
        Valor_morango = Peso_kg * 2.20

elif N_cond == 2:
    if Peso_kg <= 5:
        Valor_maca = Peso_kg * 1.80 

    else :
        Valor_maca = Peso_kg * 1.50

Valor_total = Valor_morango + Valor_maca

if Valor_total > 25:
    porc = Valor_total * 0.10
    Valor_total = Valor_total - porc

print ("O total a pagar será de: ", Valor_total)