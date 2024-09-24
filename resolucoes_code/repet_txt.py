# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

string = input("Digite uma string: ")
numero = int(input("Digite um número: "))

resultado = ' '.join([string] * numero)

# pode ser usado para dar espaço o seguinte comando: print((string + ' ') * numero)

print(resultado)