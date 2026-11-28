# Funcão reutiliável para garantir que o usuário digite um número válido

def ler_numero_inteiro(mensagem, minimo = 0):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Erro: O número deve ser no mínimo {minimo}. Tente novamente.")

            else:
                return valor
        except ValueError:
            print("Erro: Digite apenas números inteiros (Ex.: 10, 25).")


# ---- Início main ------

quantidade_itens = ler_numero_inteiro("Quantos produtos serão conferidos hoje? ", minimo=1 )
total_expedido = 0
produtos_em_alerta = []

for i in range(quantidade_itens):
    print(f"\n --- Item {i + 1} ---")
    produto = input("Nome do produto: ")
    estoque_inicial = ler_numero_inteiro("Estoque Inicial: ")

# Impedir que a saída seja maior que o estoque disponível.. 

while True:
    saidas = ler_numero_inteiro("Caixas expedidas hoje: ")
    if saidas > estoque_inicial:
        print(f"Erro: Você só tem {estoque_inicial} caixas em estoque! ")

    else:
        break

estoque_final = estoque_inicial - saidas
total_expedido += saidas

print(f"Saldo atual de {produto}: {estoque_final} caixas.")
if estoque_final <= 15:
    print("ALERTA: Estoque baixo!")
    produtos_em_alerta.append(produto)


print("\n===============================")
print("Resumo da Operação do dia")
print(f"Total geral de caixas expedidas: {total_expedido}")
print(f"Produtos que precisam de reposição: {produtos_em_alerta}")
print("\n===============================")