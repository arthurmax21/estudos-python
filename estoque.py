#1 Pergunta quantos itens vamos conferir e cria as "caixas" vaizas para guardar os resultados
quantidade_itens = int(input("Quantos produtos serão conferidos hoje?"))
total_expedido = 0
produtos_em_alerta = []

#2 Repete o processo para cada produto( O "i" conta de 0 até a quantidade escolhida)

for i in range(quantidade_itens):
    print(f"\n--- Item {i + 1} ---")

produto = input("Nome do produto:")
estoque_inicial = int(input("Estoque inicial: "))
saidas = int(input("caixas expedidas hoje: "))

    ## Calcular o saldo e soma, no total geral do dia

estoque_final = estoque_inicial - saidas
total_expedido = total_expedido + saidas

    ## Mostra o saldo imediato deste item e verifica se precisa de reposição

print(f"Saldo atual de {produto}: {estoque_final} caixas.")
if estoque_final <= 15:
    print("Alerta: Estoque baixo!!")
    produtos_em_alerta.append(produto)


#3 Exibe o resumo geral na tela do terminal

print("\n==================================")
print("Resumo da operação do dia")
print(f"Total geral de caixas expedidas: {total_expedido}")
print(f"Produtos que precisam de reposição: {produtos_em_alerta}")
print("\n==================================")

#4 Grava esse resumo aí dentro de um arquivo de texto txt.
with open("relatorio_expedicao.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("Relatório de Expedição do dia\n")
    arquivo.write(f"Total geral de caixas expedidas: {total_expedido}\n")
    arquivo.write(f"Produtos para reposição: {produtos_em_alerta}\n")

print("Arquivo 'relatorio_expediçao.txt' gerado com sucesso!!")

