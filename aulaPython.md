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

**• Operadores**
soma = 5 + 3
subtracao = 5 - 3
multiplicacao = 5 * 3
divisao = 5 / 2

**• Comparações**
igual = (5 == 5) # True
diferente = (5 != 3) # True
maior = (5 > 3) # True

**• If, Elif, Else**
1. idade = 18
2. if idade >= 18:
3. print("Adulto")
4. elif idade >= 13:
5. print("Adolescente")
6. else:
7. print("Criança")

**• Laço For**
for i in range(5):
print(i)

**• Laço While**
contador = 0
while contador < 5:
print(contador)
contador += 1

**• Definindo Funções**
def saudacao(nome):
return f"Olá, {nome}!"

**• Chamando Funções**
mensagem = saudacao("João")
print(mensagem)

**• Simulação de Switch-Case**
Diferente de outras linguagens, Python não possui a estrutura switch-case.
Podemos usar dicionários para simular um comportamento semelhante.

**• Simulação de Switch-Case**
1. def executar_acao(acao):
2. acoes = {
3. 1: "Ação 1: Iniciar",
4. 2: "Ação 2: Parar",
5. 3: "Ação 3: Pausar",
6. 4: "Ação 4: Reiniciar"
7. }
8. return acoes.get(acao, "Ação Inválida")
9.
10. codigo_acao = int(input("Digite o código da ação (1-4): "))
11. resultado = executar_acao(codigo_acao)
12. print(resultado)

**• Simulação de Switch-Case**
1. def executar_acao(acao):
2. acoes = {
3. 1: "Ação 1: Iniciar",
4. 2: "Ação 2: Parar",
5. 3: "Ação 3: Pausar",
6. 4: "Ação 4: Reiniciar"
7. }
8. return acoes.get(acao, "Ação Inválida")
9.
10. codigo_acao = int(input("Digite o código da ação (1-4): "))
11. resultado = executar_acao(codigo_acao)
12. print(resultado)

Dicionário acoes: Define as possíveis ações associadas a códigos.
Método get: Retorna a ação correspondente ao código inserido ou uma mensagem de "Ação Inválida" se o código não for encontrado.