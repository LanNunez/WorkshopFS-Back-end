# ESTRUTURAS DE REPETIÇÃO 

# while True:
#     resposta = input("Digite 'sair para encerrar:  '")
#     if resposta.lower() == "sair":
#         print("Encerrando o programa...")
#         break
#     else:
#         print("Você digitou:", resposta)


#======================================================================


# DESAFIO CAIXA ELETRÔNICO
# saldo = 0
# extrato = []
# while True:
#     print("=============================")
#     print("Simulador de Caixa Eletronico")
#     print("=============================")
#     print("1- Depósito")
#     print("2- Saque")
#     print("3- Extrato")
#     print("4- Sair")
#     print("=============================")
#     opcao = int(input("Digite a opção desejada: "))
#     if opcao == 1:
#         valor = float(input("Digite o valor do depósito: "))
#         if valor <= 0:
#             print("Valor inválido!")
#             continue
#         saldo += valor
#         extrato.append(f"Depósito: +R${valor:.2f}")
#         print("Depósito de R$", valor, "realizado com sucesso!")
#     elif opcao == 2:
#         valor = float(input("Digite o valor do saque: "))
#         if valor > saldo:
#             print("Saldo insuficiente!")
#             continue
#         else:
#             print("Saque de R$", valor, "realizado com sucesso!")
#             saldo -= valor
#             extrato.append(f"Saque: -R${valor:.2f}")
#     elif opcao == 3:
#         print("=============================")
#         print("======= Extrato =============")
#         print("=============================")
#         if not extrato:
#             print("Nenhuma movimentação.")
#         else:
#             for item in extrato:
#                 print(item)
        
#         print(f"\nSaldo atual: R${saldo:.2f}")
#     elif opcao == 4:
#         print("Saindo do programa...")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")


#=====================================================================

#Listas 

# numeros = [10, 20, 30, 40, 50]

# numeros.remove(20)
# numeros.pop(0)
# numeros.append(60)
# print(numeros)
# print(len(numeros))
# numeros.clear

# Listas Tipo Tuplas
# coordenada = (10, 20)
# print(coordenada[0])
# print(coordenada[1])

# Listas tipo Dicionario
# pessoa = {
#     "nome": "Arllan",
#     "idade": 18,
#     "altura": 1.65,
#     "Cidade": "Caaporã"
# }

# print(pessoa["nome"]) # Acessa o valor da chave "nome"
# print(pessoa["idade"])
# print(pessoa["altura"])
# print(pessoa["Cidade"])

# Listas tipo Conjunto

# numeros = {1, 2, 3, 4, 5}

# numeros.add(6)
# print(numeros)

# numeros.remove(2)
# print(numeros)

# numeros.clear()
# print(numeros)


# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

#============================================

#Funções

# def saudacao (nome):
#     print(f"Olá, {nome}!")

# saudacao("Arllan")

# # Adição em Funções 
# def soma (x, y):
#     return x + y
# resultado = soma(10, 20)
# print(resultado)



#================================================")


# Programação Orientada a Objetos (POO)

#Fazer uma Calculadora usando POO e Funções 
# class calculadora:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def soma(self):
#         return self.num1 + self.num2

#     def subtracao(self):
#         return self.num1 - self.num2

#     def multiplicacao(self):
#         return self.num1 * self.num2

#     def divisao(self):
#         if self.num2 != 0:
#             return self.num1 / self.num2
#         else:
#             return "Divisão por zero não é permitida."


# def menu():
#     print("Bem-vindo à calculadora simples!")
#     print("Escolha a operação desejada:")
#     print("1 - Soma")
#     print("2 - Subtração")
#     print("3 - Multiplicação")
#     print("4 - Divisão")
#     print("5 - Sair")
#     return input("Digite o número da operação: ")

# def main():
#     while True:
#         opcao = menu()

#         if opcao == '1':
#             num1 = float(input("Digite o primeiro número: "))
#             num2 = float(input("Digite o segundo número: "))
#             calc = calculadora(num1, num2)
#             print(f"Resultado: {calc.soma()}")
            
#         elif opcao == '2':
#             num1 = float(input("Digite o primeiro número: "))
#             num2 = float(input("Digite o segundo número: "))
#             calc = calculadora(num1, num2)
#             print(f"Resultado: {calc.subtracao()}")
            
#         elif opcao == '3':
#             num1 = float(input("Digite o primeiro número: "))
#             num2 = float(input("Digite o segundo número: "))
#             calc = calculadora(num1, num2)
#             print(f"Resultado: {calc.multiplicacao()}")
            
#         elif opcao == '4':
#             num1 = float(input("Digite o primeiro número: "))
#             num2 = float(input("Digite o segundo número: "))
#             calc = calculadora(num1, num2)
#             print(f"Resultado: {calc.divisao()}")
            
#         elif opcao == '5':
#             print("Encerrando a calculadora. Até mais!")
#             break

#         else:
#             print("Opção inválida. Por favor, escolha uma opção válida.")
# main()

# ================================================================================

# import math

# print(math.sqrt(9))
# print(math.pi)

# import random

# print(random.randint(1, 10))


# import datetime

# agora = datetime.datetime.now()
# print(agora)
