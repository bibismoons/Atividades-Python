segundos = int(input("Digite um total de segundos:"))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos = segundos % 60

print(horas, minutos, segundos)