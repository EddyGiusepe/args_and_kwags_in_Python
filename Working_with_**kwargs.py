"""
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro


Trabalhando com **kwargs
========================

* **kwargs coleta todos os argumentos de palavra-chave passados para uma função.

* Permite flexibilidade no número de argumentos de palavras-chave.

* Acesse os argumentos dentro da função usando o parâmetro **kwargs.
"""

def my_function(**kwargs):
    result = ""
    for key, value in kwargs.items():
        #result += f"{key}: {value}\n"
        result = result + f"{key}: {value}\n"
    return result


output = my_function(Nome="Eddy", Idade=41, Profissão="Data Scientist", Cidade="Vitória-ES")

print(output)
