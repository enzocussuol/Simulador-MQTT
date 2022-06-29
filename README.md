# Simulador MQTT

Este repositório fornece um simulador MQTT local desenvolvido em Python com o objetivo de estressar o broker fornecido pelo [Mosquitto](https://mosquitto.org/). A finalidade é estudar o que acontece com o protocolo MQTT quando escalamos os dispositivos e a velocidade com que eles realizam publicações.

## Dependências

O sistema faz uso da biblioteca paho-mqtt para configurar os clientes MQTT. Para instalá-la, basta rodar o comando:

```
pip install paho-mqtt
```

## Uso

Para acompanhar o que está acontecendo no broker, abra, em outro terminal, o mosquitto em formato verboso:

```
sudo mosquitto -v
```

O simulador possui 4 parâmetros, são eles:

* tempoInstancia = Tempo em segundos em que o experimento irá rodar;
* numPublishers = Número de clientes que irão publicar mensagens em um tópico pré-definido;
* numSubscribers = Número de clientes que irão escutar por mensagens nesse mesmo tópico;
* intervaloMsgs = Intervalo em segundos em que publicante irá publicar uma mensagem.

Caso seja de interesse, o tamanho da mensagem a ser publicada pode ser alterado dentro do arquivo publisher.py, sendo o padrão a publicação de uma mensagem de tamanho 1.

Dito isso, para executar um experimento basta rodar:

```
python3 main.py <tempoInstancia> <numPublishers> <numSubscribers> <intervaloMsgs>
```

Um exemplo a ser executado por 10 segundos, com 15 publicantes, 10 inscritos e mensagens sendo enviadas a cada 0.1 segundos seria:

```
python3 main.py 10 15 10 0.1
```

## Testes

O arquivo runTests.sh implementa 3 casos de teste, nos quais alguns parâmetros são variados. Para cada teste, é gerado um arquivo .png com o gráfico que ilustra o uso de CPU e memória que o Mosquitto apresentou durante a execução do teste.

O usuário é livre para programar mais testes automatizados alterando o arquivo runTests.sh
