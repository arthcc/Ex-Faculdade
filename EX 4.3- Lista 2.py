preço = float (input ("Digite o preço do produto R$:"))
codigo = float (input ("Digite o código do pagamento:"))

preço_cartao = preço * 10 / 100
preço_avista = preço * 20 / 100
preço_3vzs = preço * 5 / 100

valor_final = preço - preço_cartao
valor_final2 = preço - preço_avista
valor_final3 = preço - preço_3vzs

if codigo == 5:
    print (f"O produto que custa R$ {preço}, no pagamento em cartão custa: {valor_final}")
elif codigo == 6:
    print (f"O produto que custa R$ {preço}, no pagamento em cartão custa: {valor_final2}")
elif codigo == 7:
    print (f"O produto que custa R$ {preço}, no pagamento em cartão parcelado em três vezes custa: {valor_final3}")
else:
    print ("Código de pagamento incorreto, por favor digite novamente:")    

