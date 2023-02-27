# Pede ao usuário um número para verificar se ele pertence à sequência de Fibonacci
num = int(input("Digite um número inteiro: "))

# Inicializa as variáveis para o cálculo da sequência de Fibonacci
a, b = 0, 1
fibonacci = []

# Calcula a sequência de Fibonacci até encontrar um valor maior ou igual ao número informado
while b < num:
    fibonacci.append(b)
    a, b = b, a + b

# Verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

