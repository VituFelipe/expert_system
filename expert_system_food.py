# -*- coding: utf-8 -*-
regras = [
    # Regras para café da manhã
    {"condicoes": {"horario": "café da manhã", "dieta": "vegetariana", "humor": "saudável"}, "acao": "Recomendo aveia com frutas frescas (leve e nutritiva)."},
    {"condicoes": {"horario": "café da manhã", "dieta": "vegetariana", "humor": "comfort"}, "acao": "Recomendo panquecas de banana com mel (reconfortante e sem carne)."},
    {"condicoes": {"horario": "café da manhã", "dieta": "não vegetariana", "humor": "saudável"}, "acao": "Recomendo ovos mexidos com vegetais (proteína leve)."},
    {"condicoes": {"horario": "café da manhã", "dieta": "não vegetariana", "humor": "comfort"}, "acao": "Recomendo bacon com torradas (clássico e reconfortante)."},
    
    # Regras para almoço
    {"condicoes": {"horario": "almoço", "dieta": "vegetariana", "humor": "saudável"}, "acao": "Recomendo salada de quinoa com legumes (saudável e vegana)."},
    {"condicoes": {"horario": "almoço", "dieta": "vegetariana", "humor": "comfort"}, "acao": "Recomendo macarrão ao pesto (simples e saboroso)."},
    {"condicoes": {"horario": "almoço", "dieta": "não vegetariana", "humor": "saudável"}, "acao": "Recomendo frango grelhado com salada (equilibrado)."},
    {"condicoes": {"horario": "almoço", "dieta": "não vegetariana", "humor": "comfort"}, "acao": "Recomendo hambúrguer com batatas (reconfortante)."},
    
    # Regras para jantar
    {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "saudável"}, "acao": "Recomendo sopa de legumes (leve para a noite)."},
    {"condicoes": {"horario": "jantar", "dieta": "vegetariana", "humor": "comfort"}, "acao": "Recomendo lasanha vegetariana (quente e satisfatória)."},
    {"condicoes": {"horario": "jantar", "dieta": "não vegetariana", "humor": "saudável"}, "acao": "Recomendo peixe assado com vegetais (ômega-3 saudável)."},
    {"condicoes": {"horario": "jantar", "dieta": "não vegetariana", "humor": "comfort"}, "acao": "Recomendo bife com purê (clássico reconfortante)."}
]

# Mecanismo de inferencia (Encadeamento para Frente)
def inferir_recomendacao(fatos):
    for regra in regras:
        # aqui é pa verifica se todas as condições da regra correspondem aos fatos
        if all(fatos.get(chave) == valor for chave, valor in regra["condicoes"].items()):
            return regra["acao"]
    return "Desculpe, nao encontrei uma recomendacao baseada nas suas preferencias. Tente outras opcoes!"

# Interface com o usuario por input memo
def coletar_fatos():
    fatos = {}
    print("Bem-vindo ao Sistema Especialista de Planejamento de Refeições!")
    fatos["dieta"] = input("Você é vegetariano? (sim/nao): ").strip().lower()
    if fatos["dieta"] == "sim":
        fatos["dieta"] = "vegetariana"
    else:
        fatos["dieta"] = "não vegetariana"
    
    fatos["horario"] = input("Qual refeicao? (cafe da manha/almoço/jantar): ").strip().lower()
    
    fatos["humor"] = input("Seu humor para a refeicao? (saudavel/comfort): ").strip().lower()
    
    return fatos

# Execução do Sistema
if __name__ == "__main__":
    fatos = coletar_fatos()
    recomendacao = inferir_recomendacao(fatos)
    print("\nRecomendação:", recomendacao)
    print("Explicação: Esta sugestão é baseada em regras de produção que combinam sua dieta, horário e humor.")