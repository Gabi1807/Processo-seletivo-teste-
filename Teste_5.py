# Definição da string a ser invertida
string = "Exemplo de string a ser invertida"

# Conversão da string em lista para possibilitar a manipulação dos caracteres
lista_caracteres = list(string)

# Inversão da ordem dos caracteres
tamanho = len(lista_caracteres)
for i in range(tamanho//2):
    lista_caracteres[i], lista_caracteres[tamanho-1-i] = lista_caracteres[tamanho-1-i], lista_caracteres[i]

# Conversão da lista de caracteres em string novamente
string_invertida = "".join(lista_caracteres)

# Impressão do resultado
print(string_invertida)
