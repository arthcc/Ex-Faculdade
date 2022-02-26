d = float (input ("Digite a distância percorrida em KM: "))
t = float (input ("Digite o tempo percorrido em HORAS:"))

v = d / t

if v>80:
    print ("Sua velociade Média está acima de 80 km/h")
else:
    print ("Sua Velocidade Média está abaixo de 80 km/h")