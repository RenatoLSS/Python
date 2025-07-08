#Estadunode = identificador de estados
class EstadoNode:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None

class HashTabEstados:
    def __init__(self):
        self.tamanho = 10
        self.tabela = [None] * self.tamanho
    
    def calcular_hash(self, sigla):
        if sigla == 'DF':
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10
    
    def inserir_estado(self, sigla, nome):
        posicao = self.calcular_hash(sigla)
        novo_node = EstadoNode(sigla, nome)
        novo_node.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_node
    
    def mostrar_tabela(self):
        print("\nTabela Hash:")
        print("Pos | Estados")
        print("----+---------")
        for i in range(self.tamanho):
            print(f"{i:3} |", end=" ")
            atual = self.tabela[i]
            while atual:
                print(f"{atual.sigla}", end=" -> ")
                atual = atual.proximo
            print("None")

def main():
    # cria tabela vazia
    hashestados = HashTabEstados()
        
    # 1. mostrar tabela vazia
    print("\n[H] Tabela hash vazia:")
    hashestados.mostrar_tabela()
    
    # 26 estados + DF
    estados = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]
    
    # 2. inserir 26 estados + DF
    for sigla, nome in estados:
        hashestados.inserir_estado(sigla, nome)
    
    print("\n[I] Tabela após inserir 26 estados + DF:")
    hashestados.mostrar_tabela()
    
    # 3. inserir estado fictício (Meu nome RENATO LUCAS SOUZA SANTOS - LS definido para não conflitar com RS) 
    hashestados.inserir_estado('LS', 'Lucas Santos')
    
    print("\n[J] Tabela após inserir estado fictício:")
    hashestados.mostrar_tabela()

if __name__ == "__main__":
    main()