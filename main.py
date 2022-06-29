import psutil
import signal
import sys
import numpy as np
import time
import os

def ignoraSinal(sig, frame):
    pass

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, ignoraSinal)
    
    for proc in psutil.process_iter():
        if proc.name() == "mosquitto":
            break

    tempoInstancia = float(sys.argv[1])
    numPublishers = sys.argv[2]
    numSubscribers = sys.argv[3]
    intervaloMsgs = sys.argv[4]

    print("Rodando uma instancia do simulador MQTT")
    print("Informacoes da instancia:")
    print("Tempo maximo de execucao: ", tempoInstancia, "segundos")
    print("Numero de publicadores: ", numPublishers)
    print("Numero de inscritos: ", numSubscribers)
    print("Intervalo de tempo no envio das mensagens: ", intervaloMsgs, "segundos")

    begin = time.time()
    
    usoCPU = []
    usoMemoria = []

    comando = "python3 subscriber.py " + numSubscribers + " &" + "python3 publishers.py " + numPublishers + " " + intervaloMsgs + " &"
    os.system(comando)

    while 1:
        usoCPU.append(proc.cpu_percent())
        usoMemoria.append(proc.memory_percent())
        time.sleep(0.1)

        now = time.time()
        if now - begin >= tempoInstancia:
            cpu = np.asarray(usoCPU).mean()
            memoria = np.asarray(usoMemoria).mean()

            os.system("killall python3")
            break

    dados = open("dados.txt", "a")
    dados.write(str(cpu) + "\n")
    dados.write(str(memoria) + "\n")