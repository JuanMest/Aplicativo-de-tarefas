import funções
import FreeSimpleGUI as sg

rotulo = sg.Text("Adicionar tarefa: ")
caixa_entrada = sg.InputText(tooltip="Digite a tarefa: ")
botao_add = sg.Button("Adicionar: ")

janela = sg.Window("Lista de tarefas", layout=[[rotulo], [botao_add, caixa_entrada]])
janela.read()
janela.close()