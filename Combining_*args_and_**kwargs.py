"""
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro


Combinando *args* e *kwargs
===========================

* Você pode combinar *args e **kwargs em uma definição de função.

* *args coleta argumentos que não são palavras-chave e **kwargs coleta argumentos de palavras-chave.

* Isso fornece flexibilidade na aceitação de diferentes tipos de argumentos.
"""
def my_function(*args, **kwargs):
    
    result = ""

    for arg in args:
        result += str(arg) + "\n" # Aqui o "arg" está recebendo um número

    for key, value in kwargs.items():
        result += f"{key}: {value}\n"
    return result



output = my_function(1, 2, Name="Eddy Giusepe", Profissão="Data Scientist")            

print(output)
