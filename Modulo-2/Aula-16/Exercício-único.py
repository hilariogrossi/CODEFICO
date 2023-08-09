# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from collections import defaultdict


class Grafo(object):
    def __init__(self):
        self.vertices = defaultdict(list)


    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []


    def adicionar_aresta(self, vertice_1, vertice_2):
        if vertice_1 in self.vertices and vertice_2 in self.vertices:
            if vertice_2 not in self.vertices[vertice_1]:
                self.vertices[vertice_1].append(vertice_2)

            '''if vertice_1 not in self.vertices[vertice_2]:
                self.vertices[vertice_2].append(vertice_1)'''


    def remover_aresta(self, vertice_1, vertice_2):
        if vertice_1 in self.vertices and vertice_2 in self.vertices:
            if vertice_2 in self.vertices[vertice_1]:
                self.vertices[vertice_1].remove(vertice_2)

            '''if vertice_1 in self.vertices[vertice_2]:
                self.vertices[vertice_2].remove(vertice_1)'''


    def exibir_grafo(self):
        print('\nLista de vértices presentes no Grafo:')

        for vertice, arestas in self.vertices.items():
            print(f'Vertice {vertice}: {arestas}')


    def possui_lacos(self):
        for vertice, arestas in self.vertices.items():
            if vertice in arestas:
                return True

        return False


    def vertices_isolados(self):
        for _, arestas in self.vertices.items():
            if not arestas:
                return True

        return False
    
    def possui_arestas_paralelas(self):
        arestas_contadas = set()

        for vertice, arestas in self.vertices.items():
            for vizinho in arestas:
                aresta = tuple(sorted([vertice, vizinho]))

                if aresta in arestas_contadas:
                    return True
                
                arestas_contadas.add(aresta)
        
        return False


    def direcionado(self):
        for vertice, arestas in self.vertices.items():
            for vizinho in arestas:
                if vertice not in self.vertices[vizinho]:
                    return True
        
        return False


    def grafo_simples(self):
        return not self.possui_lacos() and not self.possui_arestas_paralelas()
        ''' if not self.possui_lacos() and not self.possui_arestas_paralelas():
                return True
            else:
                return False'''


    def grafo_completo(self):
        numero_vertices = len(self.vertices) - 1

        for vertice, arestas in self.vertices.items():
            if len(arestas) == numero_vertices:
                return True
        
        return False




def menu():
    print('''\n
    =============================================================
                            Menu:
    =============================================================
        1. Adicionar um vértice
        2. Adicionar uma aresta
        3. Remover uma aresta
        4. Exibir vértices e suas arestas
        5. Verificar se o grafo possui laços
        6. Verificar se o grafo possui vértices isolados
        7. Verificar se o grafo possui arestas paralelas
        8. Verificar se o grafo é direcionado ou não direcionado
        9. Verificar se o grafo é um grafo simples
        10. Verificar se o grafo é um grafo completo
        0. Sair
    =============================================================
    ''')


def main():
    grafo = Grafo()

    while True:
        menu()
        opcao = int(input('\nEscolha sua opção: '))

        if opcao == 0:
            print('\nSaindo do programa...\n')
            break
        
        elif opcao == 1:
            vertice = int(input('\nDigite o número do vértice a ser adiocionado: '))
            grafo.adicionar_vertice(vertice)
            print('\nVertice adicionado com sucesso!')
        
        elif opcao == 2:
            vertice_1 = int(input('\nDigite o número do primeiro vértice para formar uma aresta: '))
            vertice_2 = int(input('\nDigite o número do segundo vértice para formar uma aresta: '))

            grafo.adicionar_aresta(vertice_1, vertice_2)
            print('\nAresta adicionada com sucesso!')
        
        elif opcao == 3:
            vertice_1 = int(input('\nDigite o número do primeiro vértice para remover uma aresta: '))
            vertice_2 = int(input('\nDigite o número do segundo vértice para remover uma aresta: '))

            grafo.remover_aresta(vertice_1, vertice_2)
            print('\nAresta removida com sucesso!')
        
        elif opcao == 4:
            grafo.exibir_grafo()
        
        elif opcao == 5:
            if grafo.possui_lacos():
                print('\nO grafo possui laços.')
            
            else:
                print('\nO grafo NÃO possui laços.')

        elif opcao == 6:
            if grafo.vertices_isolados():
                print('\nO grafo possui vértices isolados.')
            
            else:
                print('\nO grafo NÃO possui vértices isolados.')
        
        elif opcao == 7:
            if grafo.possui_arestas_paralelas():
                print('\nO grafo possui arestas paralelas.')
            
            else:
                print('\nO grafo NÃO possui arestas paralelas.')

        elif opcao == 8:
            if grafo.direcionado():
                print("\nO grafo é direcionado.")
            
            else:
                print("\nO grafo NÃO é direcionado.")

        elif opcao == 9:
            if grafo.grafo_simples():
                print('\nO grafo é um grafo simples.')
            
            else:
                print('\nO grafo NÃO é um grafo simples.')
        
        elif opcao == 10:
            if grafo.grafo_completo():
                print('\nO grafo é um grafo completo.')
            
            else:
                print('\nO grafo NÃO é um grafo completo.')

        else:
            print('\nOpção inválida. Tente novamente.\n')
        

if __name__ == '__main__':
    main()
