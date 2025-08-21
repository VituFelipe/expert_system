# -*- coding: utf-8 -*-
import json

def carregar_regras(arquivo='regras_refeicoes.json'):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "cafe da manha": {
                "vegetariana": {
                    "saudavel": {"leve": "Aveia com frutas frescas", "medio": "Smoothie de iogurte vegetal", "pesado": "Torradas com abacate"},
                    "comfort": {"leve": "Panquecas de banana", "medio": "Waffles com frutas", "pesado": "Panquecas com xarope"}
                },
                "nao vegetariana": {
                    "saudavel": {"leve": "Ovos mexidos com vegetais", "medio": "Omelete com espinafre", "pesado": "Ovos com bacon"},
                    "comfort": {"leve": "Torrada com manteiga", "medio": "Bacon com ovos", "pesado": "Omelete com queijo"}
                }
            },
            "almoco": {
                "vegetariana": {
                    "saudavel": {"leve": "Salada de quinoa", "medio": "Quinoa com vegetais", "pesado": "Risoto de cogumelos"},
                    "comfort": {"leve": "Macarrao ao pesto", "medio": "Lasanha vegetariana leve", "pesado": "Lasanha vegetariana completa"}
                },
                "nao vegetariana": {
                    "saudavel": {"leve": "Frango grelhado com salada", "medio": "Peito de frango com arroz", "pesado": "Carne grelhada"},
                    "comfort": {"leve": "Hamburguer com salada", "medio": "Hamburguer com batatas", "pesado": "Costela com molho"}
                }
            },
            "jantar": {
                "vegetariana": {
                    "saudavel": {"leve": "Sopa de legumes", "medio": "Sopa de abobora", "pesado": "Curry de vegetais"},
                    "comfort": {"leve": "Lasanha vegetariana pequena", "medio": "Risoto de queijo", "pesado": "Lasanha vegetariana grande"}
                },
                "nao vegetariana": {
                    "saudavel": {"leve": "Peixe assado com vegetais", "medio": "Salmão grelhado", "pesado": "Peixe com batatas"},
                    "comfort": {"leve": "Bife com molho leve", "medio": "Bife com pure", "pesado": "Bife com batatas e molho"}
                }
            }
        }

def inferir_recomendacao(fatos, regras):
    horario = fatos["horario"]
    dieta = fatos["dieta"]
    humor = fatos["humor"]
    fome = fatos["fome"]
    recomendacao = regras[horario][dieta][humor][fome]
    return [(recomendacao, f"Recomendacao baseada em: horario={horario}, dieta={dieta}, humor={humor}, fome={fome}")]

def validar_entrada(opcoes, prompt):
    while True:
        entrada = input(prompt).strip().lower()
        if entrada in opcoes:
            return entrada
        print(f"Entrada invalida. Opcoes: {', '.join(opcoes)}")

def coletar_fatos():
    fatos = {}
    fatos["dieta"] = validar_entrada(['sim', 'nao'], "Voce e vegetariano? (sim/nao): ")
    fatos["dieta"] = "vegetariana" if fatos["dieta"] == "sim" else "nao vegetariana"
    fatos["horario"] = validar_entrada(['cafe da manha', 'almoco', 'jantar'], "Qual refeicao? (cafe da manha/almoco/jantar): ")
    fatos["humor"] = validar_entrada(['saudavel', 'comfort'], "Seu humor para a refeicao? (saudavel/comfort): ")
    fatos["fome"] = validar_entrada(['leve', 'medio', 'pesado'], "Nivel de fome? (leve/medio/pesado): ")
    return fatos

if __name__ == "__main__":
    regras = carregar_regras()
    print("Bem-vindo ao Sistema Especialista de Planejamento de Refeicoes!")
    while True:
        fatos = coletar_fatos()
        recomendacoes = inferir_recomendacao(fatos, regras)
        print("\nRecomendacoes:")
        for acao, explicacao in recomendacoes:
            print(f"- {acao}")
            print(f"  Explicacao: {explicacao}")
        if input("\nDeseja outra consulta? (sim/nao): ").strip().lower() != 'sim':
            break