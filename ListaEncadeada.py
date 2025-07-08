# nodo = paciente/cartão
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero  # numero do cartão
        self.cor = cor        # cor do cartão (A ou V)
        self.proximo = None   # proximo paciente na fila


# Classe principal que gerencia a fila de triagem
class ListaTriagem:
    def __init__(self):
        self.head = None      # primeiro paciente da fila
        self.contador_v = 0   # contador para cartões verdes (começa em 0)
        self.contador_a = 200 # contador para cartões amarelos (começa em 200)
    
    # adiciona paciente de cartões verdes no final da fila
    def inserirSemPrioridade(self, nodo):
        if self.head is None:  # Se fila vazia
            self.head = nodo   # O paciente é o primeiro
        else:
            atual = self.head
            # vai até o final da fila
            while atual.proximo is not None:
                atual = atual.proximo
            # adiciona o novo paciente no final
            atual.proximo = nodo
    
    # insere paciente amarelo com prioridade
    def inserirComPrioridade(self, nodo):
        if self.head is None:  # Se fila vazia
            self.head = nodo   # O paciente é o primeiro
        else:
            # Procura o ultimo paciente amarelo na fila
            atual = self.head
            ultimo_amarelo = None
            
            while atual is not None and atual.cor == 'A':
                ultimo_amarelo = atual
                atual = atual.proximo
            
            if ultimo_amarelo is None:  # Se não tem amarelos
                # insere no início da fila
                nodo.proximo = self.head
                self.head = nodo
            else:
                # insere depois do ultimo amarelo
                nodo.proximo = ultimo_amarelo.proximo
                ultimo_amarelo.proximo = nodo
    
    # adiciona novo paciente a fila
    def inserir(self):
        cor = input("Digite a cor do cartão a depender do nivel de prioridade (A para Amarelo, V para Verde): ").upper()
        
        # valida a entrada
        if cor not in ['A', 'V']:
            print("Opção inválida! Use A ou V.")
            return
        
        # define numero sequencial conforme a cor escolhida
        if cor == 'V':
            self.contador_v += 1
            numero = self.contador_v
        else:
            self.contador_a += 1
            numero = self.contador_a
        
        # cria novo paciente
        novo_nodo = Nodo(numero, cor)
        
        # insere na fila conforme a cor
        if self.head is None:  # fila vazia
            self.head = novo_nodo
        elif cor == 'V':       # paciente verde
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':       # paciente amarelo
            self.inserirComPrioridade(novo_nodo)
        
        print(f"Paciente adicionado a fila - Cartão {cor}{numero}")
    
    # mostra todos os pacientes na fila
    def imprimirListaEspera(self):
        if self.head is None:  # se fila vazia
            print("Não há pacientes na fila de espera.")
            return
        
        atual = self.head
        print("\nFila de espera:")
        # imprime toda a fila 
        while atual is not None:
            print(f"Cartão {atual.cor}{atual.numero}")
            atual = atual.proximo
        print()
    
    # chama o próximo paciente para atendimento
    def atenderPaciente(self):
        if self.head is None:  # se fila vazia
            print("Não há pacientes na fila de espera.")
            return
        
        # remove o primeiro da fila
        paciente = self.head
        self.head = self.head.proximo
        print(f"Cartão {paciente.cor}{paciente.numero}, favor comparecer ao balcão de atendimento.")


# fnção principal que roda o sistema
def main():
    sistema = ListaTriagem()  # cria o sistema
    
    while True:
        # Menu de opções
        print("\nSistema de Triagem Hospitalar")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            sistema.inserir()
        elif opcao == '2':
            sistema.imprimirListaEspera()
        elif opcao == '3':
            sistema.atenderPaciente()
        elif opcao == '4':
            print("FIM!")
            break
        else:
            print("Opção inválida, tente novamente.")


# ponto de entrada do programa
if __name__ == "__main__":
    main()