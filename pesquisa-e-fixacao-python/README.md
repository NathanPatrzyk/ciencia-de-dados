1. Explique a diferença entre variáveis mutáveis e imutáveis em Python e dê exemplos de tipos de dados que pertencem a cada categoria.

Variáveis Mutáveis: Onde os conteúdos das variáveis podem ser alterados, um dos exemplos são: listas, dicionários e conjuntos.
Variáveis Imutáveis: Onde os conteúdos das variáveis não podem ser alterados, um dos exemplos são: string, booleano, float, inteiro, long e tupla.

2. Pesquise e descreva três tipos de erros comuns em Python. Na sequência diga como um programador pode solucioná-los.

TypeError: Ocorre quando uma função ou operação é aplicada a um tipo incorreto de dado, pode ser evitado ao definir todas as variáveis e usar conversões de tipos quando necessário.
IndexError e KeyError: O primeiro ocorre ao buscar um elemento com indice inexistente em uma lista, e o segundo ao buscar uma chave inexistente em um dicionário, para evitar basta fazer verificações se o índice ou chave existe.
ZeroDivisionError: Ocorre ao realizar divisão por 0 podendo ser evitado realizando validação do segundo valor não ser 0.

3. O que são funções em Python e por que elas são úteis? Explique com exemplos como definir uma função e como usar parâmetros e argumentos.

São blocos de código que realizam tarefas específicas, são úteis para organizar e reutilizar códigos.
São definidas usando:
  def nome_da_funcao():
    codigo
Para usar parâmetros e argumentos usa-se:
  def nome_da_funcao(primeira_variavel, segunda_variavel, ...):
    codigo

4. O que são listas em Python? Explique como criar uma lista, acessar elementos específicos, e adicione exemplos de como modificá-la.

É uma estrutura de dados, com itens organizados linearmente, cada um sendo acessado a partir de um índice iniciado em 0.
Para criar usa-se: lista = [] ou lista = ['item_1','item_2','item_3']
Como acessar: lista[0], lista[1] e lista[2]
Adicionar elemento no final da lista: lista.append('item_4')
Adicionar elemento em qualquer posicao: lista.insert(posicao, 'item_4')
Remover o último elemento: lista.pop()
Remover qualquer elemento: lista.pop(posicao) ou lista.pop(valor)

5. Descreva a diferença entre os métodos .append() e .extend() em uma lista. Em quais situações cada método é mais adequado?

O .append() adiciona apenas um elemento na lista, util para adicionar qualquer elemento na lista. Já o .extend() adiciona vários elementos, útil para adicionar elementos de outra lista na primeira lista, ou trabalhar com dados que podem ser iterados.

6. Como funciona o laço for em Python? Dê exemplos de como ele pode ser usado para iterar sobre uma lista e um dicionário.

O laço for irá percorrer uma lista ou uma sequência de números, executando o bloco de código para cada elemento.
Em listas:
  for elemento in lista:
    codigo
Em dicionários:
  for chave, valor in dicionario.items():
    codigo

7. Explique como funcionam as estruturas condicionais if, elif e else em Python. Dê exemplos práticos de quando cada um pode ser usado.

if: Realiza determinada operacao se a condição for verdadeira:
  if variavel > 10:
    codigo
elif: Usado abaixo de um primeiro if, se a primeira condição não for verdadeiro e a do elif for, então realizará a operação:
  if variavel > 10:
    codigo
  elif variavel < 10:
    codigo
else: Realiza uma operação se a primeira condição for falsa:
  if variavel > 10:
    codigo
  else:
    codigo

8. O que é uma string em Python e quais são algumas operações comuns que podem ser realizadas em strings? Mostre exemplos de concatenação, fatiamento e métodos como .upper() e .replace().

É um tipo de variável usado em informações textuais, no caso do python podemos acessar diferentes posições da string onde será retornado a letra de cada posicao.
Principais operações: len(), lower(), upper(), capitalize().
Upper - Converte todas as letras em maiúsculas:
string = "nome"
novaString = string.upper()
print(novaString) # Saída: "NOME"
Replace - Utilizado para substituir uma ou mais ocorrências de um conteúdo em uma string:
data = "08-11-2024"
novaData = data.replace("-","/")
print(novaData) # Saída: "08/11/2024"

9. Explique o conceito de dicionário em Python e descreva uma situação onde ele pode ser mais útil do que uma lista. Dê exemplos de como criar, acessar e modificar um dicionário.

É uma estrutura que armazena os dados em pares, cada elemento consistindo em uma chave e um valor associado a essa chave, são úteis em casos que representam situações do mundo real, como dados de um produto ou de uma pessoa.
Para criar um dicionario:
produto = {"nome": "Nome do Produto", "preco": 99.99, "tamanhos": ["P", "M", "G"]}
Para criar um dicionario vazio:
produto = {}
Para acessar os valores:
produto["nome"]
Para adicionar um novo valor ou modificar os valores:
produto["nome"] = "Novo Nome do Produto"

10. Como o Python lida com indentação de código e por que ela é importante? Dê exemplos de erros que podem ocorrer se a indentação não for usada corretamente.

Ao utilizar Python usamos o tab como indentação sem a necessidade de abrir ou fechar colchetes. Se não usado corretamente determinadas partes do código podem ser repetidas ou executadas de forma não esperada.

11. Qual a diferença entre break e continue dentro de loops em Python? Explique o efeito de cada um e dê exemplos práticos.

Break: Interrompe o loop e encerra ele.
somatoria = 0
  for venda in vendas:
    somatoria = somatoria + venda
    print("Processando...")
    if somatoria > 40000:
      print("Meta de venda batida!")
      break
Continue: Interrompe o loop, porém vai para próxima iteração.
  for cidade in cidades:
    if cidade == "Irati":
      desconto[cidade] = 0.3
      continue
    desconto[cidade] = 0.2

12. Como os operadores and, or e not funcionam em expressões condicionais em Python? Dê exemplos de situações onde cada operador seria usado.

And: Executa o código se as duas condições forem verdadeiras. Se uma pessoa tiver idade maior que 18 e menor que 70 anos paga ingresso inteiro.
Or: Executa o código se uma ou outra condição forem verdadeiras. Se uma pessoa tiver idade menor que 18 ou maior que 70 anos paga meio ingresso.
Not: Executa o código se a condição for falsa. Se uma pessoa não tiver idade menor que 18 anos paga ingresso inteiro.

13. O que vem a ser um módulo em Python? Explique a importância de bibliotecas padrão e externas, e como se usa o comando import para trabalhar com elas.

São arquivos .py que contém variaveis e funções que podem ser importados e utilizados em outros arquivos .py, as bibliotecas padrões são importantes para fornecer soluções para evitar que tenhamos que escrever o próprio código para determinada tarefa, enquanto as bibliotecas externas possibilitam que a comunidade disponibilize outras soluções mesmo que não disponíveis por padrão.
Para fazer as importações podemos usar:
import nome_do_modulo
import nome_do_modulo as ndm
from nome_do_modulo import *
from nome_do_modulo import nome_da_funcao

14. Sendo necessário fazer ordenações em listas e dicionários do Python, quais são o métodos disponíveis para essa tarefa? Dê exemplos de implementações para os dois caso.

sort: Ordena lista de valores:
  numeros = [1,3,5,2,4,6,9,8,7]
  numeros.sort()
  print(numeros_ordenados) # Saída: [1,2,3,4,5,6,7,8,9]
sorted: Ordena uma lista ou dicionario (ordena pela chave) de valores.
  numeros = { 1: "Um", 3: "Tres", 5: "Cinco", 2: "Dois", 4: "Quatro", 6: "Seis", 9: "Nove", 8: "Oito", 7: "Sete" }
  numeros_ordenados = sorted(numeros)
  print(numeros_ordenados) # Saída: { 1: "Um", 2: "Dois", 3: "Tres", 4: "Quatro", 5: "Cinco", 6: "Seis", 7: "Sete", 8 "Oito", 9: "Nove" }

15. Descreva o que é uma list comprehension em Python e como ela pode ser usada para gerar listas de forma eficiente. Forneça exemplos comparando list comprehension com um loop for.

É uma forma de criar listas usando um sintaxe concisa. Gerando uma nova lista aplicando uma expressão para cada item um determinado iterável.
Usando list comprehension:
  lista = [1,2,3,4,5]
  resultado = [elemento**2 for elemento in lista]
  print(resultado) # Saída: [1,4,9,16,25]
Usando loop for:
  lista = [1,2,3,4,5]
  resultado = []
  for elemento in lista:
    resultado.append(elemento**2)
  print(resultado) # Saída: [1,4,9,16,25]
