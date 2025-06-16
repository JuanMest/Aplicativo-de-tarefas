CAMINHO = 'lista.txt'

"""Lê o arquivo de texto e retorna para o usuário"""
def leitura(caminho=CAMINHO):
    with open(caminho, "r") as file_leitura:
        lista_leitura = file_leitura.readlines()
    return lista_leitura

"""Adiciona tarefas ao arquivo de texto"""
def registrar(lista_registro, caminho=CAMINHO):
    with open(caminho, "w") as file_registro:
        file_registro.writelines(lista_registro)
