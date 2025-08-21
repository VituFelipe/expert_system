# -*- coding: utf-8 -*-
import json

# Funcao para carregar regras de um arquivo JSON
def carregar_regras(arquivo='regras_refeicoes.json'):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo de regras nao encontrado. Usando regras padrao.")
        return [
            {"condicoes": {"horario": "cafe da manha", "dieta": "vegetariana", "humor": "saudavel", "fome": "leve"}, "acao": "Aveia com frutas frescas (leve e nutritiva)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "vegetariana", "humor": "saudavel", "fome": "medio"}, "acao": "Smoothie de iogurte vegetal com frutas (equilibrado)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "vegetariana", "humor": "saudavel", "fome": "pesado"}, "acao": "Torradas com abacate e ovos vegetais (satisfatorio)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "leve"}, "acao": "Ovos mexidos com vegetais (proteina leve)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "medio"}, "acao": "Omelete com espinafre (saudavel e saciante)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "pesado"}, "acao": "Ovos com bacon e torradas (forte e nutritivo)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "vegetariana", "humor": "comfort", "fome": "leve"}, "acao": "Panquecas de banana com mel (reconfortante e leve)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "vegetariana", "humor": "comfort", "fome": "medio"}, "acao": "Waffles com frutas (doce e reconfortante)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "vegetariana", "humor": "comfort", "fome": "pesado"}, "acao": "Panquecas com xarope (satisfatorio e reconfortante)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "nao vegetariana", "humor": "comfort", "fome": "leve"}, "acao": "Torrada com manteiga e geleia (simples e reconfortante)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "nao vegetariana", "humor": "comfort", "fome": "medio"}, "acao": "Bacon com ovos (classico reconfortante)."},
            {"condicoes": {"horario": "cafe da manha", "dieta": "nao vegetariana", "humor": "comfort", "fome": "pesado"}, "acao": "Omelete com queijo e bacon (forte e reconfortante)."},
            {"condicoes": {"horario": "almoco", "dieta": "vegetariana", "humor": "saudavel", "fome": "leve"}, "acao": "Salada de quinoa com legumes (saudavel e vegana)."},
            {"condicoes": {"horario": "almoco", "dieta": "vegetariana", "humor": "saudavel", "fome": "medio"}, "acao": "Quinoa com vegetais grelhados (nutritivo)."},
            {"condicoes": {"horario": "almoco", "dieta": "vegetariana", "humor": "saudavel", "fome": "pesado"}, "acao": "Risoto de cogumelos (saudavel e saciante)."},
            {"condicoes": {"horario": "almoco", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "leve"}, "acao": "Frango grelhado com salada (equilibrado)."},
            {"condicoes": {"horario": "almoco", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "medio"}, "acao": "Peito de frango com arroz integral (saudavel)."},
            {"condicoes": {"horario": "almoco", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "pesado"}, "acao": "Carne grelhada com legumes (forte e saudavel)."},
            {"condicoes": {"horario": "almoco", "dieta": "vegetariana", "humor": "comfort", "fome": "leve"}, "acao": "Macarrao ao pesto (simples e saboroso)."},
            {"condicoes": {"horario": "almoco", "dieta": "vegetariana", "humor": "comfort", "fome": "medio"}, "acao": "Lasanha vegetariana leve (saborosa)."},
            {"condicoes": {"horario": "almoco", "dieta": "vegetariana", "humor": "comfort", "fome": "pesado"}, "acao": "Lasanha vegetariana completa (reconfortante)."},
            {"condicoes": {"horario": "almoco", "dieta": "nao vegetariana", "humor": "comfort", "fome": "leve"}, "acao": "Hamburguer com salada (leve e reconfortante)."},
            {"condicoes": {"horario": "almoco", "dieta": "nao vegetariana", "humor": "comfort", "fome": "medio"}, "acao": "Hamburguer com batatas (classico)."},
            {"condicoes": {"horario": "almoco", "dieta": "nao vegetariana", "humor": "comfort", "fome": "pesado"}, "acao": "Costela com molho (forte e reconfortante)."},
            {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "saudavel", "fome": "leve"}, "acao": "Sopa de legumes (leve para a noite)."},
            {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "saudavel", "fome": "medio"}, "acao": "Sopa de abobora com torrada (nutritiva)."},
            {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "saudavel", "fome": "pesado"}, "acao": "Curry de vegetais com arroz (saudavel e saciante)."},
            {"condicoes": {"horario": "jantar", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "leve"}, "acao": "Peixe assado com vegetais (omega-3 saudavel)."},
            {"condicoes": {"horario": "jantar", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "medio"}, "acao": "Salmão grelhado com salada (leve)."},
            {"condicoes": {"horario": "jantar", "dieta": "nao vegetariana", "humor": "saudavel", "fome": "pesado"}, "acao": "Peixe com batatas assadas (forte e saudavel)."},
            {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "comfort", "fome": "leve"}, "acao": "Lasanha vegetariana pequena (quente e leve)."},
            {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "comfort", "fome": "medio"}, "acao": "Risoto de queijo (cremoso e reconfortante)."},
            {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "comfort", "fome": "pesado"}, "acao": "Lasanha vegetariana grande (reconfortante)."},
            {"condicoes": {"horario": "jantar", "dieta": "nao vegetariana", "humor": "comfort", "fome": "leve"}, "acao": "Bife com molho leve (simples)."},
            {"condicoes": {"horario": "jantar", "dieta": "nao vegetariana", "humor": "comfort", "fome": "medio"}, "acao": "Bife com pure (classico)."},
            {"condicoes": {"horario": "jantar", "dieta": "nao vegetariana", "humor": "comfort", "fome": "pesado"}, "acao": "Bife com batatas e molho (forte e reconfortante)."}
        ]

# Funcao auxiliar para formatar condicoes
def formatar_condicoes(condicoes):
    return ', '.join(f'{k}={v}' for k, v in condicoes.items())

# Mecanismo de Inferencia (Encadeamento para Frente, retorna multiplas e explicacoes)
def inferir_recomendacao(fatos, regras):
    recomendacoes = []
    for idx, regra in enumerate(regras):
        if all(fatos.get(chave) == valor for chave, valor in regra["condicoes"].items()):
            condicoes_str = formatar_condicoes(regra["condicoes"])
            explicacao = "Regra {} aplicada: Se {}, entao {}".format(idx + 1, condicoes_str, regra['acao'])
            recomendacoes.append((regra["acao"], explicacao))
    if recomendacoes:
        return recomendacoes
    return [("Nenhuma recomendacao encontrada. Tente ajustar preferencias.", "Nenhuma regra correspondeu aos fatos fornecidos.")]

# Validacao de Entradas
def validar_entrada(opcoes, prompt):
    while True:
        entrada = input(prompt).strip().lower()
        print(f"Depuracao: Entrada recebida: '{entrada}'")  # Adicionado para depuracao
        if entrada in opcoes:
            return entrada
        print(f"Entrada invalida. Opcoes: {', '.join(opcoes)}")

# Coleta de Fatos
def coletar_fatos():
    fatos = {}
    fatos["dieta"] = validar_entrada(['sim', 'nao'], "Voce e vegetariano? (sim/nao): ")
    if fatos["dieta"] == "sim":
        fatos["dieta"] = "vegetariana"
    else:
        fatos["dieta"] = "nao vegetariana"
    fatos["horario"] = validar_entrada(['cafe da manha', 'almoco', 'jantar'], "Qual refeicao? (cafe da manha/almoco/jantar): ")
    fatos["humor"] = validar_entrada(['saudavel', 'comfort'], "Seu humor para a refeicao? (saudavel/comfort): ")
    fatos["fome"] = validar_entrada(['leve', 'medio', 'pesado'], "Nivel de fome? (leve/medio/pesado): ")
    return fatos

# Execucao Principal com Loop
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