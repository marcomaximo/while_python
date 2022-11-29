#Loop com contador iniciado em 0 que finaliza a execução ao possui o valor 5; somando-se 1 a cada execução
contador = 0
while (contador < 5):
       print(contador)
       contador = contador + 1


#Loop com else que valida o fim da execução ao contador obter o valor numérico igual a 10
d = 0
while d < 10:
    print(d)
    d += 1
else:
    print("Final da execução do loop")


#Loop com while True que valida a execução por 3 vezes, parando-a ao atingir esse número
m = 0
while True:
    print("Olá Mundo")
    m+=1
    if m == 3:
        break