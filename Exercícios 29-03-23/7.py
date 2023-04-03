valor_a = float(input("Digite o primeiro número:"))
valor_b = float(input("Digite o segundo número:"))
valor_c = float(input("Digite o terceiro número:"))
valor_d = float(input("Digite o quarto número:"))

media_aritmetica = (valor_a + valor_b + valor_c + valor_d)/4
media_harmonica = 4/((1/valor_a) + (1/valor_b) + (1/valor_c) + (1/valor_d))
media_geometrica = (valor_a * valor_b * valor_c * valor_d) **(1/4)
media_quadratica = ((valor_a ** 2) + (valor_b ** 2) + (valor_c ** 2) + (valor_d ** 2))/4

print("A média aritmética é:", media_aritmetica)
print("A média harmônica é:", media_harmonica)
print("A média geométrica é:", media_geometrica)
print("A média quadrática é:", media_quadratica)