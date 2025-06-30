# Função que resolve uma expressão aritmética em notação pós-fixa (notação polonesa reversa)
def resolver(expressao):
    pilha = []  # Inicializa uma pilha para armazenar os operandos
    tokens = expressao.split()  # Divide a string de entrada em tokens (números e operadores)

    for token in tokens:  # Itera sobre cada token
        if token.isdigit():  # Se o token for um número inteiro
            pilha.append(float(token))  # Converte para float e empilha
        else:
            # Remove os dois últimos números empilhados (operandos)
            b = pilha.pop()
            a = pilha.pop()

            # Realiza a operação correspondente ao operador encontrado
            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                resultado = a / b
            else:
                # Se o operador não for válido, lança um erro
                raise ValueError(f"Operador inválido: {token}")

            # Empilha o resultado da operação
            pilha.append(resultado)

    # Retorna o único valor restante na pilha, que é o resultado final
    return pilha[0]

# Teste da função com uma expressão em notação pós-fixa
expressao = "5 1 2 + 4 * + 3 -"
resultado = resolver(expressao)
print(f"O resultado de '{expressao}' é: {resultado}")
