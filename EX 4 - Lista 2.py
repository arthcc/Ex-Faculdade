preço = float(input("Digite o valor do produto: R$"))
forma_de_pagamento = float (input ("Digite o código de pagamento:"))
preço_cartao = preço * 10 / 100
preço_avista = preço * 20 / 100

valor_final = preço - preço_cartao
valor_final2 = preço - preço_avista

if forma_de_pagamento == 5:
    print (f"O produto que custa R$ {preço}, no pagamento em cartão, custa: {valor_final}")
else:
    print (f"O produto que custa R$ {preço}, no pagamento a vista, custa: {valor_final2}") 
