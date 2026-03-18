#print("Olá, mundo!"   # Erro de Sintaxe na ausencia do ")" fechando o comando print.
# Jeito certo: print ("Olá, mundo")

#print(nome) # NameError, Variavel que ainda não foi definida.
# Jeito certo:
# nome = "Arllan"
# print(nome)

# def somar(a, b):
#     return a + b

# resultado = somar(10, "5") # Erro de Tipagem (TypeError). O código tenta juntar tipos incompativeis como um inteiro + string 
# print(resultado)

#Jeito certo abaixo:

#def somar(a, b):
#     return a + b
#
# resultado = somar(10, 5)
# print(resultado)

# numeros = [10, 20, 30] # Corrigindo um Erro de Índice (IndexError) 
# indice = int(input("Digite um índice para acessar a lista: ")) # Se o usuario digitar um indice que não tenha na lista o erro acontece. E também há um possivel ValueError caso o usuario coloque um caractere invalido.

# print(numeros[indice]) 

# Jeito certo: 

# numeros = [10, 20, 30]

# try:
#     indice = int(input("Digite um índice para acessar a lista: "))
#     print(numeros[indice])
# except ValueError:
#     print("Erro: Digite um número inteiro válido.")
# except IndexError:
#     print("Erro: Índice fora do intervalo da lista.")

# def dividir(a, b):
#     return a / b # ZeroDivisionError ocorre quando o usuario tenta dividir algo por zero.

# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ") 

# resultado = dividir(int(num1), int(num2)) #ValueError usuario vai digitar um número com a tipagem string, e aqui tenta dividir inteiro com a string que o usuario digitou 
# print(f"Resultado: {resultado}")