import clr
import os

# Ruta al archivo DLL
dll_path = r'C:\Users\CONTROL01\Documents\Jorge Documents\OT0000\py3\helloworld\AdvancedHMIDrivers.dll'

# Agregar la ruta al sistema
clr.AddReference(dll_path)

# Importar la clase
from AdvancedHMIDrivers import EthernetIPforCLXCom
from flask import Flask, render_template
import threading
import time
#crear clase de EthernetIPforCLXCom
plc = EthernetIPforCLXCom()
plc.IPAddress = "192.168.1.1"

app = Flask(__name__)

# Simulated PLC inputs
plc_inputs = [False] * 16

#Simula que esten prendiendo y apagando las entradas del PLC
def update_plc_inputs():
    while True:
        for i in range(16):
            plc_inputs[i] = not plc_inputs[i]
            time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html', plc_inputs=plc_inputs)

if __name__ == '__main__':
    threading.Thread(target=update_plc_inputs, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
