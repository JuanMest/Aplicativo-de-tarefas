import funções
import FreeSimpleGUI as sg

rotulo = sg.Text("Adicionar tarefa: ")
caixa_entrada = sg.InputText(tooltip="Digite a tarefa: ", key="tarefa")
botao_add = sg.Button("Adicionar")
caixa_lista = sg.Listbox(values=funções.leitura(), key="lista", enable_events=True, size=(30, 20))
botao_edit = sg.Button("Editar")

janela = sg.Window("Lista de tarefas",
                   layout=[[rotulo], [caixa_entrada, botao_add], [caixa_lista, botao_edit]],
                   font=('Helvetica', 15))

while True:
    evento, valores = janela.read()
    print(evento)
    print(valores)
    match evento:
        case "Adicionar":
            lista = funções.leitura()
            new_entrada = valores["tarefa"] + "\n"
            lista.append(new_entrada)
            funções.registrar(lista)
            janela['lista'].update(lista)

        case "Editar":
            item_editar = valores["lista"][0]
            novo_item = valores["tarefa"]

            lista = funções.leitura()
            index = lista.index(item_editar)
            lista[index] = novo_item + '\n'

            funções.registrar(lista)
            janela["lista"].update(values=lista)

        case "lista":
            janela['tarefa'].update(value=valores['lista'][0])

        case sg.WINDOW_CLOSED:
            break

janela.close()