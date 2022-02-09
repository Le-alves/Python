#entrada de valores
gesf_E = float (input("Qual o grau Esférico do olho esquerdo: "))
while - 15 < gesf_E > 0:
    print("\nDigite um número entre 0 e -15")
    gesf_E = float (input("Primeiro teste esquerdo: "))
while gesf_E % 0.25 != 0:
    print ("Digite um numero multiplo de 0.25")
    gesf_E = float (input("Primeiro teste esquerdo: "))



gesf_D = float (input("Qual o grau Esférico do olho direito: "))
while - 15 < gesf_D > 0:
    print("\nDigite um número entre 0 e -15")
    gesf_D = float (input("Primeiro teste direito: "))

while gesf_D % 0.25 != 0:
    print ("Digite um numero multiplo de 0.25")
    gesf_D = float (input("Primeiro teste esquerdo: "))


gcil_E = float (input("Qual o grau Cilíndrico do olho esquerdo: "))
while gcil_E < -6 :
    print("\nDigite um número até -6")
    gcil_E = float (input("Segundo teste esquerdo: "))

while gcil_E % 0.25 != 0:
    print ("Digite um numero multiplo de 0.25")
    gcil_E = float (input("Primeiro teste esquerdo: "))

    

gcil_D = float (input("Qual o grau Cilíndrico do olho direito: "))
while gcil_D < -6 :
    print("\nDigite um número até -6")
    gcil_D = float (input("Segundo teste direito: "))

while gcil_D % 0.25 != 0:
    print ("Digite um numero multiplo de 0.25")
    gcil_D = float (input("Primeiro teste esquerdo: "))

# Desenvolvimento 


if (gcil_D >= -6) or (gcil_E >= -6):
    if (( -3 > gesf_E > -10 ) or ( -3 < gesf_D < -10 )):
        print ("Recomenda-se a Lente Prime")


elif (( -3 > gesf_E > -12 ) or ( -3 < gesf_D < -12 )):
    if ((gcil_E >= -2) or (gcil_D >= -2)):
        print ("Recomenda-se a Lente Prime")

else : 
    if(( -0 >= gesf_E >= -15 ) or ( -0 >= gesf_D >= -15 )):
        if (gcil_D <= -5) or (gcil_E <= -5):
         print ("Recomenda-se a Lente vision")