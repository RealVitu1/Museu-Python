import json
from datetime import datetime

#Classes Principais

class ObraDeArte:
    def __init__(self, titulo, data_criacao, tema, estilo, descricao, tecnica, autor, localizacao):
        self.titulo = titulo
        self.data_criacao = data_criacao
        self.tema = tema
        self.estilo = estilo
        self.descricao = descricao
        self.tecnica = tecnica
        self.autor = autor
        self.localizacao = localizacao
        self.documentos = []
        self.figuras_proeminentes = []

    def adicionar_documento(self, documento):
        self.documentos.append(documento)
    
    def adicionar_figura_proeminente(self, figura):
        self.figuras_proeminentes.append(figura)
    
    def __repr__(self):
        return f"ObraDeArte({self.titulo}, {self.autor.nome}, {self.data_criacao})"

class Artista:
    def __init__(self, nome, data_nascimento, local_nascimento, biografia, estilos):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.local_nascimento = local_nascimento
        self.biografia = biografia
        self.estilos = estilos
    
    def __repr__(self):
        return f"Artista({self.nome}, {self.data_nascimento})"

class EstiloArtistico:
    def __init__(self, denominacao, periodo_influencia, descricao, escola_representativa):
        self.denominacao = denominacao
        self.periodo_influencia = periodo_influencia
        self.descricao = descricao
        self.escola_representativa = escola_representativa
    
    def __repr__(self):
        return f"EstiloArtistico({self.denominacao})"

class Documento:
    def __init__(self, tipo, descricao):
        self.tipo = tipo
        self.descricao = descricao
    
    def __repr__(self):
        return f"Documento({self.tipo})"

class FiguraProeminente:
    def __init__(self, nome, biografia):
        self.nome = nome
        self.biografia = biografia
    
    def __repr__(self):
        return f"FiguraProeminente({self.nome})"

class Emprestimos:
    def __init__(self, obra, periodo, evento, responsavel, tema):
        self.obra = obra
        self.periodo = periodo
        self.evento = evento
        self.responsavel = responsavel
        self.tema = tema
    
    def __repr__(self):
        return f"Emprestimos({self.obra.titulo}, {self.evento})"

class VisitaGuiada:
    def __init__(self, tema, descricao, obras):
        self.tema = tema
        self.descricao = descricao
        self.obras = obras
    
    def __repr__(self):
        return f"VisitaGuiada({self.tema})"

#Funções Auxiliares

def salvar_dados(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, default=str)
        print(f"Dados salvos em {filename}.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Dados carregados de {filename}.")
        return data
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
    return None

def selection_sort(obras, chave):
    try:
        for i in range(len(obras)):
            min_idx = i
            for j in range(i+1, len(obras)):
                if getattr(obras[j], chave) < getattr(obras[min_idx], chave):
                    min_idx = j
            obras[i], obras[min_idx] = obras[min_idx], obras[i]
        print(f"Obras ordenadas por {chave}.")
    except AttributeError:
        print(f"Atributo {chave} não encontrado nas obras.")
    except Exception as e:
        print(f"Erro ao ordenar obras: {e}")

#Exemplos de Uso

#Registro de um novo artista e estilo artístico
artista1 = Artista("Pablo Picasso", "1881-10-25", "Málaga, Espanha", "Pintor e escultor espanhol, co-fundador do cubismo", ["Cubismo"])
artista2 = Artista("Vincent van Gogh", "1853-03-30", "Zundert, Países Baixos", "Pintor pós-impressionista", ["Pós-Impressionismo"])

estilo1 = EstiloArtistico("Cubismo", "1907-1920", "Estilo caracterizado pela fragmentação do objeto em formas geométricas", "Escola de Paris")
estilo2 = EstiloArtistico("Pós-Impressionismo", "1880-1920", "Movimento artístico que sucedeu o Impressionismo, caracterizado pela subjetividade e pela ênfase em cores vivas e traços expressivos", "Nenhuma escola específica")

#Adicionando várias obras de arte
obra1 = ObraDeArte("Les Demoiselles d'Avignon", "1907", "Retrato", estilo1, "Obra que marca o início do Cubismo", "Óleo sobre tela", artista1, "Sala Cubismo")
obra2 = ObraDeArte("Guernica", "1937", "Pintura histórica", estilo1, "Representação do bombardeio de Guernica durante a Guerra Civil Espanhola", "Óleo sobre tela", artista1, "Sala de Guerra")
obra3 = ObraDeArte("Starry Night", "1889", "Paisagem", estilo2, "Uma das pinturas mais conhecidas de Van Gogh", "Óleo sobre tela", artista2, "Sala Pós-Impressionismo")

obras = [obra1, obra2, obra3]

#Registro de um empréstimo de uma obra de arte
Emprestimos1 = Emprestimos(obra1, "2023-05-01 a 2023-08-01", "Exposição de Cubismo", "Museu de Arte Moderna", "Cubismo na Arte Moderna")

#Criação e salvamento de um roteiro de visita guiada
visita1 = VisitaGuiada("Obras de Pablo Picasso", "Visita guiada pelas principais obras de Picasso no museu", [obra1, obra2])

#Salvando dados em arquivos
salvar_dados([artista1.__dict__, artista2.__dict__], 'artistas.json')
salvar_dados([estilo1.__dict__, estilo2.__dict__], 'estilos.json')
salvar_dados([obra.__dict__ for obra in obras], 'obras.json')
salvar_dados([Emprestimos1.__dict__], 'Emprestimoss.json')
salvar_dados([visita1.__dict__], 'visitas.json')

#Carregando dados de arquivos
artistas_carregados = carregar_dados('artistas.json')
estilos_carregados = carregar_dados('estilos.json')
obras_carregadas = carregar_dados('obras.json')
Emprestimoss_carregados = carregar_dados('Emprestimoss.json')
visitas_carregadas = carregar_dados('visitas.json')

#Ordenar obras por data de criação usando Selection Sort
selection_sort(obras, 'data_criacao')

#Exibindo dados carregados e ordenados
print("Artistas carregados:", artistas_carregados)
print("Estilos carregados:", estilos_carregados)
print("Obras carregadas:", obras_carregadas)
print("Empréstimos carregados:", Emprestimoss_carregados)
print("Visitas carregadas:", visitas_carregadas)
print("Obras ordenadas por data de criação:", obras)
