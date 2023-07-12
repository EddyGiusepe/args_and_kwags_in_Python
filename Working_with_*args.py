"""
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro


Trabalhando com *args
=====================

* *args coleta todos os argumentos que não são palavras-chave passados para uma função.

* Permite flexibilidade no número de argumentos.

* Acesse os argumentos dentro da função usando o parâmetro *args.
"""

def my_function(*args):
    for arg in args:
        print(arg)

print(my_function(1, 2, 3, 4))
