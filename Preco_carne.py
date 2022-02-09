while True :
    print ("Caso seja Filé Duplo, tecle 1: ")
    print ("Caso seja alcatra, tecle 2: ")
    print ("Caso seja Picanhha, tecle 3: ")
    print ("Para encerrar, tecle 0")
    N_cond = int(input(" "))
    
    if N_cond == 0:
        break
    Peso_g = int (input ("Quantas gramas pesou o produto: "))
    Peso_kg = Peso_g / 1000
    Valor_file = 0
    Valor_alcatra = 0
    Valor_picanha = 0
    Valor_pagar = 0
    if N_cond == 1:
        if Peso_kg <= 5:
            Valor_file = Peso_kg * 4.90 
            Valor_pagar = Valor_file

        else :
            Valor_file = Peso_kg * 5.80
            Valor_pagar = Valor_file

    elif N_cond == 2:
        if Peso_kg <= 5:
            Valor_alcatra = Peso_kg * 5.90
            Valor_pagar = Valor_alcatra 

        else :
            Valor_alcatra = Peso_kg * 6.80
            Valor_pagar = Valor_alcatra

    elif N_cond == 3:
        if Peso_kg <= 5:
            Valor_picanha = Peso_kg * 6.90 
            Valor_pagar = Valor_picanha

        else :
            Valor_picanha = Peso_kg * 7.80
            Valor_pagar = Valor_picanha

    #Pagamento
    print ("Pagamento realizado com cartao da empresa?")
    print ("1- Sim \n2- Não")
    Desconto_cartao = float (input (" "))
    V_desc  = 0
    V_total = 0
    if Desconto_cartao == 1:
        V_desc = Valor_pagar * 0.05
        V_total = Valor_pagar - V_desc
    else:
        V_total = Valor_pagar
    
    print ("| NOTA FISCAL |")
    print ("|             |")
    print ("* Tipo de carne escolhida:  ")
    print ("* Quantidade de carne escolhida:  " ,Peso_g, "gramas" )
    print ("* Preço total:  ",Valor_pagar)
    print ("* Tipo de pagamento:  ")
    print ("* Valor do desconto:   ")
    print ("* Valor final a pagar:  ", V_total)
    
        
    


