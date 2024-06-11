import numpy as np
import random
import pickle

# Resgatando os modelos de previsão para serem usados nesse script
with open('modelo_rf_bg.pkl', 'rb') as file:
    modelo_bg = pickle.load(file)
    
with open('modelo_rf_cf.pkl', 'rb') as file:
    modelo_cf = pickle.load(file)


# Eletronegatividade de cada elemento químico 
eletronegatividades = {
 'H': 2.2, 'Li': 0.98, 'Be': 1.57, 'B': 2.04, 'C': 2.55, 'N': 3.04, 'O': 3.44, 'F': 3.98, 'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.9,
 'P': 2.19, 'S': 2.58, 'Cl': 3.16, 'K': 0.82, 'Ca': 1.0, 'Sc': 1.36, 'Ti': 1.54, 'V': 1.63, 'Cr': 1.66, 'Mn': 1.55, 'Fe': 1.83, 'Co': 1.88,
 'Ni': 1.91, 'Cu': 1.9, 'Zn': 1.65, 'Ga': 1.81, 'Ge': 2.01, 'As': 2.18, 'Se': 2.55, 'Br': 2.96, 'Rb': 0.82, 'Sr': 0.95, 'Y': 1.22, 'Zr': 1.33,
 'Nb': 1.6, 'Mo': 2.16, 'Ru': 2.2, 'Rh': 2.28, 'Pd': 2.2, 'Ag': 1.93, 'Cd': 1.69, 'In': 1.78, 'Sn': 1.96, 'Sb': 2.05, 'Te': 2.1, 'I': 2.66,
 'Cs': 0.79, 'Ba': 0.89, 'Hf': 1.3, 'Ta': 1.5, 'W': 2.36, 'Re': 1.9, 'Os': 2.2, 'Ir': 2.2, 'Pt': 2.28, 'Au': 2.54, 'Hg': 2.0, 'Tl': 1.62,
 'Pb': 2.33, 'Bi': 2.02,
}

# Dicionário com índice arbitrário (nenhum significado físico) para cada elemento químico 
valor_para_elemento = {
1: 'H', 2: 'Li', 3: 'Be', 4: 'B', 5: 'C', 6: 'N', 7: 'O', 8: 'F', 9: 'Na', 10: 'Mg', 11: 'Al', 12: 'Si', 13: 'P', 14: 'S', 15: 'Cl', 16: 'K', 
17: 'Ca', 18: 'Sc', 19: 'Ti', 20: 'V', 21: 'Cr', 22: 'Mn', 23: 'Fe', 24: 'Co', 25: 'Ni', 26: 'Cu', 27: 'Zn', 28: 'Ga', 29: 'Ge', 30: 'As', 31: 'Se', 
32: 'Br', 33: 'Rb', 34: 'Sr', 35: 'Y', 36: 'Zr', 37: 'Nb', 38: 'Mo', 39: 'Ru', 40: 'Rh', 41: 'Pd', 42: 'Ag', 43: 'Cd', 44: 'In', 45: 'Sn', 46: 'Sb', 
47: 'Te', 48: 'I', 49: 'Cs', 50: 'Ba', 51: 'Hf', 52: 'Ta', 53: 'W', 54: 'Re', 55: 'Os', 56: 'Ir', 57: 'Pt', 58: 'Au', 59: 'Hg', 60: 'Tl', 61: 'Pb', 62: 'Bi',
}


def individuo_bgcf(n):
    """Cria uma indivíduo estilizado para o problema dos materiais 2D.

    Args:
      n: inteiro que representa a dimenção (os elementos químicos) de cada indivíduo.

    """
    pesos = [0.90] + [0.010] * 10
    
    individuo = []
    for _ in range(n):
        valor = random.choices(range(11), weights=pesos, k=1)[0]
        individuo.append(valor)
    
    while sum(1 for x in individuo if x != 0) < 2:
        individuo[random.randint(0, len(individuo) - 1)] = random.randint(1, 10)
        individuo[random.randint(0, len(individuo) - 1)] = random.randint(1, 10)
    
    return individuo



def populacao_bgcf(tamanho, n):
    """Cria uma população para o problema dos materiais 2D.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa a dimenção (os elementos químicos) de cada indivíduo.

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_bgcf(n))
    return populacao



def objetivo_bgcf(individuo):
    """Computa a função objetivo estilizada para o problema dos materiais 2D de um indivíduo.

    Args:
      individuo: lista contendo os genes do indivíduo.

    """
    individuo_reshape = np.array(individuo).reshape(1, -1)
    bandgap = modelo_bg.predict(individuo_reshape)[0]
    calor = modelo_cf.predict(individuo_reshape)[0]
    
    if calor <= 0:
        soma = (2 * bandgap) + abs(calor)  
    else: 
        soma = (2 * bandgap) - calor  

    return soma

    
    
def objetivo_pop_bgcf(populacao):
    """Computa a função objetivo estilizada para o problema dos materiais 2D de uma população.

    Args:
      populacao: lista contendo os individuos do problema.

    """
    fitness = []
    for individuo in populacao:
        fitness.append(objetivo_bgcf(individuo))
    return fitness


def cruzamento_ponto_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo.

    Args:
      pai: lista representando um individuo.
      mae: lista representando um individuo.
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento.

    """
    if random.random() < chance_de_cruzamento:
        while True:
            corte1 = random.randint(1, len(mae) - 2)
            corte2 = random.randint(corte1 + 1, len(mae) - 1)
            filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
            filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
            
            if sum(filho1) != 0 and sum(filho2) != 0:
                break
            
        return filho1, filho2
    else:
        return pai, mae

    

def mutacao_bgcf(populacao, chance_de_mutacao):
    """Realiza mutação estilizada para o problema dos materiais 2D.

    Args:
      populacao: lista contendo os indivíduos do problema.
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação.

    """
    valores_possiveis = range(1, 11)
    
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            tipo_de_mutacao = random.randint(0, 1)
            
            # Mutação de alteração
            if tipo_de_mutacao == 0:  
                genes_nao_zero = [(i, gene) for i, gene in enumerate(individuo) if gene != 0]
                indices = [tupla[0] + 1 for tupla in genes_nao_zero]
                duplas = [(list(valor_para_elemento.keys())[i-1], eletronegatividades[valor_para_elemento[i]]) for i in indices]
                eletronegatividade = [tupla[1] for tupla in duplas]
                maior = max(eletronegatividade)
                chave = [tupla[0] for tupla in duplas if tupla[1] == maior]
                indice = chave[0] - 1
                individuo[indice] = random.choice(range(individuo[indice] + 1, max(valores_possiveis)))
                
            # Mutação de adição
            else:  
                genes_zero = [(i, gene) for i, gene in enumerate(individuo) if gene == 0]
                indices = [tupla[0] + 1 for tupla in genes_zero]
                duplas = [(list(valor_para_elemento.keys())[i-1], eletronegatividades[valor_para_elemento[i]]) for i in indices]
                eletronegatividade = [tupla[1] for tupla in duplas]
                maior = max(eletronegatividade)
                chave = [tupla[0] for tupla in duplas if tupla[1] == maior]
                indice = chave[0] - 1
                individuo[indice] = random.choice(range(1, max(valores_possiveis)))
                
    return populacao


                
def selecao_roleta_max(populacao, fitness):
    """Realiza seleção da população pela roleta.

    Args:
      populacao: lista contendo os individuos do problema.
      fitness: lista contendo os valores computados da funcao objetivo.

    """
    selecionados = random.choices(populacao, fitness, k=len(populacao))
    return selecionados