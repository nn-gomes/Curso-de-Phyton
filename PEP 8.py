"""
PEP 8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Pyton de forma Pytonica.

[1] - Utilize Camel Case para nomes de Classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - Utilize nomes minúsculos, separados por underline para funções e variáveis;

def soma( ):
    pass

def soma_dois ( ):
    pass

numero = 4

numero_impar = 5

[ 3 ] - Utilize 4 espaços para identação!!! (Não usar TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- 2 linhas em branco para definir uma classe ou função.
- Métodos dentro de uma classe devem ser seprados com uma única lina em branco.


class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[5] - Imports
- Imports devem ser sempre feitos em linas separadas.

[6] - Espaços em expressões de instruções.

[7] - Termine sempre uma instrução com uma lina em branco.
"""
from types import SetPointerType


class Calculadora:
    pass

class CalculadoraCientifica:
    pass


def soma( ):
    pass

def soma_dois ( ):
    pass

numero = 4

numero_impar = 5


if 'a' in 'banana':
    print('tem')

# Import errado

import sys, os

#Import Certo

import sys
import os

# Não há problema em utilizar assim:

from types import StringType, Listype

#Caso seja imports do mesmo pacote, recomenda-se fazer:

from types imports(
    StringType,
    Listype,
    SetType,
    OutroType
)

#imports devem ser colocados logo no topo do arquivo, logo depois de quaisquer comentários, ou docstrings
#e antes de constantes e variáveis globais.

# Não faça:

funcao {algo [ 1 ], {outro: 2 }}

#Faça

funcao{algo[1], {outro: 2}}

#Não faça:

dict ['chave'] = lista [indice]

#Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça

x = 1
y = 3
variavel_longa = 5


