def max_crossing_subarray(a, baixo, meio, fim):
    somaEsquerda = -float("inf")
    soma_corrente = 0
    for i in range(meio, baixo-1, -1):
        soma_corrente += a[i]
        if soma_corrente > somaEsquerda:
            somaEsquerda = soma_corrente
            max_left = i
    somaDireita = -float("inf")
    soma_corrente = 0
    for j in range(meio+1, fim+1):
        soma_corrente += a[j]
        if soma_corrente > somaDireita:
            somaDireita = soma_corrente
            maxDireito = j
    return (max_left, maxDireito, somaEsquerda+somaDireita)

def max_subarray(a, baixo, fim):
    if baixo == fim:  # base case
        return (baixo, fim, a[baixo])
    else:
        meio = (baixo+fim)//2
        left_baixo, left_fim, somaEsquerda = max_subarray(a, baixo, meio)
        right_baixo, right_fim, somaDireita = max_subarray(a, meio+1, fim)
        CruzamentoBaixo, CruzamentoFim, cross_sum = max_crossing_subarray(
            a, baixo, meio, fim)

        if somaEsquerda >= somaDireita and somaEsquerda >= cross_sum:
            return (left_baixo, left_fim, somaEsquerda)
        elif somaDireita >= somaEsquerda and somaDireita >= cross_sum:
            return (right_baixo, right_fim, somaDireita)
        else:
            return (CruzamentoBaixo, CruzamentoFim, cross_sum)

S = [5, 15, -30, 10, -5, 40, 10]
s1 = [-16,20,-10,12,27,6,4,8]

print(max_subarray(S,0,2))
print(max_subarray(s1,1,3))
print(max_subarray(s1,1,4))
