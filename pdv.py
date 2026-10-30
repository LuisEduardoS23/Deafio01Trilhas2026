compras = []

while True:
    valor = float(input("Valor da compra em R$ (0 para encerrar): "))
    if valor == 0:
        break
    if valor < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.")
        continue

    idade = int(input("Idade do cliente: "))
    if idade < 0:
        print("Aviso: a idade não pode ser negativa. Tente novamente.")
        continue

    valor_final = valor
    if idade >= 65:
        valor_final = valor_final * 0.8

    if valor_final > 100:
        valor_final = valor_final * 0.9

    valor_final = round(valor_final, 2)
    print(f"Valor final: R$ {valor_final:.2f}")

    compras.append((valor, valor_final))


total_bruto = 0
total_final = 0
for bruto, final in compras:
    total_bruto += bruto
    total_final += final

total_descontos = total_bruto - total_final

print("\n--- Resumo do dia ---")
print(f"Quantidade de compras: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")