def resolver(expressao):
    pilha = []
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    for token in expressao.split():
        if token in operadores:
            b = pilha.pop()
            a = pilha.pop()
            resultado = operadores[token](a, b)
            pilha.append(resultado)
        else:
            pilha.append(float(token))

    return pilha[0]

# Teste
expressao = "5 1 2 + 4 * + 3 -"
resultado = resolver(expressao)
print(f"Resultado: {resultado}")