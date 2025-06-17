import funções
import time

tempo = time.strftime("%d/%m/%Y - %H:%M:%S")
print("Data e horário: ", tempo)

while True:
    acao_usuario = input("Adicionar, mostrar, editar, completar, sair: ").lower()
    acao_usuario = acao_usuario.strip()

    if acao_usuario.startswith("adicionar"):
        tarefa = acao_usuario[10:] + "\n"

        lista = funções.leitura()

        lista.append(tarefa)

        funções.registrar(lista)

    elif acao_usuario.startswith("mostrar"):

        lista = funções.leitura()

        for indice, item in enumerate(lista):
            item = item.title()
            print(f"{indice + 1} -", item.strip('\n'))

    elif acao_usuario.startswith("editar"):
        try:
            numero = int(acao_usuario[7:])
            numero = numero - 1

            lista = funções.leitura()

            nova_tarefa = input("Adicione sua nova tarefa: ")
            lista[numero] = nova_tarefa + '\n'

            funções.registrar(lista)

            print(lista[numero])

        except ValueError:
            print("Comando inválido")
            continue

    elif acao_usuario.startswith("completar"):
        try:
            n = int(acao_usuario[11:])

            lista = funções.leitura()

            index = n - 1
            item_removido = lista[index]
            lista.pop(index)

            funções.registrar(lista)

            print(f"O item {item_removido.strip()} foi concluído na sua lista de tarefas!")

        except IndexError:
            print("Não existe nenhuma tarefa com este número!")
            continue

    elif acao_usuario.startswith("sair"):
        break

    else:
        print("Comando inválido!")

print("Programa finalizado com sucesso!")
