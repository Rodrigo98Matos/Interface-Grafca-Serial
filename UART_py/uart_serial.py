import serial
import serial.tools.list_ports


class uart():
    def __init__(self):
        self.serialPort = serial.Serial()
        self.baudrate = [9600, 115200]
        self.portlist = list()


    def update_port(self):
        """
        Metodo update de portas seriais
        """
        self.portlist = [port.device for port in serial.tools.list_ports.comports()]
        return self.portlist
    

    def connect_serial(self):
        """
        Conexão
        """
        try:
            self.serialPort.open()
        except:
            print("Houve um erro ao abrir a serial!")
    


    def ler_serial(self, size_byte):
        """Recebe dados"""
        dados_lidos = self.serialPort.readline().decode('utf-8')
        print(dados_lidos)


    def enviar_serial(self, dado):
        """Envia mensagem ou dado via serial"""
        if(self.serialPort.isOpen()):
            enviar_dado = str(self.dado)+'\n'
            self.serialPort.write(enviar_dado.encode())
            self.serialPort.flushOutput()

    

    def fechar_serial(self):
        """Fechar"""
        self.serialPort.close()
