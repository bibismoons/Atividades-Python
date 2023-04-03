x1 = float(input("Digite um número para definir a coordenada x do ponto A:"))
y1 = float(input("Digite um número para definir a coordenada y do ponto A:"))

x2 = float(input("Digite um número para definir a coordenada x do ponto B:"))
y2 = float(input("Digite um número para definir a coordenada y do ponto B:"))

distancia = (((x2 - x1) ** 2) + ((y2-y1) ** 2)) ** (1/2)

print("A distância entre os dois pontos é:", distancia)