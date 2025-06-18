import funções
import FreeSimpleGUI as sg

rotulo = sg.Text("Adicionar tarefa: ")
caixa_entrada = sg.InputText(tooltip="Digite a tarefa: ", key="lista")
botao_add = sg.Button("Adicionar")

janela = sg.Window("Lista de tarefas",
                   layout=[[rotulo], [botao_add, caixa_entrada]],
                   font=('Helvetica', 15))

while True:
    evento, valores = janela.read()
    print(evento)
    print(valores)
    match evento:
        case "Adicionar":
            lista = funções.leitura()
            new_entrada = valores["lista"] + "\n"
            lista.append(new_entrada)
            funções.registrar(lista)
        case sg.WINDOW_CLOSED:
            break

janela.close()