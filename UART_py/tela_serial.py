import PySimpleGUI as sg
from uart_serial import uart

arduino = uart()

class tela:
    def __init__(self, portas):
        #Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Porta:',size=(7,0)),sg.Combo(values=(portas),key='porta')],
            [sg.Text('Baudrate:',size=(7,0)),sg.Combo(values=([9600,115200]),key='baudrate')],
            [sg.Checkbox('Dados da Missão',key='dados_missao'),sg.Checkbox('Beacon',key='beacon')],
            [sg.Button('Continuar')],
        ]
        """layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(5,0),key='idade')],
            [sg.Text('Email:')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Hotmail',key='hotmail'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Radio('Sim','email',key='email_sim'),sg.Radio('Não','email',key='email_nao')],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))]
        ]"""
        #Janela
        self.janela = sg.Window("dados do Usuário").layout(layout)
        #Extrair os dados da tela
        self.button, self.values = self.janela.Read()
    
    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == sg.WIN_CLOSED:
                break
            print(self.values)

