from uart_serial import uart

arduino = uart()
arduino.update_port()
arduino.serialPort.port = 'COM5'
arduino.serialPort.baudrate = 9600
arduino.connect_serial()
cont = 0
while(1):
    arduino.ler_serial()
    if (cont>=30): break
    cont+=1
arduino.fechar_serial()
