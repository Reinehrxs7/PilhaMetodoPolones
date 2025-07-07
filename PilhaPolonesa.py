class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, no):
        no.next = self.top
        self.top = no
        self.size += 1

    def pop(self):
        if self.size > 0:
            removido = self.top
            self.top = self.top.next
            self.size -= 1
            return removido.valor
        else:
            raise IndexError("pop from empty stack")

    def topo(self):
        if self.top is not None:
            return self.top.valor
        else:
            return None

    def tamanho(self):
        return self.size

    def __str__(self):
        if self.top is not None:
            no = self.top
            pilha_listagem = []
            while no is not None:
                pilha_listagem.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(pilha_listagem)
        else:
            return "a pilha está vazia"

# Função para resolver expressões em notação pós-fixa usando Pilha
def resolver(expressao):
    pilha = Pilha()
    tokens = expressao.split()

    for token in tokens:
        if token.replace('.', '', 1).isdigit():  
            pilha.push(No(float(token)))
        else:
            b = pilha.pop()
            a = pilha.pop()

            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                resultado = a / b
            else:
                raise ValueError(f"Operador inválido: {token}")

            pilha.push(No(resultado))

    return pilha.pop()

# Teste
if __name__ == "__main__":
    expressao = "5 1 2 + 4 * + 3 -"
    resultado = resolver(expressao)
    print(f"O resultado de '{expressao}' é: {resultado}")