# Vamos solicitar como entrada dois números e depois vamos realizar uma operação entre eles.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(numero1 + numero2)
elif operacao == '-':
    print(abs(numero1 - numero2))
elif operacao == '*':
    print(numero1 * numero2)
elif operacao == '/':
    print(numero1 / numero2)
else:
    print("Operação inválida")    

#print(numero1 * numero2)