import funções
import FreeSimpleGUI as sg
import time

sg.theme("LightBlue")
relogio = sg.Text("", key="relogio")

rotulo = sg.Text("Adicionar tarefa: ")
caixa_entrada = sg.InputText(tooltip="Digite a tarefa: ", key="tarefa")
botao_add = sg.Button("Adicionar", mouseover_colors='DarkBlue')

caixa_lista = sg.Listbox(values=funções.leitura(), key="lista", enable_events=True, size=(40, 15))
botao_edit = sg.Button("Editar", mouseover_colors='DarkBlue')

botao_completar = sg.Button("completar", mouseover_colors='DarkBlue')
botao_sair = sg.Button("Sair", mouseover_colors='DarkBlue')

janela = sg.Window("Lista de tarefas",
                   layout=[[relogio],
                           [rotulo],
                           [caixa_entrada, botao_add],
                           [caixa_lista, botao_edit, botao_completar],
                           [botao_sair]],
                   font=('Helvetica', 15))

while True:
    evento, valores = janela.read(200)
    janela['relogio'].update(time.strftime("%d/%m/%Y - %H:%M:%S"))
    print(evento)
    print(valores)

    match evento:
        case "Adicionar":
            try:
                lista = funções.leitura()
                new_entrada = valores["tarefa"] + "\n"
                lista.append(new_entrada)
                funções.registrar(lista)
                janela['lista'].update(values=lista)
                janela['tarefa'].update(value="")
            except IndexError:
                sg.popup("Digite uma tarefa primeiro")

        case "Editar":
            try:
                item_editar = valores["lista"][0]
                novo_item = valores["tarefa"]

                lista = funções.leitura()
                index = lista.index(item_editar)
                lista[index] = novo_item + '\n'

                funções.registrar(lista)
                janela["lista"].update(values=lista)
                janela['tarefa'].update(value="")
            except IndexError:
                sg.popup("Selecione uma tarefa primeiro")

        case "completar":
            try:
                item_completado = valores["lista"][0]
                lista = funções.leitura()
                lista.remove(item_completado)
                funções.registrar(lista)
                janela['lista'].update(values=lista)
                janela['tarefa'].update(value="")
            except IndexError:
                sg.popup("Selecione uma tarefa primeiro")

        case "Sair":
            break

        case "lista":
            janela['tarefa'].update(value=valores['lista'][0])

        case sg.WINDOW_CLOSED:
            break

janela.close()