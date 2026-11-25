# 1. Entrada de dados (o computador pergunta e guarda a resposta)
produto = input("Digite o nome do produto: ")
estoque_inicial = int(input("Quantidade de caixas no início do dia: "))
saidas = int(input("Quantidade de caixas expedidas hoje: "))

# 2. Processamento (cálculo matemático)
estoque_final = estoque_inicial - saidas

# 3. Saída e Tomada de Decisão (if / else)
print("-------------------------------")
print("Produto:", produto)
print("Estoque atual:", estoque_final, "caixas")

if estoque_final < 10:
    print("ALERTA: Estoque baixo! Solicitar reposição.")
else:
    print("STATUS: Estoque normalizado.")

quantidade_itens = int(input("Quantos produtos você quer conferir hoje? "))

for i in range(quantidade_itens):
    print(f"\n--- Conferindo item {i + 1} ---")
    produto = input("Nome do produto: ")
    estoque_inicial = int(input("Estoque inicial: "))
    saidas = int(input("Caixas expedidas: "))
    
    estoque_final = estoque_inicial - saidas
    print(f"Saldo de {produto}: {estoque_final} caixas.")
    
    if estoque_final <= 15:
        print("ALERTA: Solicitar reposição!")
    else:
        print("STATUS: Estoque OK.")

print("\nConferência do dia finalizada!")

quantidade_itens = int(input("Quantos produtos serão conferidos?"))

total_expedido = 0
produtos_em_alerta = []

for i in range(quantidade_itens):
    print(f"\n--- Item {i + 1} ---")
    produto = input("Nome do produto:")
    estoque_inicial = int(input("Estoque incial:"))
    saidas = int(input("Caixas expedidas hoje:"))

    estoque_final = estoque_inicial - saidas
    total_expedido = total_expedido + saidas #Acumula o total de caixas que saíram

    if estoque_final <= 15:
        produtos_em_alerta.append(produto) #Guarda o nome do produto na lista de alerta

print("\n===============================")
print("Resumo da Operaçãó do dia")
print(f"Total geral de caixas expedidas: {total_expedido}")
print(f"Produtos que precisam de reposição: {produtos_em_alerta}")
print("==================================")

with open("relatorio_expedicao.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO DE EXPEDIÇÃO DO DIA\n")
    arquivo.write(f"Total geral de caixas expedidas: {total_expedido}\n")
    arquivo.write(f"Produtos para reposição:{produtos_em_alerta}\n")

print("Arquivo 'relatorio_expedicao.txt' gerado comm sucesso!")