# Problema do Segmento de soma máxima
## Guilherme Lucioni de Freitas

## Features

Um segmento de um vetor A[0..n − 1] ´e qualquer subvetor da forma A[i..k], com 0 ≤ i ≤ k < n. A soma de um segmento A[i..k] é o número A[i] + A[i + 1] + · · · + A[k]. E a altura de um vetor A[0..n − 1] é o valor da soma de um segmento de soma máxima.
Aplique o paradigma Divisão e Conquista para obter, e implementar, um algoritmo que determina a altura de um vetor, ou seja, um segmento de soma m´axima. Para testar sua implementação, crie instâncias de entrada diversas que considere uma quantidade razoável de situações possíveis.
O programa deve receber como entrada um vetor contendo números inteiros, e devolver como sa´ıda os índices inicial e final da altura (segmento de soma máxima), assim como o valor da soma. Por exemplo, a entrada −16 20 −10 12 27 −6 −4 8 deve produzir como saída 1 4 49.


Testes
```sh
Entrada: [5, 15, -30, 10, -5, 40, 10]
Saída: (0, 1, 20)
```
```sh
Entrada: [-16,20,-10,12,27,6,4,8]
Saída: (1, 3, 22)
```
```sh
Entrada: [-16,20,-10,12,27,6,4,8]
Saída: (1, 4, 49)
```