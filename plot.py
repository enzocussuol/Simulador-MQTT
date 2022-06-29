import matplotlib.pyplot as plt
import sys

dados = open("dados.txt", "r")

dadosCPU = []
dadosMemoria = []

for i in range(0, 5):
    cpu = float(dados.readline())
    memoria = float(dados.readline())

    dadosCPU.append(cpu)
    dadosMemoria.append(memoria)

plt.clf()
teste = int(sys.argv[1])

if teste == 1:
    plt.plot([1, 10, 50, 100, 200], dadosCPU, color="b", label="CPU")
    plt.plot([1, 10, 50, 100, 200], dadosMemoria, color="r", label="Memoria")
    plt.xlabel("Number of Publishers")
    plt.title("CPU and Memory Usage by Number of Publishers")
    plt.legend()
    plt.savefig("teste1.png")

if teste == 2:
    plt.plot([1, 10, 50, 100, 200], dadosCPU, color="b", label="CPU")
    plt.plot([1, 10, 50, 100, 200], dadosMemoria, color="r", label="Memoria")
    plt.xlabel("Number of Subscribers")
    plt.title("CPU and Memory Usage by Number of Subscribers")
    plt.legend()
    plt.savefig("teste2.png")

if teste == 3:
    plt.plot([10, 5, 1, 0.1, 0.01], dadosCPU, color="b", label="CPU")
    plt.plot([10, 5, 1, 0.1, 0.01], dadosMemoria, color="r", label="Memoria")
    plt.xlabel("Message Interval Time (seconds)")
    plt.title("CPU and Memory Usage by Message Interval")
    plt.legend()
    plt.gca().invert_xaxis()
    plt.savefig("teste3.png")