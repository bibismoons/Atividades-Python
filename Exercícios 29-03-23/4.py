num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

quociente_1 = num1/num2
quociente_2 = num2/num1

resto_1 = num1%num2
resto_2 = num2%num1

print("Na primeira divisão:", num1, "/", num2)
print("O dividendo é:", num1)
print("O divisor é:", num2)
print("O quociente é:", quociente_1)
print("O resto é:", resto_1)

print("Na segunda divisão:", num2, "/", num1)
print("O dividendo é:", num2)
print("O divisor é:", num1)
print("O quociente é:", quociente_2)
print("O resto é:", resto_2)