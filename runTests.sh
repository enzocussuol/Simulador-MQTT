#!/bin/bash

# Teste 1: Aumentando o numero de publishers
# Numero de subscribers e intervalo entre as mensagens fixos para facilitar

rm dados.txt

for i in 1 10 50 100 200; do
    python3 main.py 10 $i 1 1
done

python3 plot.py 1

# Teste 2: Aumentando o numero de subscribers
# Numero de publishers e intervalo entre as mensagens fixos para facilitar

rm dados.txt

for i in 1 10 50 100 200; do
    python3 main.py 10 1 $i 1
done

python3 plot.py 2

# Teste 3: Diminuindo o intervalo entre as mensagens
# Numero de publishers e subscribers fixos para facilitar

rm dados.txt

for i in 10 5 1 0.1 0.01; do
    python3 main.py 10 1 1 $i
done

python3 plot.py 3

rm dados.txt