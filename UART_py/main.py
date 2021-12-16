from uart_serial import uart
from tela_serial import tela

arduino = uart()
portas = arduino.update_port()
tela_serial = tela(portas)
tela_serial.iniciar()
arduino.serialPort.port = tela_serial.values['porta']
arduino.serialPort.baudrate = tela_serial.values['baudrate']
arduino.connect_serial()
cont = 0
while(1):
    arduino.ler_serial(10)
    if (cont>=30): break
    cont+=1
arduino.fechar_serial()
