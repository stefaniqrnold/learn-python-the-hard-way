**• Declaração de Variáveis**
○ Não é necessário declarar o tipo
x = 10
y = "Hello"

**Strings**
nome = "Maria"
saudacao = 'Olá, mundo!'

**• Operações com Strings**
mensagem = "Python " + "é incrível!"

**• Métodos de Strings**
frase = "Python é poderoso"
print(frase.upper()) # PYTHON É PODEROSO
print(frase.lower()) # python é poderoso

**• Listas (coleções ordenadas e mutáveis de itens em Python.)**
lista = [1, 2, 3, 4, 5]

**• Criando e Acessando Listas**
frutas = ["maçã", "banana", "laranja"]
print(frutas) # Saída: ['maçã', 'banana', 'laranja']
print(frutas[1]) # Saída: banana

**• Iterando Sobre Listas**
for fruta in frutas:
print(fruta)

**• Adicionando e Removendo Itens**
frutas.append("manga") # Adiciona 'manga' ao final da lista
print(frutas) # Saída: ['maçã', 'banana', 'laranja', 'manga']

frutas.remove("banana") # Remove o item 'banana' da lista
print(frutas) # Saída: ['maçã', 'laranja', 'manga']

**• Modificando Itens**
frutas[0] = "pera" # Modifica o primeiro item da lista
print(frutas) # Saída: ['pera', 'laranja', 'manga']

**• Tuplas (estruturas de dados imutáveis. Útil para armazenar coleções de itens que não devem mudar.)**
tupla = (1, 2, 3, 4, 5)

**• Acessando Elementos**
primeiro_elemento = tupla[0]
ultimo_elemento = tupla[-1] # retorna o ultimo item da lista

**• Iterando sobre Tuplas**
for elemento in tupla:
print(elemento)

**• Dicionários (estruturas de dados mutáveis que armazenam pares chave-valor. Ideal para associações e buscas rápidas.)**

**• Definição**
dicionario = {
'nome': 'Ana',
'idade': 30,
'cidade': 'São Paulo'
}

**• Acessando Valores**
nome = dicionario['nome']
idade = dicionario['idade']

**• Adicionando e Modificando Itens**
dicionario['profissao'] = 'Engenheira'
dicionario['idade'] = 31

**• Manipulação de Dicionários**
dicionario = {"nome": "Carlos", "idade": 28}
dicionario["idade"] = 29 # Atualiza o valor

**• Removendo Itens**
del dicionario['cidade']

**• Iterando sobre Dicionários**
for chave, valor in dicionario.items():
print(f"{chave}: {valor}")