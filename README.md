# PDV com Descontos

## O que o código faz

Este programa simula a lógica de um PDV (Ponto de Venda). Ele recebe o valor de uma compra e a idade do cliente, aplica descontos progressivos de acordo com regras de negócio e mostra o valor final em reais. Várias compras podem ser registradas em sequência e, ao encerrar, o programa exibe um resumo do dia.

## Como ele faz

1. O código pede o valor da compra. Se o valor for `0`, o loop termina.
2. Se o valor for negativo, mostra um aviso e pede novamente.
3. Pede a idade do cliente. Se for negativa, mostra um aviso e pede novamente.
4. Se a idade for maior ou igual a 65, aplica 20% de desconto.
5. Depois, se o valor já descontado pela idade for maior que 100, aplica mais 10% de desconto sobre esse valor.
6. Arredonda para duas casas decimais e exibe o valor final (ex.: `R$ 144.00`).
7. Guarda a compra (valor original e valor final) numa lista com `.append()`.
8. Ao encerrar, percorre a lista e mostra: quantidade de compras, total bruto, total de descontos e total final.

## Como rodar

```
python pdv.py
```

## Tabela de exemplos

Cole aqui a tabela de casos de teste do enunciado (valor, idade e valor final esperado).

Casos-limite para conferir:

| Valor | Idade | Valor final esperado | Observação |
|-------|-------|----------------------|------------|
| 125.00 | 70 | R$ 100.00 | 125 × 0.8 = 100, não passa de 100, então não há os 10% |
| 200.00 | 64 | R$ 180.00 | Sem desconto de idade, só o de valor |
| 101.00 | 30 | R$ 90.90 | 101 × 0.9 = 90.90 |
